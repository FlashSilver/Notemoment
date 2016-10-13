$( ".input" ).focusin(function() {
  $( this ).find( "span" ).animate({"opacity":"0"}, 200);
});

$( ".input" ).focusout(function() {
  $( this ).find( "span" ).animate({"opacity":"1"}, 300);
});

  $.ajaxSetup({"error":function(XMLHttpRequest,textStatus, errorThrown) {   
      alert(textStatus);
      alert(errorThrown);
      alert(XMLHttpRequest.responseText);
  }});

//$.cookie.defaults = { path: '/', expires: 365 };

//$(document).ready(function(){
$(".login").submit(function(e){
	e.preventDefault();
  //$(this).find(".submit i").removeAttr('class').addClass("fa fa-check").css({"color":"#fff"});
  //$(".submit").css({"background":"#2ecc71", "border-color":"#2ecc71"});
  $("input").css({"border-color":"#2ecc71"});
  var netid=$("#netid" ).val();
  var pswd=$("#pswd").val();
  $.post("/login/",
  {
	netid: netid,
	pswd: pswd,
	csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
	  },
  function(data,status){
  			if(data=="1"){
                 $(".feedback").show().animate({"opacity":"1", "bottom":"-80px"}, 400);
            }else{
                $.cookie("username", netid, {path:'/'});
                $.cookie("avatar", data[0].avatar, {path:'/'});
                $.cookie("nickname", data[0].nickname, {path:'/'});
                $.cookie("takingcls", data[0].takingcls, {path:'/'});
                window.location.href = "http://www.notemoment.tech/aclass/MATH2B";
            }
     },"json");
 return false;
});
//});
