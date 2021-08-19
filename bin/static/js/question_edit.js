$( function () {
  var Create = ( function () {
    return function () {
      var self = this;
      var QUESTION_TYPE = { SELECT_ONE: '1', SELECT_ALL: '2', YES_NO: '3' };
      var INITIAL_INPUT_STATE = [
        {
          label: '',
          correctFlag: 'True'
        },
        {
          label: '',
          correctFlag: 'False'
        },
        {
          label: '',
          correctFlag: 'False'
        },
        {
          label: '',
          correctFlag: 'False'
        }
      ];

      var INITIAL_YES_NO_INPUT_STATE = [
        {
          label: 'YES',
          correctFlag: 'True'
        },
        {
          label: 'NO',
          correctFlag: 'False'
        }
      ];

      self.init = function () {
        self.$create = $( '.create' );
        self.$backButton = $( '.navigation-button' );
        self.$questionType = $( '[name="questionType"]' );
        self.$answerInputList = $( '.create__answer__input-list' );
        self.$answerInputYesNo = $( '.create__answer__yes-no' );
        self.$modal = $( '.modal' );
        self.$modalYes = $( '.modal__button--yes' );
        self.$modalNo = $( '.modal__button--no' );
        self.$buttonSubmit = $( '.create__submit' );
        self.$buttonPreview = $( '.create__submenu__button--preview' );
        self.$buttonDraftSubmit = $( '.create__submenu__button--draft' );
        self.$buttonAddTopic = $( '.create__description__topic__button' );
        self.$buttonAddTopic = $( '.create__description__topic__button' );
        self.$buttonImageSelect = $( '.create__select-image' );
        self.$filePicture = $( '.create__picture-file' );
        self.$preview = $( '.preview' );
        self.$previewClose = $( '.create__submenu__button--edit' );

        self.currentQuestionType = self.$questionType.val();

        self.questionPicture = '';
        self.descriptionPicture = '';

        self.$questionType.on( 'change', self._onChangeQuestionType );
        self.$create.on( 'acceptChangeQuestionType', self._changeInputInterface );
        self._registerDynamicDomEventHandler();
        self.$buttonSubmit.on( 'click', self.submit );
        self.$buttonPreview.on( 'click', self.showPreview );
        $( '.preview__header__close' ).on( 'click', self.closePreview );
        self.$buttonDraftSubmit.on( 'click', self.submitDraft );
        self.$buttonAddTopic.on( 'click', self._addTopicLabel );
        self.$buttonImageSelect.on( 'click', self._onClickSelectImage );
        self.$filePicture.on( 'change', self._onChangeFile );
        self.$previewClose.on( 'click', self.closePreview );
        $( '.create__description__topic-remove' ).on( 'click', self.deleteTopic );
        self._initInputInterface( self.currentQuestionType );
      };

      self._registerDynamicDomEventHandler = function () {
        $( '.create__answer__delete' ).on(
          'click',
          self._onClickCreateAnswerDelete
        );
      };

      self._onClickSelectImage = function ( event ) {
        var $this = $( event.currentTarget );
        if ( $this.attr( 'data-name' ) === 'questionPicture' )
          $( '#questionPictureFile' ).trigger( 'click' );
        if ( $this.attr( 'data-name' ) === 'descriptionPicture' )
          $( '#descriptionPictureFile' ).trigger( 'click' );
      };

      self._onChangeFile = function ( event ) {
        var $this = $( event.currentTarget );
        const fr = new FileReader();
        var file = event.target.files[ 0 ];

        if ( file && file.type.match( 'image.*' ) ) {
          fr.readAsDataURL( file );
        }

        fr.onload = function ( _this ) {
          if ( $this.attr( 'name' ) === 'questionPicture' )
            self.questionPicture = _this.currentTarget.result;
          if ( $this.attr( 'name' ) === 'descriptionPicture' )
            self.descriptionPicture = _this.currentTarget.result;
        };
      };

      self._getValidationQuestionReasons = function () {
        var errorArray = [];
        if ( $( '[name="categoryId"]' ).val() === '0' )
          errorArray.push( { name: 'categoryId', reason: 'required' } );
        if ( $( '[name="sub_categoryId"]' ).val() === '0' )
          errorArray.push( { name: 'sub_categoryId', reason: 'required' } );
        if ( $( '[name="questionText"]' ).val() === '' )
          errorArray.push( { name: 'questionText', reason: 'required' } );
        return errorArray;
      };

      self._getValidationAnswerReasons = function () {
        var errorArray = [];
        if (
          self.currentQuestionType !== QUESTION_TYPE.YES_NO &&
          $.makeArray( $( '.create__answer__input' ) ).every( function ( element ) {
            return !element.value;
          } )
        )
          errorArray.push( {
            state: 'answer',
            name: 'answer.label',
            reason: 'required',
            type: 'placeholder'
          } );

        if (
          self.currentQuestionType !== QUESTION_TYPE.YES_NO &&
          $.makeArray( $( '.create__answer__correct__input' ) ).every( function (
            value
          ) {
            return !value.checked;
          } )
        )
          errorArray.push( {
            state: 'answer',
            reason: 'atLeast',
            name: 'answer.correctFlag'
          } );

        return errorArray;
      };

      self._getValidationDescriptionReasons = function () {
        var errorArray = [];
        if ( $( '[name="descriptionText"]' ).val() === '' )
          errorArray.push( { name: 'descriptionText', reason: 'required' } );

        return errorArray;
      };

      self._showValidate = function ( errorReasons ) {
        if ( !errorReasons ) return undefined;

        errorReasons.forEach( function ( reason ) {
          if ( !reason.state ) {
            $(
              '[data-name=' +
                reason.name +
                '][data-reason=' +
                reason.reason +
                ']'
            ).attr( 'aria-hidden', 'false' );
          }

          if ( reason.type === 'placeholder' ) {
            $( '.create__answer__input' ).each( function ( index, element ) {
              var $input = $( element );
              if ( !$input.val() )
                $input.attr( {
                  'aria-invalid': 'true',
                  placeholder: '入力されていません'
                } );
            } );
          }
          if ( reason.reason === 'atLeast' ) {
            $( '[data-name="answer.correctFlag"][data-reason="atLeast"]' ).attr(
              'aria-hidden',
              'false'
            );
          }
        } );
        return errorReasons;
      };

      self._onClickCreateAnswerDelete = function ( event ) {
        if ( $( '.create__answer__input-wrapper' ).length <= 2 ) return;
        var $this = $( event.currentTarget );
        var $parent = $this.parents( '.create__answer__input-wrapper' );
        $parent.remove();
        $( '.create__answer__input-wrapper' ).each( function ( index, element ) {
          var $this = $( element );
          $this
            .find( '.create__answer__alphabet-label' )
            .text( String.fromCharCode( index + 65 ) );
          $this
            .find( 'create__answer__input' )
            .attr( 'name', 'answer[' + index + '].label' );
        } );
      };

      self._onChangeQuestionType = function ( event ) {
        var $this = $( event.currentTarget );
        if ( self._shouldRenderModal( self.currentQuestionType ) ) {
          self._showModal().then(
            function () {
              self.currentQuestionType = $this.val();
              self.$create.trigger( 'acceptChangeQuestionType', [
                self.currentQuestionType
              ] );
              return;
            },
            function () {
              $this.val( self.currentQuestionType );
              return;
            }
          );
          return;
        }
        self.currentQuestionType = $this.val();
        self.$create.trigger( 'acceptChangeQuestionType', [
          self.currentQuestionType
        ] );
      };

      self._shouldRenderModal = function ( questionType ) {
        var $answerLabels = $( '.create__answer__input' );
        var $correctInput = $( '.create__answer__correct__input' );
        if ( questionType === QUESTION_TYPE.YES_NO ) return false;

        if (
          $answerLabels.length !== 4 ||
          $.makeArray(
            $answerLabels.map( function ( index, element ) {
              return $( element ).val();
            } )
          ).some( function ( val ) {
            return val === '';
          } )
        )
          return true;
        if (
          ( questionType === QUESTION_TYPE.SELECT_ONE ) |
          ( questionType === QUESTION_TYPE.SELECT_ALL )
        ) {
          var isInitialValueOfCorrectInput = $.makeArray(
            $correctInput.map( function ( index, element ) {
              return index === 0 ?
                !$( element ).prop( 'checked' ) :
                $( element ).prop( 'checked' );
            } )
          ).some( function ( val ) {
            return val;
          } );
          if ( isInitialValueOfCorrectInput ) return true;
        }
      };

      self._showModal = function () {
        self.$modal.attr( 'aria-hidden', 'false' );
        return new Promise( function ( resolve, reject ) {
          self.$modalYes.on( 'click', function () {
            resolve();
            self.$modal.attr( 'aria-hidden', 'true' );
          } );
          self.$modalNo.on( 'click', function () {
            reject();
            self.$modal.attr( 'aria-hidden', 'true' );
          } );
        } );
      };

      self.initUserInterfaceAnswer = function ( questionType ) {
        if ( questionType === QUESTION_TYPE.SELECT_ONE ) {
          self.$answerInputYesNo.attr( 'aria-hidden', 'true' );
          self.$answerInputList.attr( 'aria-hidden', 'false' );
          $( '.create__answer__correct__input' ).on(
            'change',
            self._selectOnlyOneCorrectFlag
          );
          self._registerDynamicDomEventHandler();
        }
        if ( questionType === QUESTION_TYPE.SELECT_ALL ) {
          self.$answerInputYesNo.attr( 'aria-hidden', 'true' );
          self.$answerInputList.attr( 'aria-hidden', 'false' );

          $( '.create__answer__correct__input' ).off(
            'change',
            self._selectOnlyOneCorrectFlag
          );
          self._registerDynamicDomEventHandler();
        }
        if ( questionType === QUESTION_TYPE.YES_NO ) {
          $( '.create__answer__correct__input' ).off(
            'change',
            self._selectOnlyOneCorrectFlag
          );
          self.$answerInputList.attr( 'aria-hidden', 'true' );
          self.$answerInputYesNo.attr( 'aria-hidden', 'false' );
          self._registerDynamicDomEventHandler();
        }
      };

      self._initInputInterface = function ( questionType ) {
        if ( questionType === QUESTION_TYPE.SELECT_ONE ) {
          self.$answerInputYesNo.attr( 'aria-hidden', 'true' );
          self.$answerInputList.attr( 'aria-hidden', 'false' );
          $( '.create__answer__correct__input' ).on(
            'change',
            self._selectOnlyOneCorrectFlag
          );
          self._registerDynamicDomEventHandler();
        }
        if ( questionType === QUESTION_TYPE.SELECT_ALL ) {
          self.$answerInputYesNo.attr( 'aria-hidden', 'true' );
          self.$answerInputList.attr( 'aria-hidden', 'false' );

          $( '.create__answer__correct__input' ).off(
            'change',
            self._selectOnlyOneCorrectFlag
          );
          self._registerDynamicDomEventHandler();
        }
        if ( questionType === QUESTION_TYPE.YES_NO ) {
          $( '.create__answer__correct__input' ).off(
            'change',
            self._selectOnlyOneCorrectFlag
          );
          self.$answerInputList.attr( 'aria-hidden', 'true' );
          self.$answerInputYesNo.attr( 'aria-hidden', 'false' );
          self._registerDynamicDomEventHandler();
        }
      };

      self._changeInputInterface = function ( event, questionType ) {
        if ( questionType === QUESTION_TYPE.SELECT_ONE ) {
          self._initilizeInputInterface( QUESTION_TYPE.SELECT_ONE );
          self.$answerInputYesNo.attr( 'aria-hidden', 'true' );
          self.$answerInputList.attr( 'aria-hidden', 'false' );
          $( '.create__answer__correct__input' ).on(
            'change',
            self._selectOnlyOneCorrectFlag
          );
          self._registerDynamicDomEventHandler();
        }
        if ( questionType === QUESTION_TYPE.SELECT_ALL ) {
          self._initilizeInputInterface( QUESTION_TYPE.SELECT_ALL );
          self.$answerInputYesNo.attr( 'aria-hidden', 'true' );
          self.$answerInputList.attr( 'aria-hidden', 'false' );

          $( '.create__answer__correct__input' ).off(
            'change',
            self._selectOnlyOneCorrectFlag
          );
          self._registerDynamicDomEventHandler();
        }
        if ( questionType === QUESTION_TYPE.YES_NO ) {
          $( '.create__answer__correct__input' ).off(
            'change',
            self._selectOnlyOneCorrectFlag
          );
          self._initilizeInputInterface( QUESTION_TYPE.YES_NO );
          self.$answerInputList.attr( 'aria-hidden', 'true' );
          self.$answerInputYesNo.attr( 'aria-hidden', 'false' );
          self._registerDynamicDomEventHandler();
        }
      };

      self._initilizeInputInterface = function ( questionType ) {
        if ( questionType === QUESTION_TYPE.SELECT_ONE ) {
          var $child = self.$answerInputList
            .find( '.create__answer__input-wrapper:eq(0)' )
            .clone( true );
          self.$answerInputList.empty().append(
            INITIAL_INPUT_STATE.map( function ( element, index ) {
              var $newElement = $child.clone();
              $newElement
                .find( '.create__answer__alphabet-label' )
                .text( String.fromCharCode( index + 65 ) );
              $newElement
                .find( '.create__answer__input' )
                .attr( 'name', 'answer[' + index + '].label' )
                .val( '' );
              index === 0 ?
                $newElement
                  .find( '.create__answer__correct__input' )
                  .attr( 'name', 'answer[' + index + '].correctFlag' )
                  .prop( 'checked', true ) :
                $newElement
                  .find( '.create__answer__correct__input' )
                  .attr( 'name', 'answer[' + index + '].correctFlag' )
                  .prop( 'checked', false );
              return $newElement;
            } )
          );
        }
        if ( questionType === QUESTION_TYPE.SELECT_ALL ) {
          var $child = self.$answerInputList
            .find( '.create__answer__input-wrapper:eq(0)' )
            .clone( true );
          self.$answerInputList.empty().append(
            INITIAL_INPUT_STATE.map( function ( element, index ) {
              var $newElement = $child.clone();
              $newElement
                .find( '.create__answer__alphabet-label' )
                .text( String.fromCharCode( index + 65 ) );
              $newElement
                .find( '.create__answer__input' )
                .attr( 'name', 'answer[' + index + '].label' )
                .val( '' );
              index === 0 ?
                $newElement
                  .find( '.create__answer__correct__input' )
                  .attr( 'name', 'answer[' + index + '].correctFlag' )
                  .prop( 'checked', true ) :
                $newElement
                  .find( '.create__answer__correct__input' )
                  .attr( 'name', 'answer[' + index + '].correctFlag' )
                  .prop( 'checked', false );
              return $newElement;
            } )
          );
        }
        if ( questionType === QUESTION_TYPE.YES_NO ) {
          $( 'create__answer__yes-no__input-text' ).each( function (
            index,
            element
          ) {
            index === 0 ?
              $( element ).propp( 'checked', true ) :
              $( element ).propp( 'checked', false );
          } );
        }
      };

      self._selectOnlyOneCorrectFlag = function ( event ) {
        var $this = $( event.currentTarget );
        $( '.create__answer__correct__input' ).each( function ( index, element ) {
          var $input = $( element );
          $input.is( $this ) ?
            $input.prop( 'checked', true ) :
            $input.prop( 'checked', false );
        } );
      };

      self._showTopicLabels = function () {
        $( '[name="topicLabels[]"]' ).length &&
          $( '.create__description__topic-list' ).attr( 'aria-hidden', 'false' );
      };

      self._addTopicLabel = function () {
        var value = $( '[name="topic"]' ).val();
        if ( !value ) return;

        $( '[name="topic"]' ).val( '' );
        var deleteButton = $(
          '<button type="button" class="create__description__topic-remove"></button>'
        );
        var input = $( '<input type="hidden"name="topicLabels[]">' ).val( value );
        var item = $( '<li class="create__description__topic-item"></li>' )
          .append( value )
          .append( deleteButton )
          .append( input );
        deleteButton.on( 'click', self.deleteTopic );
        $( '.create__description__topic-list' ).append( item );
        self._showTopicLabels();
      };

      self.deleteTopic = function ( event ) {
        var $this = $( event.currentTarget );
        $this.parent().remove();
        if ( !$( '.create__description__topic-item' ).length )
          $( '.create__description__topic-list' ).attr( 'aria-hidden', 'true' );
      };

      self.submit = function () {
        console.log( self._createSendData( self.currentQuestionType, 'False' ) );
        var errors = self
          ._getValidationQuestionReasons()
          .concat( self._getValidationAnswerReasons() )
          .concat( self._getValidationDescriptionReasons() );
        if ( errors.length ) {
          self._showValidate( errors );
          return;
        }

        $.ajax( '/api/question/edit', {
          cache: false,
          type: 'POST',
          data: self._createSendData( self.currentQuestionType, 'False' ),
          dataType: 'json',
          success: function () {
            location.href = '/question/edit/complete';
          },
          error: function () {
            alert( '失敗1111' );
          }
        } );
      };

      self._createSendData = function ( questionType, draft ) {
        return {
          questionId: Number( $( '[name="question_id"]' ).val() ),
          categoryId: Number( $( '[name="categoryId"]' ).val() ),
          sub_categoryId: Number( $( '[name="sub_categoryId"]' ).val() ),
          questionText: $( '[name="questionText"]' ).val(),
          questionType: Number( $( '[name="questionType"]' ).val() ),
          questionPicture: self.questionPicture,
          answers: self._createAnswerData( questionType ),
          topicLabels:
            $.makeArray( $( '[name="topicLabels[]"]' ) ).map( function ( element ) {
              return element.value;
            } ) || [],
          descriptionText: $( '[name="descriptionText"]' ).val(),
          descriptionPicture: self.descriptionPicture,
          draftFlag: draft
        };
      };

      self._createAnswerData = function ( questionType ) {
        if (
          questionType === QUESTION_TYPE.SELECT_ONE ||
          questionType === QUESTION_TYPE.SELECT_ALL
        ) {
          return $.makeArray(
            $( '.create__answer__input-wrapper' ).map( function ( index, element ) {
              return {
                label: $( element )
                  .find( '.create__answer__input' )
                  .val(),
                correctFlag: $( element )
                  .find( '.create__answer__correct__input' )
                  .prop( 'checked' ) ?
                  'True' :
                  'False'
              };
            } )
          );
        }

        if ( questionType === QUESTION_TYPE.YES_NO ) {
          return $.makeArray(
            $( '.create__answer__yes-no__input' ).map( function ( index, element ) {
              return {
                label: $( element )
                  .next()
                  .text(),
                correctFlag: $( element ).prop( 'checked' ) ? 'True' : 'False'
              };
            } )
          );
        }
      };

      self.submitDraft = function () {
        console.log( self._createSendData( self.currentQuestionType, 'True' ) );
        $.ajax( '/api/question/edit', {
          cache: false,
          type: 'POST',
          data: self._createSendData( self.currentQuestionType, 'True' ),
          dataType: 'json',
          success: function () {
            location.href = '/question/edit/complete';
          },
          error: function () {
            alert( '失敗222' );
          }
        } );
      };

      self.showPreview = function () {
        self.$preview
          .find( '.question__text' )
          .text( $( '[name="questionText"]' ).val() );
        var $answer = $( '<li class="correct-answer__item"></li>' );
        var $icon = $(
          '<svg class="correct-answer__icon" viewbox="0 0 11.929 9.186"><path d="M38.039 80.043l-6.863 6.863-2.522-2.522a.313.313 0 0 0-.443 0l-.738.738a.313.313 0 0 0 0 .443l3.481 3.481a.313.313 0 0 0 .443 0l7.822-7.822a.313.313 0 0 0 0-.443l-.738-.738a.313.313 0 0 0-.442 0z" transform="translate(-27.382 -79.952)"></path></svg>'
        );
        var $list = self.$preview.find( 'ul' );
        self
          ._createAnswerData( self.currentQuestionType )
          .filter( function ( answer ) {
            return answer.correctFlag === 'True';
          } )
          .forEach( function ( value ) {
            $list.append(
              $answer
                .clone()
                .append( $icon )
                .append( value.label )
            );
          } );
        self.questionPicture ?
          $( '.question__image' ).attr( 'src', self.questionPicture ) :
          $( '.question__image' ).attr(
            'src',
            '/static/img/challenge/question_default.jpg'
          );
        self.descriptionPicture ?
          $( '.description__image' ).attr( 'src', self.descriptionPicture ) :
          $( '.question__image' ).attr(
            'src',
            '/static/img/challenge/description_default.jpg'
          );

        self.$preview
          .find( '.description__paragraph' )
          .append( $( '[name="descriptionText"]' ).val() );

        self.$preview.attr( 'aria-hidden', 'false' );
      };
      self.closePreview = function () {
        self.$preview.attr( 'aria-hidden', 'true' );
        self.$preview.find( '.question__text' ).empty();
        self.$preview.find( '.description__paragraph' ).empty();
        self.$preview.find( 'ul' ).empty();
      };

      self.init();
    };
  } )();
  if ( $( '.create' ).length ) var questionToggle = new Create();
} );
