window.onpageshow = function ( event ) {
  if ( event.persisted ) {
    window.location.reload();
  }
};
$( function () {
  var Challenge = ( function ( dateFns ) {
    return function () {
      var self = this;
      var ANIMATION_START = 'animationstart';

      self.init = function () {
        self.startTime = new Date();
        self.$form = $( 'form' );
        self.$timelimit = $( '.timelimit' );
        self.$timelimitProgressFill = $( '.timelimit__progress-fill' );
        self.$timelimitText = $( '.timelimit__time' );
        self.limitTime = 120;
        self.$answerInput = $( '[name="answerId"]' );

        self.timerId = setInterval( self.displayTime, 1000 );
        self.$timelimitProgressFill.attr( 'aria-busy', 'true' );
        self.$timelimit.on( 'reachTimeLimit', self.stopTimer );
        self.$form.on( 'submit', self._onSubmit );
      };

      self.stopTimer = function () {
        clearInterval( self.timerId );
        self.$answerInput.prop( 'checked', false );
        $( '<input />' )
          .attr( 'type', 'hidden' )
          .attr( 'name', 'answerId' )
          .attr( 'value', 999999 )
          .prop( 'checked', true )
          .appendTo( self.$form );
        self.$form.trigger( 'submit' );
      };

      self.displayTime = function () {
        self.limitTime--;
        self.$timelimitText.html(
          Math.floor( self.limitTime / 60 ) +
            ':' +
            ( '00' + ( self.limitTime % 60 ) ).slice( -2 )
        );
        if ( self.limitTime === 0 ) self.$timelimit.trigger( 'reachTimeLimit' );
      };

      self._onSubmit = function ( event ) {
        $( '<input />' )
          .attr( 'type', 'hidden' )
          .attr( 'name', 'elapsedTime' )
          .attr(
            'value',
            dateFns.differenceInMilliseconds( new Date(), self.startTime )
          )
          .appendTo( $( event.currentTarget ) );
      };

      self.init();
    };
  } )( dateFns );
  if ( $( '.timelimit' ).length ) var challenge = new Challenge();
} );
