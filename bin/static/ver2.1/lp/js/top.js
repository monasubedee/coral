"use strict";

$(function () {
  $('[data-balloon]').each(function () {
    var comment = $(this).attr('data-balloon');
    $(this).append("\n      <div class=\"balloon\">".concat(comment, "</div>\n    "));
  }); // var transition = 200;
  // $('[data-balloon] img').on({
  //   'mouseenter': function () {
  //     if ($(this).hasClass("reverce")) {
  //       if ($(window).width() >= 768) {
  //         $(this)
  //           .next(".balloon")
  //           .fadeIn(transition)
  //           .animate(
  //             {
  //               top: "85%",
  //               bottom: "auto"
  //             },
  //             {
  //               duration: transition,
  //               queue: false
  //             }
  //           );
  //       } else{
  //         console.log('here')
  //         $(this)
  //           .next(".balloon")
  //           .css({
  //             bottom: "auto"
  //           })
  //           .fadeIn(transition)
  //           .animate(
  //             {
  //               top: "95%"
  //             },
  //             {
  //               duration: transition,
  //               queue: false
  //             }
  //           );
  //       }
  //     } else {
  //       $(this)
  //         .next(".balloon")
  //         .css({
  //           top: "auto"
  //         })
  //         .fadeIn(transition)
  //         .animate(
  //           {
  //             bottom: "95%",
  //           },
  //           {
  //             duration: transition,
  //             queue: false
  //           }
  //         );
  //     }
  //   },
  //   'mouseleave': function () {
  //     if ($(this).hasClass("reverce")) {
  //       if ( $(window).width() >= 768) {
  //         $(this)
  //           .next(".balloon")
  //           .css({
  //             bottom: "auto"
  //           })
  //           .fadeOut(transition)
  //           .animate(
  //             {
  //               top: "60%",
  //             },
  //             {
  //               duration: transition,
  //               queue: false
  //             }
  //           );
  //       } else {
  //         $(this)
  //           .next(".balloon")
  //           .css({
  //             bottom: "auto"
  //           })
  //           .fadeOut(transition)
  //           .animate(
  //             {
  //               top: "80%",
  //             },
  //             {
  //               duration: transition,
  //               queue: false
  //             }
  //           );
  //       }
  //     }else{
  //       $(this)
  //         .next(".balloon")
  //         .css({
  //           top: "auto"
  //         })
  //         .fadeOut(transition)
  //         .animate(
  //           {
  //             bottom: "80%",
  //             top: "auto"
  //           },
  //           {
  //             duration: transition,
  //             queue: false
  //           }
  //         );
  //     }
  //   }
  // });

  var effect_pos = 0; // 画面下からどの位置でフェードさせるか(px)
  // フェードする前のcssを定義

  $(window).on('scroll load', function () {
    var scroll_top = $(this).scrollTop();
    var scroll_btm = scroll_top + $(this).height();
    effect_pos = scroll_btm - effect_pos; // effect_posがthis_posを超えたとき、エフェクトが発動
    // console.log('scroll_top:' + scroll_top);
    // console.log('effect_pos:'+effect_pos);

    $('[data-balloon]').each(function () {
      var this_pos = $(this).offset().top - 200; // console.log('this_pos:' + this_pos);

      if ($(window).scrollTop() > this_pos) {
        $(this).addClass('reverce');
      } else {
        $(this).removeClass('reverce');
      }
    });
  });
  $('.problem__target').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    asNavFor: '.problem__toggle',
    responsive: [{
      breakpoint: 768,
      settings: {
        dots: true,
        dotsClass: 'slide-dots'
      }
    }]
  });
  $('.problem__toggle').slick({
    slidesToShow: 3,
    slidesToScroll: 1,
    asNavFor: '.problem__target',
    focusOnSelect: true,
    arrows: false,
    responsive: [{
      breakpoint: 768,
      settings: {
        arrows: true,
        slidesToShow: 1
      }
    }]
  });
  $(".problem__target__item").matchHeight();
});