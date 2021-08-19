$(document).ready(function(){
    $(".add-tab-btn").on("click",function(){
        var title=$(this).parent().find("input").val();
        var list_box=$(this).parent().next(".result-tabs-list");
        if(title.trim()!=""){
            list_box.append("<span>"+title+"<i>x</i></span>");
        }
    })
    $(".submit-setting-base-btn").on("click",function(){
        p = document.getElementsByName('occupation')
        var occupation = []
        for (i=0; i<p.length; i++) {
        if (p[i].checked==true)	{
            occupation.push(p[i].value)
        }
        }
    })
})