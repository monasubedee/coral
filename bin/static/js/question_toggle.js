$( function () {
  var QuestionToggle = ( function () {
    return function () {
      var self = this;

      self.init = function () {
        self.$questionWrapper = $( '.question-toggle__wrapper' );
        self.$btn = $( '.question-toggle__button' );

        self.isShow = self.$questionWrapper.attr( 'aria-hidden' ) === 'false';

        self.$btn.on( 'click', self._onButton );
      };

      self._onButton = function () {
        self.isShow ? self._closeQuestion() : self._showQuestion();
      };
      self._showQuestion = function () {
        self.$btn.attr( 'aria-expanded', 'true' );
        self.$questionWrapper.attr( 'aria-hidden', 'false' );
        self.isShow = true;
      };
      self._closeQuestion = function () {
        self.$btn.attr( 'aria-expanded', 'false' );
        self.$questionWrapper.attr( 'aria-hidden', 'true' );
        self.isShow = false;
      };

      self.init();
    };
  } )();
  if ( $( '.question-toggle' ).length ) var questionToggle = new QuestionToggle();
} );
