$( function () {
  $( '.fav-button' ).on( 'click', function ( event ) {
    var $this = $( event.currentTarget );
    var isFaved = $this.attr( 'data-faved' ) === 'true';
    var userId = Number( $this.attr( 'data-userId' ) );
    var questionId = Number( $this.attr( 'data-questionId' ) );
    if ( isFaved ) {
      $.ajax( '/api/unfav', {
        type: 'POST',
        cache: false,
        data: JSON.stringify( {
          userId: userId,
          questionId: questionId
        } ),
        contentType: 'application/json',
        success: function () {
          $this.attr( 'data-faved', 'false' );
        },
        error: function () {
          alert( '通信に失敗しました' );
        }
      } );
    } else {
      $.ajax( '/api/fav', {
        type: 'POST',
        cache: false,
        data: JSON.stringify( {
          userId: userId,
          questionId: questionId
        } ),
        contentType: 'application/json',
        success: function () {
          $this.attr( 'data-faved', 'true' );
        },
        error: function () {
          alert( '通信に失敗しました' );
        }
      } );
    }
  } );
} );
