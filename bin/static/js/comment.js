$( function () {
  $( '#doComment' ).click( function () {
    if ( $( '#feed_comment' ).val() == '' ) {
      alert( 'フィードコメントを入力してください．' );
    } else {
      var textData = JSON.stringify( {
        questionId: $( '#questionId' ).val(),
        comment: $( '#feed_comment' ).val()
      } );
      $.ajax( '/api/comment', {
        type: 'POST',
        cache: false,
        data: textData,
        contentType: 'application/json',
        success: function () {
          $( '.feed__toast' )
            .html( 'フィードコメントコメントを送信しました' )
            .attr( 'aria-hidden', 'false' );
          $( '.feed__body' ).hide();
        },
        error: function () {
          $( '.feed__toast' )
            .html( 'フィードコメントが送信できませんでした．' )
            .attr( 'aria-hidden', 'false' );
        }
      } );
    }
  } );
} );
