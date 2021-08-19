$(function () {
  $(".kb-container-loadedAjax").css({
    opacity: 1,
  });
  $(".kb-container-loading").hide();

  $("#output").text("000 Knowledge!");

  if (location.pathname.match(/home/)){
    $(".kb-sidebar ul li").eq(0).addClass('active');
  }
  if (location.pathname.match(/question/)){
    $(".kb-sidebar ul li").eq(1).addClass('active');
  }
  if (location.pathname.match(/manabu/)) {
    $(".kb-sidebar ul li").eq(2).addClass('active');
  }
  if (location.pathname.match(/target/)) {
    $(".kb-sidebar ul li").eq(3).addClass('active');
  }
  if (location.pathname.match(/news/)) {
    $(".kb-sidebar ul li").eq(4).addClass('active');
  }
});
