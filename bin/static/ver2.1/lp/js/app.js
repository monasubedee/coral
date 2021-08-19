"use strict";

// var current_scrollY;
// function modalOpen() {
//   current_scrollY = $(window).scrollTop();
//   $('body').attr('data-modalActive', 'true');
//   $('body').css({
//     position: 'fixed',
//     top: -1 * current_scrollY,
//     'z-index': 10
//   });
//   $('html').prop({ scrollTop: 0 });
// }
// function modalClose() {
//   $('.header__hamburger').removeClass('active');
//   $('.header__menu').fadeOut(400);
//   $('body').attr('data-modalActive', 'false');
//   $('body').css({
//     position: 'relative',
//     top: 'auto'
//   });
//   $('html').prop({ scrollTop: current_scrollY });
//   return;
// }
$(function () {
  $('a[href^="#"]').click(function () {
    if ($(window).width() < 768) {
      $('.header__hamburger').removeClass('active');
      $('.header__menu').fadeOut(400);
    }

    if (!$(this).hasClass('news__item')) {
      // var headerH = $('header').outerHeight() - 1;
      var speed = 500;
      var href = $(this).attr("href");
      var target = $(href == "#" || href == "" ? 'html' : href);
      var position = target.offset().top;
      $("html, body").animate({
        scrollTop: position
      }, speed, "swing");
      return false;
    }
  });
  var effect_pos = 100; // 画面下からどの位置でフェードさせるか(px)

  var effect_move = 50; // どのぐらい要素を動かすか(px)

  var effect_time = 400; // エフェクトの時間(ms) 1秒なら1000
  // フェードする前のcssを定義

  $(".fade-up").each(function () {
    $(this).css({
      opacity: 0,
      transform: "translateY(" + effect_move + "px)",
      transition: effect_time + "ms"
    });
  });
  $(window).on('scroll load', function () {
    var scroll_top = $(this).scrollTop();
    var scroll_btm = scroll_top + $(this).height();
    effect_pos = scroll_btm - effect_pos; // effect_posがthis_posを超えたとき、エフェクトが発動

    $('.fade-up').each(function () {
      var this_pos = $(this).offset().top - $(window).height() + $(window).height() / 5;

      if ($(window).scrollTop() > this_pos) {
        $(this).css({
          opacity: 1,
          transform: 'translateY(0)'
        });
      }
    });
  });
  $('.header__hamburger').on('click', function () {
    if (!$(this).hasClass('active')) {
      $(this).addClass('active');
      $('.header__menu').fadeIn(400); // modalOpen();
    } else {
      $(this).removeClass('active');
      $('.header__menu').fadeOut(400); // modalClose();
    }
  });
});