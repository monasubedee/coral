$(function(){
  if ($('select.language').length) {
    $('select.language').append('<option value="0">選択無し</option>')
    for (var i = 1; i < countrys.length; i++) {
      $('select.language').each(function(){
        var selected = $(this).attr('data-selected') == (i) ? ' selected' : '';
        $(this).append('<option value="' + (i) + '"' + selected + '>' + countrys[i] + '</option>')
      });
    }
  }
});

var countrys = ["アブハジア語", "アファル語", "アフリカーンス語", "アルバニア語", "アムハラ語", "アラビア語", "アルメニア語", "アッサム語", "アイマラ語", "アゼルバイジャン語", "バシキール語", "バスク語", "ベンガル語", "ブータン語", "ビハール語", "ビスラマ語", "ブルターニュ語", "ブルガリア語", "ビルマ語", "白ロシア語 (ベラルーシ語)", "カンボジア語", "カタラン語", "中国語 (簡体)", "中国語 (繁体)", "コルシカ語", "クロアチア語", "チェコ語", "デンマーク語", "オランダ語", "英語", "エスペラント語", "エストニア語", "フェロー語", "ペルシャ語", "フィジー語", "フィンランド語", "フランス語", "フリジア語", "ガリシア語", "ゲール語 (スコットランド語)", "ゲール語 (マン島語)", "グルジア語", "ドイツ語", "ギリシャ語", "グリーンランド語", "グアラニー語", "グジャラート語", "ハウサ語", "ヘブライ語", "ヒンディー語", "ハンガリー語", "アイスランド語", "インドネシア語", "インターリンガ (国際語)", "インターリング語", "イヌクティトゥト語", "イヌピア語", "アイルランド語", "イタリア語", "日本語", "ジャワ語", "カンナダ語", "カシミール語", "カザフ語", "キヤーワンダ語 (ルアンダ語)", "キルギス語", "キルンディ語 (ルンディ語)", "韓国語", "クルド語", "ラオタ語", "ラテン語", "ラトビア語 (レット語)", "リンブルク語", "リンガラ語", "リトアニア語", "マケドニア語", "マダガスカル語", "マレー語", "マラヤーラム語", "マルタ語", "マオリ語", "マラーティー語", "モルドバ語", "モンゴル語", "ナウル語", "ネパール語", "ノルウェー語", "オック語", "オリヤー語", "オロモ語 (アファン語、ガラ語)", "パシト語 (パシュトー語)", "ポーランド語", "ポルトガル語", "パンジャブ語", "ケチュア語", "レートロマンス語", "ルーマニア語", "ロシア語", "サモア語", "サングホ語", "サンスクリット語", "セルビア語", "セルボクロアチア語", "セソト語", "セツワナ語", "ショナ語", "シンド語", "シンハラ語", "スワジ語", "スロバキア語", "スロベニア語", "ソマリ語", "スペイン語", "スンダ語", "スワヒリ語 (キスワヒリ語)", "スウェーデン語", "タガログ語", "タジク語", "タミル語", "タタール語", "テルグ語", "タイ語", "チベット語", "チグリニャ語", "トンガ語", "ツォンガ語", "トルコ語", "トルクメン語", "トウィ語", "ウイグル語", "ウクライナ語", "ウルドゥー語", "ウズベク語", "ベトナム語", "ヴォラピュック語", "ウェールズ語", "ウォロフ語", "コーサ語", "イディッシュ語", "ヨルバ語", "ズールー語"];
