$(document).ready(function () {
    function responsive() {
        let ww = $(window).innerWidth();
        let wh = $(window).innerHeight();
        let fh = $(".kb-footer").outerHeight();
        let hh = $(".kb-header").outerHeight();
        $(".kb-container-no-sb").css({
            "minHeight": wh - fh
        })
        $(".kb-container").css({
            "minHeight": wh - (fh + hh),
            "margin-top": hh,
            "padding": "20px",
            "width": ww - $(".kb-sidebar").outerWidth(),
            "marginLeft": $(".kb-sidebar").outerWidth(),
            "opacity": 1,
        })
        $(".kb-kb-container-no-sb").css({
            "minHeight": wh - (fh + hh),
            "margin-top": hh,
            "padding": "20px",
            "width": ww,
            "marginLeft": 0,
            "opacity": 1,
        })
        $(".kb-tameru-container").css({
            "height": wh - (fh + hh),
        })
        if ($('.kb-activity-media--wrap').length) {
            if (ww >= 992) {
                $('.kb-activity-media--wrap').height($('.kb-ranking').height());
            }
            else {
                $('.kb-activity-media--wrap').css('height','300px')
            }
        }
        if(ww>=992){
            if($(".kb-sidebar").css("display")=="none" || $(".kb-sidebar").css("display")==undefined){
                $(".kb-footer").find("p").css({
                    paddingLeft:0
                })
            }
            else{
                $(".kb-footer").find("p").css({
                    paddingLeft:$(".kb-sidebar").outerWidth()+10
                })
            }
        }
        else{
            $(".kb-footer").find("p").css({
                paddingLeft:0
            })
        }
        if(ww<=992){
            $(".kb-container").css({
                marginLeft:0,
                width:'100%'
            })
            $(".kb-sidebar").css({
                height: wh
            });
        }
        else{
            $(".kb-sidebar").css({
                height: wh - hh
            });
            $(".kb-container").css({
                marginLeft:$(".kb-sidebar").outerWidth(),
                width:ww-$(".kb-sidebar").outerWidth()
            })
        }

    }
    responsive();
    $(window).on("resize",function () {
        responsive();
        var ww=$(window).innerWidth();
        if(ww<=992){
            $(".kb-sidebar").hide();
            $(".overlap").remove();
        }
        else{
            $(".kb-sidebar").show();
        }
    })
    setInterval(responsive,10);
    var ud='';
    if(localStorage.getItem("ud")){
      ud=JSON.parse(localStorage.getItem("ud"));
    }
    else {
        ud=null;
    }
    if(ud!=null){
      var profile=ud.profile==''?'/static/ver2.1/img/1104@3x.png':ud.profile;
      $(".h-profile").find(".my-profile").css({
          "background-image":`url('${profile}')`,
      });
      $(".h-profile").find("p").text(ud.name);
      if(ud.authority==0){
        $(".kb-header").find(".dropdown-menu .bb").nextAll().addBack().hide();
      }
    }
    $.ajax({
        method:"Get",
        url:'/knowledge_count',
        success:function(data){
           // $("#output").text(JSON.parse(data).data+" Knowledge!");
            $("#output").text(JSON.parse(data).data);
            
        }
    })
    $(document).on("click",".logout",function(){
      localStorage.setItem("ud",'');
    })
    $(".kb-tabs-list>div").on("click", function () {
        var target = $(this).attr("data-target");
        $(target).siblings().removeClass('active');
        $(target).addClass('active');
        $(this).siblings().removeClass("active");
        $(this).removeClass("active").addClass("active");
    })
    $(".open-modal").on("click", function () {
        let id = $(this).attr("data-modal");
        $(id).show();
    })
    $(".modal-close").on("click", function () {
        $(this).closest(".modal").hide();
    })
    $(".mobile-sidebar-btn").on("click",function(){
       $("body").append("<div class='overlap'></div>");
       $(".overlap").css({
           "position":"fixed",
           "top":"0",
           "left":"0",
           "width":"100%",
           "z-index":'9998',
           "height":"100%",
           "background":"rgba(0,0,0,0.7)"
       })
       $(".kb-sidebar").show();
    })
    $(".sidebar-close").on("click",function(){
        $(".kb-sidebar").hide();
        $(".overlap").remove();
    })
    $(document).on("click",function(e){
        if(e.target.matches(".dropdown-btn,.dropdown-btn>*")){
            e.preventDefault();
            $(".dropdown-menu").toggle();
        }
        else{
            $(".dropdown-menu").hide();
        }
    })
    /* sidebar nav highlight */

    // textarea focus


})
