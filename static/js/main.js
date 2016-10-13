

$(function () {

  var netid = $.cookie("username");
  var nickname = $.cookie("nickname");
  var avatar = $.cookie("avatar");
  var takingcls = $.cookie("takingcls");


  var globalnoteid="";

  if(takingcls!=undefined && takingcls!="null"){
      var classes=takingcls.split(',').slice(0,-1);
      $(".classbutton").text(classes[0]);
  }

  if(netid!=undefined && netid!="null") {
    $("#myDropdown").hide();
    $(".dropdown-content").height(240);
    $("#nickname").text(nickname);
    $("#avatar").attr("src",avatar);

    $("#classname").height(classes.length*50);

    $.each(classes, function( index, value ) {
          $("#classname").append("<div class='item'><h5 class='classes'>"+value+"</h5></div>");
      });
    $(".item").click(function() {
       window.location.replace("http://www.notemoment.tech/aclass/"+$(this).find(".classes").html());
});


    //var likepeople=$(".texthide").text();



    var names=[];
    $('.texthide').each(function(){
        var noteid=$(this).parent().find(".idhide").text();

        $(this).parent().parent().find(".fa-hand-o-left").click(function () {

        });


        var people= $(this).text();
        var peoplelist=people.substring(3,people.length-2).split("', u'");
        //alert(peoplelist)
        var collectpeople=$(this).parent().find(".collhide").text();
        var listcollectpeople=collectpeople.substring(4,collectpeople.length-4).split("',), (u'");
        $(this).parent().find("#heart").hover(function () {
                    //$(this).animate({ margin: -10, width: "+=20", height: "+=20" });
                    $(this).css("transform", "scale(1.1, 1.1)");
                    $(this).css('cursor', 'pointer');
                }, function () {
                    //$(this).animate({ margin: 0, width: "-=20", height: "-=20" });
                    $(this).css("transform", "none");
                    $(this).css('cursor', 'auto');
                });


         $(this).parent().find(".fa-money").hover(function(){
                //$(this).animate({ margin: -10, width: "+=20", height: "+=20" });
               $(this).css("transform", "scale(1.1, 1.1)");
                $(this).css('cursor','pointer');
            }, function(){
                 //$(this).animate({ margin: 0, width: "-=20", height: "-=20" });
               $(this).css("transform", "none");
                $(this).css('cursor','auto');
            });
        //$(this).parent().find(".md-content").find(".lower").find(".md-close").click(function() {
        //    alert(noteid);
        //});
        //$("#form1").submit(function( event ) {
        //    console.log(noteid)
        //    event.preventDefault();
        //});

        $(this).parent().find("#heart").click(function() {

                var noteid=$(this).parent().find(".idhide").text();
                var stat=0;
                 if($(this).attr("Class")=="fa fa-heart") {
                     stat=0;
                     $(this).removeClass('fa-heart').addClass('fa-heart-o').css('color', '#b8b9b4');
                     $(this).parent().find("#coltext").css('color', '#b8b9b4');
                     $(this).parent().css("transform", "none");
                     $(this).parent().off('mouseenter mouseleave');
                 }else if($(this).attr("Class")=="fa fa-heart-o"){
                     stat=1;
                     $(this).removeClass('fa-heart-o').addClass('fa-heart').css('color', '#000000');
                     $(this).parent().find("#coltext").css('color', '#000000');
                     $(this).parent().css("transform", "none");
                     $(this).parent().off('mouseenter mouseleave');

                 }
                     $.post("/collect/",
                         {
                             netid: netid,
                             noteid: noteid,
                             state: stat,
                             csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                         },
                         function (data, status) {
                             if (status == "success") {
                             }
                         }, "json");

                });


        if(collectpeople.length>=1) {

            if (jQuery.inArray(netid, listcollectpeople) < 0) {
                $(this).parent().find(".fa-heart").removeClass("fa-heart").addClass("fa-heart-o").css('color', '#b8b9b4');
                $(this).parent().find("#coltext").css('color', '#b8b9b4');


            }

        }
                 $(this).parent().find(".fa-thumbs-o-up").click(function() {
                  var noteid=$(this).parent().find(".hide").text();
                     alert(noteid);
                    $.post("/like/",
                  {
                    netid: netid,
                    noteid: noteid,
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                      },
                  function(data,status){
                      if(status=="success") {
                      }
                     },"json");
                  likenumber=likenumber+1;
                  $(this).removeClass('fa-thumbs-o-up').addClass('fa-thumbs-up').css('color', '#000000');
                  $(this).parent().find("#countr").css('color','#000000');
                  $(this).parent().css("transform", "none");
                  $(this).parent().off('mouseenter mouseleave');
                  $(this).parent().find("#countr").text(likenumber+" people liked this note");
                });

        if(people.length>=1){
          if(jQuery.inArray(netid,people.substring(3,people.length-2).split("', u'"))<0){
            //$(this).hide();
            $(this).parent().find(".fa-thumbs-up").removeClass('fa-thumbs-up').addClass('fa-thumbs-o-up').css('color', '#b8b9b4');
              $(this).parent().find("#countr").css('color', '#b8b9b4');
            $(this).parent().find(".fa-thumbs-o-up").hover(function(){
                //$(this).animate({ margin: -10, width: "+=20", height: "+=20" });
               $(this).css("transform", "scale(1.1, 1.1)");
                $(this).css('cursor','pointer');
            }, function(){
                 //$(this).animate({ margin: 0, width: "-=20", height: "-=20" });
               $(this).css("transform", "none");
                $(this).css('cursor','auto');
            });

            var likenumber=parseInt($(this).parent().find(".likehide").text());


              $(this).parent().find(".fa-thumbs-o-up").click(function() {
                  var noteid=$(this).parent().find(".hide").text();

                    $.post("/like/",
                  {
                    netid: netid,
                    noteid: noteid,
                    csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
                      },
                  function(data,status){
                      if(status=="success") {
                      }
                     },"json");
                  likenumber=likenumber+1;
                  $(this).removeClass('fa-thumbs-o-up').addClass('fa-thumbs-up').css('color', '#000000');
                  $(this).parent().find("#countr").css('color','#000000');
                  $(this).parent().css("transform", "none");
                  $(this).parent().off('mouseenter mouseleave');
                  $(this).parent().find("#countr").text(likenumber+" people liked this note");
                });
          }
        }

      });

  }else{
     $("#dialog").hide();
     $("#classdropdown").hide();
  }

  $( "#signout" ).click(function() {
       $.removeCookie('username', { path: '/' });
       $.removeCookie('username');
       location.reload();
});

    $("#form1").submit(function( event ) {
        var amount=0;
        if($(this).parent().find('#dotfive').is(':checked')) {
            amount=0.5;
            $(this).find("input[name='business']").val("2453152576@qq.com");
            $(this).find("input[name='amount']").val(amount);
        }else if($(this).parent().find('#one').is(':checked')){
            amount=1;
            $(this).find("input[name='business']").val("2453152576@qq.com");
            $(this).find("input[name='amount']").val(amount);
        }else if($(this).parent().find('#other').is(':checked')){
            amount=parseFloat($(this).parent().find(".moneyinput").val());
            $(this).find("input[name='business']").val("2453152576@qq.com");
            $(this).find("input[name='amount']").val(amount);
        }else{
            alert("Please make a choice!")
            event.preventDefault();
        }

        });


    $(".upload").click(function(){
        window.location.replace("http://notemoment.tech/upload/");
    })
  'use strict';

  var console = window.console || { log: function () {} };
  var $images = $('.docs-pictures');
  var $toggles = $('.docs-toggles');
  var $buttons = $('.docs-buttons');
  var options = {
        // inline: true,
        url: 'data-original',
        build: function (e) {
          console.log(e.type);
        },
        built: function (e) {
          console.log(e.type);
        },
        show: function (e) {
          console.log(e.type);
        },
        shown: function (e) {
          console.log(e.type);
        },
        hide: function (e) {
          console.log(e.type);
        },
        hidden: function (e) {
          console.log(e.type);
        },
        view: function (e) {
          console.log(e.type);
        },
        viewed: function (e) {
          console.log(e.type);
        }
      };

  function toggleButtons(mode) {
    if (/modal|inline|none/.test(mode)) {
      $buttons.
        find('button[data-enable]').
        prop('disabled', true).
          filter('[data-enable*="' + mode + '"]').
          prop('disabled', false);
    }
  }

  $images.on({
    'build.viewer': function (e) {
      console.log(e.type);
    },
    'built.viewer':  function (e) {
      console.log(e.type);
    },
    'show.viewer':  function (e) {
      console.log(e.type);
    },
    'shown.viewer':  function (e) {
      console.log(e.type);
    },
    'hide.viewer':  function (e) {
      console.log(e.type);
    },
    'hidden.viewer': function (e) {
      console.log(e.type);
    },
    'view.viewer':  function (e) {
      console.log(e.type);
    },
    'viewed.viewer': function (e) {
      console.log(e.type);
    }
  }).viewer(options);

  toggleButtons(options.inline ? 'inline' : 'modal');

  $toggles.on('change', 'input', function () {
    var $input = $(this);
    var name = $input.attr('name');

    options[name] = name === 'inline' ? $input.data('value') : $input.prop('checked');
    $images.viewer('destroy').viewer(options);
    toggleButtons(options.inline ? 'inline' : 'modal');
  });

  $buttons.on('click', 'button', function () {
    var data = $(this).data();
    var args = data.arguments || [];

    if (data.method) {
      if (data.target) {
        $images.viewer(data.method, $(data.target).val());
      } else {
        $images.viewer(data.method, args[0], args[1]);
      }

      switch (data.method) {
        case 'scaleX':
        case 'scaleY':
          args[0] = -args[0];
          break;

        case 'destroy':
          toggleButtons('none');
          break;
      }
    }
  });

});
