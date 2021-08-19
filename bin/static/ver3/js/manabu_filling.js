//const answer_str = "あアＡａ1"
const answer_str = $(".answer_box").attr("data-answer");
let input_str = "";
let currentNum = 1;

//数字
const strType_number = "0123456789";

//英字
const strType_alphabet_up =
  "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ";

const strType_alphabet_up_eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

const strType_alphabet_low =
  "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ";

const strType_alphabet_low_eng = "abcdefghijklmnopqrstuvwxyz";

//ひらがな
const strType_hiragana =
  "あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわゐうゑをんゔがぎぐげござじずぜぞだぢづでどばびぶべぼぱぴぷぺぽぁぃぅぇぉっゃゅょ";

//数字
const strType_katakana =
  "アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヰウヱヲンヴガギグゲゴザジズゼゾダヂヅデドバビブベボヷヸヹヺパピプペポァィゥェォッャュョ";

//回答をランダムに配置
function answerInput() {
  $(".answer_box").empty();
  answer_slice = answer_str.slice(currentNum - 1, currentNum);
  console.log("answer_slice = ", answer_slice)
  var random = Math.floor(Math.random() * 4 + 1);
  $(".answer_str" + random).text(answer_slice);
  strType();
  currentNum += 1;
}

function notice(target) {
  $('.kb-manabu-notice').css('right', 'calc(-100%)');
  $('.kb-manabu-notice-' + target).css('right', 'calc(0% + 5px)');
  noticeDlay = setTimeout(function () {
    $('.kb-manabu-notice-' + target).css('right', 'calc(-100%)');
  }, 3000);
}

function getComment(q_id) {
  $.ajax({
    method: "GET",
    url: `/manabu/getComment?id=${q_id}`,
    success: function (data) {
      var d = JSON.parse(data);
      $(".manabu-comment-media").remove();
      if (d.data === null) {

      }
      else {
        d.data.map((item, index) => {
          $('.comment-lists').addClass('mt-4').append(`<div class='flex flex-s py-3 manabu-comment-media'>
                 <div>
                   <p class='m-0 pr-3 text-muted'>${item.tsCreate.replace((/[/-]/g), ".")}</p>
                 </div>
                 <div>
                   <p class='m-0'>${item.comment.replace(/\r?\n/g, '<br>')}</p>
                 </div>
                 <div></div>
                 </div>`)
            if(item.flag===1){
              $(".comment-lists .manabu-comment-media").eq(index).find("div:last-child").append(`
                    <p class="fas fa-trash comment_delete deleteable my-0" data-id=${item.id} style="cursor:pointer"></p>
              `);
            }
        })
        if ($(".comment-lists>div").length > 4) {
          $('.comment-lists').css({ "height": "200px", "overflow": "auto" });
        }
        else {
          $('.comment-lists').css({ "height": "auto", "overflow": "auto" });
        }
      }
    }
  })
}

//誤答をランダムに配置
function strType() {
  //数字
  if (strType_number.indexOf(answer_slice) != -1) {
    $(".answer_box:empty").each(function(i, o) {
      $(this).text(
        strType_number[Math.floor(Math.random() * strType_number.length)]
      );
    });
    //アルファベット大文字
  } else if (strType_alphabet_up.indexOf(answer_slice) != -1 || strType_alphabet_up_eng.indexOf(answer_slice) != -1) {
    $(".answer_box:empty").each(function() {
      $(this).text(
        strType_alphabet_up[
          Math.floor(Math.random() * strType_alphabet_up.length)
        ]
      );
    });

    //アルファベット小文字
  } else if (strType_alphabet_low.indexOf(answer_slice) != -1 || strType_alphabet_low_eng.indexOf(answer_slice) != -1) {
    $(".answer_box:empty").each(function() {
      $(this).text(
        strType_alphabet_low[
          Math.floor(Math.random() * strType_alphabet_low.length)
        ]
      );
    });
    //ひらがな
  } else if (strType_hiragana.indexOf(answer_slice) != -1) {
    $(".answer_box:empty").each(function() {
      $(this).text(
        strType_hiragana[Math.floor(Math.random() * strType_hiragana.length)]
      );
    });
    //カタカナ
  } else if (strType_katakana.indexOf(answer_slice) != -1) {
    $(".answer_box:empty").each(function() {
      $(this).text(
        strType_katakana[Math.floor(Math.random() * strType_katakana.length)]
      );
    });
  }
}

//回答した文字列
$(".answer_box").on("click", function() {
  if ($(this).text() == answer_slice) {
    if (currentNum <= answer_str.length) {
      $(".input_str").append($(this).text());
      answerInput();
    } else {
      $(".input_str").append(answer_slice);
      alert("正解");

      var questionId = parseInt($(".answer_box").attr("data-que_id"));
      var questionType = parseInt($(".answer_box").attr("data-que_type"));
      var obj = {
        "userId": 1,
        "questionId": questionId,
        "answers": [answer_str],
        "questionType": questionType,
        "elapsedTime": 10
      }
      var qId = '';
      var xhr = new XMLHttpRequest();
      var url = "/manabu/result";
      xhr.open("POST", url, true);
      xhr.setRequestHeader("Content-Type", "application/json");
      xhr.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
          var json = JSON.parse(this.responseText);
          var q_id = json.data.questionId;
          qId = q_id;
          $(".kb-manabu-question").css({
            "position": "relative"
          })
          if (json.data.favState == true) {
            $(".favorite").attr({
              "src": '/static/img/like1.png',
              "data-value": true
            })
          }
          else {
            $(".favorite").attr({
              "src": '/static/img/like2.png',
              "data-value": false
            });
          }
          if (json.data.ratingState > 0) {
            for (var i = 0; i < json.data.ratingState; i++) {
              $(".rating img").eq(i).attr("src", '/static/img/star-on@3x.png');
            }
          }


          $(".manabu-break-btn-hide").hide();
          $(".manabu-solve-return").slideToggle();
          $('.choose-list button').attr('disabled', 'disabled');
          $('#explain_text').text(json.data.descriptionText);


          var index;
          var noticeDlay;
          $(".rating img").on("click", function () {
            index = $(".rating img").index($(this));
            notice('rating')
            var limit = $(".rating img").length;
            for (var i = 0; i < limit; i++) {
              if (i <= index) {
                $(".rating img").eq(i).attr("src", '/static/img/star-on@3x.png');
              }
              else {
                $(".rating img").eq(i).attr("src", '/static/img/star-off@3x.png');
              }
            }
            $.ajax({
              type: "POST",
              url: '/manabu/rate',
              headers: { "Content-Type": "application/json" },
              data: JSON.stringify({
                "userId": 0,
                "questionId": q_id,
                "rating": index + 1
              }),
              success: function (result) {
                console.log(result);
              }
            })
          });
          $(".favorite").on("click", function () {
            let status = '';
            if ($(this).attr("src") == '/static/img/like2.png') {
              $(this).attr("src", '/static/img/like1.png');
              $(this).attr("data-value", true);
              notice('favorite')
              status = "true";
            }
            else {
              $(this).attr("src", '/static/img/like2.png');
              $(this).attr("data-value", false);
              $('.kb-manabu-notice-favorite').css('right', 'calc(-100%)');
              clearTimeout(noticeDlay);
              status = "false";
            }
            $.ajax({
              type: "POST",
              url: '/manabu/favorite',
              headers: { "Content-Type": "application/json" },
              data: JSON.stringify({
                "userId": 0,
                "questionId": q_id,
                "fav": status
              }),
              success: function (result) {
                console.log(result);
              }
            })
          })

          getComment(q_id);

          var ques_comments = [];

          $(".submit-manabu").on("click", function (e) {
            e.preventDefault();
            window.location.href = "/manabu/solve";
          });

          $(document).on("click", "#comment", function (e) {
            e.preventDefault();

            var date = new Date();
            var month = (date.getMonth() + 1) >= 10 ? (date.getMonth() + 1) : '0' + (date.getMonth() + 1);
            var day = date.getDate() >= 10 ? date.getDate() : '0' + date.getDate();
            var custom_format = `${date.getFullYear()}年${month}月${day}日`;
            let q_comment = $('.ques_comment').val().replace(/\r?\n/g, '<br>');


            var comment = input_varidate('.ques_comment', {
              required: true,
              maxLength: 1000,
              message: 'コメント'
            });
            if (comment == true) {
              input_errorElement('.ques_comment', '', '.ques_comment-wrap');
              notice('comment')
              $(".comment-error").hide();
              ques_comments.push($('.ques_comment').val())
              $('.ques_comment').val('');
            } else {
              input_errorElement('.ques_comment', comment, '.ques_comment-wrap');
              $(".comment-error").show();
            }
            if (q_comment.trim() !== "") {
              $.ajax({
                type: "POST",
                url: '/manabu/comment',
                headers: { "Content-Type": "application/json" },
                data: JSON.stringify({
                  "userId": 0,
                  "questionId": qId,
                  "comment": q_comment
                }),
                success: function (result) {
                  getComment(questionId)
                }
              })
            }
          });
        }3
      };
      xhr.send(JSON.stringify(obj));
      $(document).on('click', '#delete-comment', function (e) {
        let id = $(this).attr("data-delete");
        $.ajax({
          method: "DELETE",
          url: '/manabu/comment',
          headers: { "Content-Type": "application/json" },
          data: JSON.stringify({
            "id": id
          }),
          success: function (data) {
            console.log(qId);
            if (JSON.parse(data).result.result === "ok") {
              getComment(qId)
              $("#attention").hide();
              notice("comment-delete");
            }
          }
        });
        });
    }
  } else {
    alert("不正解");
  }
});

answerInput();
