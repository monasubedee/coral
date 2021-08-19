"use strict";

$(function () {
  $('.news__item').modaal({
    before_open: function before_open(modal_wrapper) {// modalOpen();
    },
    before_close: function before_close(modal_wrapper) {// modalClose();
    }
  });
  $(document).on('click', '.modaal-close-clone', function () {
    $('.news__item').modaal('close');
    var listId = $('.modaal-content-container .news__modal--inner').attr('data-listId');
    $('.modaal-content-container .news__modal--inner').appendTo(listId);
  });
  $('.btn__pager__modal').on('click', function (event) {
    event.preventDefault();
    var target = $(this).attr('data-href');
    var listId = $('.modaal-content-container .news__modal--inner').attr('data-listId');
    $('.modaal-content-container .news__modal--inner').appendTo(listId);
    $('.modaal-close').remove();
    $(target).find('.news__modal--inner').appendTo('.modaal-content-container');
    $('.modaal-wrapper').attr('id', $(this).attr('data-modaal-scope'));
    $('.modaal-content-container').append('<span class="modaal-close-clone"></span>');
  });
});