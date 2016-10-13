__author__ = 'zhangtianren'
import urllib,time
import iknow.settings
import os
from django.http import HttpResponse,request
from mysql import connector
import simplejson as json
from django import forms
from  forms import DocumentForm
from django.test import TestCase
# from django.views.decorators.csrf import csrf_exempt
import socket
import oss2
from sqlite3 import OperationalError
from django.shortcuts import render_to_response
import model


endpoint='http://oss-us-west-1.aliyuncs.com'
ali='http://arroyo.oss-us-west-1.aliyuncs.com/'
auth = oss2.Auth('h9p8vicTD1xAplNn', 'symR186PUptAyQJnF0sKFNeHtGD2jl')
bucket = oss2.Bucket(auth, endpoint, 'arroyo')

myname = socket.getfqdn(socket.gethostname(  ))
myaddr = socket.gethostbyname(myname)

sql1=('SELECT noteid,posted_notes.netid,avatar,nickname,cover,notepic,notecls,posttime,clstime,likenum,picnum from note_users,posted_notes WHERE note_users.netid=posted_notes.netid')
sql2=('INSERT INTO note_users VALUES(%s,%s,%s,%s,%s,%s)')
sql3=('UPDATE note_users set avatar=%s WHERE netid=%s')
sql4=('INSERT INTO posted_notes VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)')
sql5=('SELECT * from note_user,posted_notes WHERE noteid=%s AND note_user.netid=posted_notes.netid')
sql6=('UPDATE note_users set nickname=%s WHERE netid=%s')
sql7=("SELECT  posted_notes.netid,noteid,avatar,nickname,cover,notepic,notecls,posttime,likenum,picnum from note_users,posted_notes WHERE notecls='%s' AND posted_notes.netid=note_users.netid")
sql8=("UPDATE posted_notes SET likenum=likenum+1 WHERE noteid='%s'")
sql9=("SELECT pswd FROM note_users WHERE netid='%s'")
sql10=("INSERT INTO collected_notes VALUES(%s,%s)")

sql11=("SELECT noteid FROM collected_notes WHERE netid='%s'")
sql12=("SELECT notepic,noteid,posted_notes.netid,avatar,nickname,cover,notecls,posttime,clstime,likenum,picnum from note_users,posted_notes WHERE note_users.netid=posted_notes.netid AND posted_notes.noteid='%s'")

sql13=("UPDATE note_users SET takingcls='%s' WHERE netid='%s'")
sql14=("SELECT takingcls FROM note_users WHERE netid='%s'")

sql15=("SELECT netid FROM like_notes WHERE noteid='%s'")
sql16=("insert into like_notes values('%s','%s')")
sql17=("delete from collected_notes where noteid='%s'")

sql18=("SELECT netid FROM collected_notes WHERE noteid='%s'")
sql19=("SELECT avatar,nickname,takingcls FROM note_users WHERE netid='%s'")

sql20=("SELECT noteid,posted_notes.netid,avatar,nickname,cover,notepic,notecls,posttime,clstime,likenum,picnum from note_users,posted_notes WHERE note_users.netid=posted_notes.netid AND note_users.netid='%s'")


try:
    cnx=connector.connect(host="127.0.0.1",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")

except OperationalError:
    cnx=connector.connect(host="127.0.0.1",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")

#db0=cnx.cursor(dictionary=True)
#db0.execute('ALTER TABLE posted_notes CHANGE puttime posttime varchar(100);')


file = open('C:\iknow\iknow\myApp\class.txt', 'r')
allclass=[]
for row in file.read().split('.'):
    allclass.append(row.replace('\n',''))


def gettime(note):
    return note['posttime']

def query(request):
    cnx=connector.connect(host="127.0.0.1",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")
    data=[]
    db0=cnx.cursor(dictionary=True)
    db0.execute(sql1)
    for row in db0:
        data.append(row)
    data.sort(key=gettime,reverse=True)
    for i in data:
        i['likepeople']=getlike(i['noteid'])
    return HttpResponse(json.dumps(data,ensure_ascii=False))

def getlike(noteid):
    cnx=connector.connect(host="127.0.0.1",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")
    like=[]
    db0=cnx.cursor()
    db0.execute(sql15%noteid)
    for row in db0:
        like.append(row[0])
    return like

def getclass(request):
    filepath=os.path.join(iknow.settings.BASE_DIR, 'myApp/')
    f=open(filepath+'class.txt','r')
    content=f.read()
    f.close()
    return HttpResponse(content)

def create(request):
    cnx=connector.connect(host="127.0.0.1",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")

    if request.method=='POST':
        userid=request.POST.get('userid')
        pswd=request.POST.get('pswd')
        username=request.POST.get('username')
        avatar = request.FILES['avatar']
        takingcls=request.POST.get('takingcls')
        pswd=request.POST.get('pswd')
        #print(userid,username,avatar)
        file_name = userid+avatar.name
        bucket.put_object(file_name, avatar)
        url=ali+file_name
        if userid!=None and username!=None and url!=None:
            userid=str(userid).replace("'","")
            username=str(username).replace("'","")
            param=(userid,pswd,username,url,takingcls)
            print(param)
            db0=cnx.cursor(dictionary=True)
            db0.execute("INSERT INTO note_users VALUES(%s,%s,%s,%s,%s)",param)
            cnx.commit()
    return HttpResponse(json.dumps([url],ensure_ascii=False))


def postnotes(request):
    cnx=connector.connect(host="127.0.0.1",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")

    if request.method=='POST':
        noteid=time.time();
        print(request.is_ajax())
        
        userid=request.POST.get('userid')
        noteclass=request.POST.get('noteclass')
        puttime=request.POST.get('puttime')
        clstime=request.POST.get('clstime')
        picnum=request.POST.get('picnum')
        if request.is_ajax():
            notepic=[]
            for i in range(int(picnum)):
                notepic.append(request.FILES['notepic'+str(i)])
        else:
            notepic=request.FILES.getlist('notepic')
        allfiles=''
        for note in notepic:  
            file_name =userid+note.name
            bucket.put_object(file_name, note)
            allfiles=allfiles+ali+file_name+','
        allfiles=allfiles[:-1]
        if len(notepic)>1:
            cover=allfiles[:allfiles.index(',')]
        else:
            cover=allfiles
        if userid!=None and picnum>0:
            userid=str(userid).replace("'","")
            noteclass=str(noteclass).replace("'","")
            puttime=str(puttime).replace("'","")
            param=(noteid,userid,cover,allfiles,noteclass,puttime,clstime,0,picnum)
            db0=cnx.cursor(dictionary=True)
            db0.execute(sql4,param)
            cnx.commit();

    return HttpResponse(json.dumps([],ensure_ascii=False))


def noteinfor(request,noteid):
    cnx=connector.connect(host="127.0.0.1",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")

    content=[]
    db0=cnx.cursor(dictionary=True)
    db0.execute(sql5%(noteid))
    for row in db0:
        # content.append(row)
        return HttpResponse(json.dumps(row,ensure_ascii=False))
# noteinfor(request,'1453165589.477143')

def oneclass(request,classname):
    cnx=connector.connect(host="127.0.0.1",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")
    data=[]
    db0=cnx.cursor(dictionary=True)
    db0.execute(sql7%(classname))
    for row in db0:
        data.append(row)
    for row in data:
        row['likepeople']=getlike(row['noteid'])
    return HttpResponse(json.dumps(data,ensure_ascii=False))

def like(request):
    cnx=connector.connect(host="127.0.0.1",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")
    if request.method=='POST':
        noteid=request.POST.get('noteid')
        netid=request.POST.get('netid')
        param=(noteid,netid)
        db0=cnx.cursor(dictionary=True)
        db0.execute(sql16%(noteid,netid))
        cnx.commit()
    return HttpResponse(json.dumps([],ensure_ascii=False))


def changeprofile(request,content):
    cnx=connector.connect(host="127.0.0.1",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")

    if request.method == 'POST':
        db0=cnx.cursor(dictionary=True)
        if content=='username':
            netid=request.POST.get('userid')
            nickname=request.POST.get('username')
            param=(nickname,netid)
            db0.execute(sql3,param)
        elif content=='avatar':
            netid=request.POST.get('userid')
            avatar=request.POST.get('avatar')
            param=(avatar,netid)
            db0.execute(sql6,param)

def login(request):
    cnx=connector.connect(host="127.0.0.1",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")

    data=[]
    if request.method == 'POST':
        netid=request.POST.get('netid')
        pswd=request.POST.get('pswd')
        db0=cnx.cursor(dictionary=True)
        db0.execute(sql9%(netid))
        yes={"a","b"}
        no={}
        for row in db0:
            if row['pswd']==pswd:
                
                print("yes")
                db0.execute(sql19%netid)
                for row in db0:
                    data.append(row)
                print(data)
                return HttpResponse(json.dumps(data,ensure_ascii=False))
            else:
        # data.sort(key=get,reverse=True)
                print("nos")
                return HttpResponse(json.dumps([1],ensure_ascii=False))
        return HttpResponse(json.dumps([1],ensure_ascii=False))

def collect(request):
    cnx=connector.connect(host="127.0.0.1",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")
    if request.method == 'POST':
         noteid=request.POST.get('noteid')
         netid=request.POST.get('netid')
         state=request.POST.get('state')
         print(netid)
         print(state)
         param=(noteid,netid)
         db0=cnx.cursor(dictionary=True)
         if int(state)==1:
             print('yes')
             db0.execute(sql10,param)
             cnx.commit();
         else:
             print('no')
             db0.execute(sql17%noteid)
             cnx.commit();
         return HttpResponse(json.dumps([0],ensure_ascii=False))

def getcollect(netid):
    collect=[]
    cnx=connector.connect(host="127.0.0.1",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")
    
    db1=cnx.cursor()
    db1.execute(sql11%netid)
    for row in db1:
        collect.append(row)
    return collect

def getcollectfrommobile(request,noteid):
    collect=[]
    cnx=connector.connect(host="127.0.0.1",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")
    db1=cnx.cursor()
    db1.execute(sql18%noteid)
    for row in db1:
        collect.append(row)
    return HttpResponse(collect)
    
def getcollectpeople(noteid):
    collect=[]
    cnx=connector.connect(host="47.88.102.126",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")
    db1=cnx.cursor()
    db1.execute(sql18%noteid)
    for row in db1:
        collect.append(row)
    return collect

def seecollect(request,netid):
    data=[]
    db0=cnx.cursor(buffered=True,dictionary=True)
    print(getcollect(netid))
    for item in getcollect(netid):
        db0.execute(sql12%(item))
        for row in db0:
            data.append(row)
    for row in data:
        row['likepeople']=getlike(row['noteid'])
    return HttpResponse(json.dumps(data,ensure_ascii=False))
        
def saveclass(request):
    cnx=connector.connect(host="127.0.0.1",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")
    if request.method == 'POST':
        netid=request.POST.get('netid')
        takingcls=request.POST.get('takingcls')
        db0=cnx.cursor(dictionary=True)
        db0.execute(sql13%(takingcls,netid))
        cnx.commit();
        return HttpResponse(json.dumps([],ensure_ascii=False))  
        
def getclass(request,netid):
    cnx=connector.connect(host="127.0.0.1",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")
    db0=cnx.cursor()
    db0.execute(sql14%(netid))
    print(sql14%(netid))
    for row in db0:
        return HttpResponse(row)

def history(request,netid):
    data=[]
    db0=cnx.cursor(buffered=True,dictionary=True)
    db0.execute(sql20%(netid))
    for row in db0:
        data.append(row)
    for row in data:
        row['likepeople']=getlike(row['noteid'])
    return HttpResponse(json.dumps(data,ensure_ascii=False))

def getallclasses(request):

    return HttpResponse(json.dumps(allclass,ensure_ascii=False))


#Website     
def home(request):
    return render_to_response('ex.html')
    

def aclass(request,classname):
    cnx=connector.connect(host="127.0.0.1",user="root",password="Arroyo@QXJ123",database="notemoment",charset="utf8")
    data=[]
    db0=cnx.cursor(dictionary=True)
    db0.execute(sql7%(classname))
    for row in db0:
        data.append(row)
    for row in data:
        row['notepic']=row['notepic'].split(',')
        row['likepeople']=getlike(row['noteid'])
        row['collectpeople']=getcollectpeople(row['noteid'])
    context={'querydata':data}
    return render_to_response('ex.html',context)

def weblogin(request):
    return render_to_response('login.html')

def upload(request):

    return render_to_response('upload.html')    
