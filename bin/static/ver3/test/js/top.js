$(function () {
  $(".profile-data").append('\
    <div class="flex flex-s p-3">\
      <div class="">\
          <div class="profile-img profile mb-2" style="background-image:url(/static/ver2.1/img/1104@3x.png);background-size:cover;background-position:center;">\
            </div>\
      </div>\
      <div class="">\
          <div>\
              <div>\
              <h4 class="m-0">明日花 キララ</h4>\
              <p class="text-muted my-2"><i class="far fa-envelope mr-2"></i>asukakirara@gmail.com</p>\
              </div>\
          </div>\
          <div class="flex flex-s py-2 profile-data-info">\
              <div>\
                  <small class="text-muted">チーム</small>\
                  <p class="my-1 line-height-1">ディレクター</p>\
              </div>\
              <div class="px-5">\
                  <small class="text-muted">役職</small>\
                  <p class="my-1 line-height-1">社員</p>\
              </div>\
              <div>\
                  <small class="text-muted">入社日</small>\
                  <p class="my-1 line-height-1">1993/11/17</p>\
              </div>\
          </div>\
      </div>\
    </div>\
    <div class="flex flex-c py-3 bb">\
        <div class="text-center pr-4">\
            <small class="text-muted">まなんだ数</small>\
            <h1 class="font-normal my-1">22</h1>\
        </div>\
        <div class="text-center px-4 bl br">\
            <small class="text-muted">ためた数</small>\
            <h1 class="font-normal my-1">10</h1>\
        </div>\
        <div class="text-center pl-4">\
            <small class="text-muted">合計まなび日数</small>\
            <h1 class="my-1 font-normal">610</h1>\
        </div>\
    </div>\
  '
  );
  $(".manabu-tameru-progress").append(
    '\
    <div class="py-3">\
      <div class="pl-3">\
        <div class="flex flex-sb">\
            <span class="text-muted">\
                <small class="dot dot-blue">毎週 10問まなぶ</small>\
            </span>\
            <span class="text-muted">\
                <small>期限：2020年08月17日まで</small>\
            </span>\
        </div>\
        <div class="py-3">\
            <div class="progress-bar">\
                <div class="progress-bar-status bg-blue" data-value="0" style="background: red; width: 0%;"></div>\
            </div>\
        </div>\
        <div class="flex flex-sb">\
            <span class="text-muted">\
                <small>達成率：0%</small>\
            </span>\
            <span class="text-muted">\
                <small>3人中 0人がクリア</small>\
            </span>\
        </div>\
      </div>\
    </div>\
    <div class="py-3">\
      <div class="pl-3">\
        <div class="flex flex-sb">\
          <span class="text-muted">\
              <small class="dot dot-red">毎月 10問ためる</small>\
          </span>\
          <span class="text-muted">\
              <small>期限：2020年08月31日まで</small>\
          </span>\
        </div>\
        <div class="py-3">\
            <div class="progress-bar">\
                <div class="progress-bar-status bg-red" data-value="0" style="width: 0%;"></div>\
            </div>\
        </div>\
        <div class="flex flex-sb">\
            <span class="text-muted">\
                <small>達成率：0%</small>\
            </span>\
            <span class="text-muted">\
                <small>3人中 0人がクリア</small>\
            </span>\
        </div>\
      </div>\
    </div>\
    <div class="py-3">\
      <div class="pl-3">\
        <div class="flex flex-sb">\
          <span class="text-muted">\
              <small class="dot dot-red">毎月 10問ためる</small>\
          </span>\
          <span class="text-muted">\
              <small>期限：2020年08月31日まで</small>\
          </span>\
        </div>\
        <div class="py-3">\
            <div class="progress-bar">\
                <div class="progress-bar-status bg-red" data-value="0" style="width: 0%;"></div>\
            </div>\
        </div>\
        <div class="flex flex-sb">\
            <span class="text-muted">\
                <small>達成率：0%</small>\
            </span>\
            <span class="text-muted">\
                <small>3人中 0人がクリア</small>\
            </span>\
        </div>\
      </div>\
    </div>\
  '
  );
})
