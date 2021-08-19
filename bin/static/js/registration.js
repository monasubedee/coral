$( function () {
  var Registration = ( function ( R, dateFns ) {
    return function () {
      var self = this;

      self.init = function () {
        self.$birthYear = $( '[name="birthYear"]' );
        self.$birthMonth = $( '[name="birthMonth"]' );
        self.$birthDay = $( '[name="birthDay"]' );
        self.$hiredYear = $( '[name="hiredYear"]' );
        self.$buttonAddLanguage = $( '.registration__add-language' );
        self.$buttonAddRole = $( '.registration__add-role' );
        self.$buttonAddSkill = $( '.registration__add-skill' );
        self.$buttonSubmit = $( '.registration__submit' );
        self.$buttonImageSelect = $( '.registration__add-picture' );
        self.$filePicture = $( '.registration__input-file' );
        self.initSelectDate();

        self.$buttonAddLanguage.on( 'click', self._addLanguage );
        self.$buttonAddRole.on( 'click', self._addRole );
        self.$buttonAddSkill.on( 'click', self._addSkill );
        self.$buttonSubmit.on( 'click', self.submit );
        self.$buttonImageSelect.on( 'click', self._onClickImageSelect );
        self.$filePicture.on( 'change', self._onChangeFile );
      };

      self.initSelectDate = function () {

        // 15歳からにしているが現状テストアカウントが2019年生まれのためコメントアウト
        // var maxYear = dateFns.getYear(
        //   dateFns.addYears( dateFns.setDayOfYear( new Date(), 1 ), -15 )
        // );
        var maxYear = dateFns.getYear( new Date() );
        var yearRange = R.range( 1940, maxYear + 1 );
        yearRange.forEach( function ( year ) {
          self.$birthYear.append(
            '<option value="' + year + '">' + year + '</option>'
          );
        } );

        self.appendDayOption(
          new Date(
            dateFns.getYear( self.$birthYear.attr( 'data-birth-date' ) ),
            dateFns.getMonth( self.$birthYear.attr( 'data-birth-date' ) )
          )
        );

        var maxHiredYear = dateFns.getYear( new Date() );
        var yearRange = R.range( 1940, maxHiredYear + 1 );
        yearRange.forEach( function ( year ) {
          self.$hiredYear.append(
            '<option value="' + year + '">' + year + '</option>'
          );
        } );
      };

      self.appendDayOption = function ( date ) {

        // 後で変更
        // self.$birthDay.empty();
        // var maxDay = dateFns.getDaysInMonth( date );
        // var dayRange = R.range( 1, maxDay + 1 );
        // dayRange.forEach( function ( day ) {
        //   self.$birthDay.append(
        //     '<option value="' + day + '">' + day + '</option>'
        //   );
        // } );
      };

      self._showRoleLabels = function () {
        $( '[name="roles"]' ).length &&
          $( '.registration__role-list' ).attr( 'aria-hidden', 'false' );
      };

      self._addRole = function () {
        var value = $( '[name="role"]' ).val();
        if ( !value ) return;

        $( '[name="role"]' ).val( '' );
        var deleteButton = $(
          '<button class="create__description__topic-remove"></button>'
        );
        var input = $( '<input type="hidden"name="roles">' ).val( value );
        var item = $( '<li class="create__description__topic-item"></li>' )
          .append( value )
          .append( deleteButton )
          .append( input );
        $( '.registration__role-list' ).append( item );
        self._showRoleLabels();
      };

      self._showSkillSetLabels = function () {
        $( '[name="skillSet"]' ).length &&
          $( '.registration__skill-list' ).attr( 'aria-hidden', 'false' );
      };

      self._addSkill = function () {
        var value = $( '[name="skill"]' ).val();
        if ( !value ) return;

        $( '[name="skill"]' ).val( '' );
        var deleteButton = $(
          '<button class="create__description__topic-remove"></button>'
        );
        var input = $( '<input type="hidden"name="skillSet">' ).val( value );
        var item = $( '<li class="create__description__topic-item"></li>' )
          .append( value )
          .append( deleteButton )
          .append( input );
        $( '.registration__skill-list' ).append( item );
        self._showSkillSetLabels();
      };

      self._showLanguageLabels = function () {
        $( '[name="languageSet"]' ).length &&
          $( '.registration__language-list' ).attr( 'aria-hidden', 'false' );
      };

      self._addLanguage = function () {
        var value = $( '[name="language"]' ).val();
        if (
          !value ||
          !$.makeArray( $( '#languageList option' ) )
            .map( function ( element ) {
              return element.value;
            } )
            .includes( value )
        )
          return;

        $( '[name="language"]' ).val( '' );
        var deleteButton = $(
          '<button class="create__description__topic-remove"></button>'
        );
        var input = $( '<input type="hidden"name="languageSet">' ).val( value );

        var item = $( '<li class="create__description__topic-item"></li>' )
          .append( value )
          .append( deleteButton )
          .append( input );
        $( '.registration__language-list' ).append( item );
        self._showLanguageLabels();
      };

      self._onClickImageSelect = function () {
        self.$filePicture.trigger( 'click' );
      };

      self._onChangeFile = function ( event ) {
        var $this = $( event.currentTarget );
        const fr = new FileReader();
        var file = event.target.files[ 0 ];

        if ( file && file.type.match( 'image.*' ) ) {
          fr.readAsDataURL( file );
        }

        fr.onload = function ( _this ) {
          if ( $this.attr( 'name' ) === 'profilePicture' )
            self.profilePicture = _this.currentTarget.result;
          $( '.registration__icon' ).attr( 'src', self.profilePicture );
        };
      };

      self._getValidation = function () {
        var errorArray = [];
        if ( $( '[name="displayName"]' ).val() === '' )
          errorArray.push( { name: 'displayName', reason: 'required' } );
        if ( $( '[name="name"]' ).val() === '' )
          errorArray.push( { name: 'name', reason: 'required' } );
        if ( $( '[name="password"]' ).val() === '' )
          errorArray.push( { name: 'password', reason: 'required' } );
        if ( !/.+@.+\..+/.test( $( '[name="name"]' ).val() ) )
          errorArray.push( { name: 'name', reason: 'invalidType' } );
        if ( $( '[name="hiredYear"]' ).val() === '' )
          errorArray.push( { name: 'hiredYear', reason: 'required' } );
        if ( !$( '[name="languageSet"]' ).length )
          errorArray.push( { name: 'languageSet', reason: 'required' } );
        return errorArray.length ? errorArray : undefined;
      };
      self._showValidate = function ( errorReasons ) {
        if ( !errorReasons ) return undefined;

        errorReasons.forEach( function ( reason ) {
          $(
            '[data-name=' + reason.name + '][data-reason=' + reason.reason + ']'
          ).attr( 'aria-hidden', 'false' );
        } );
        return errorReasons;
      };

      self.submit = function () {
        console.log( 'self._createSendData()', self._createSendData() );
        if ( self._showValidate( self._getValidation() ) ) {
          console.log( 'validate!' );
          return;
        }
        console.log( self._createSendData() );

        $.ajax( '/registration', {
          cache: false,
          type: 'POST',
          data: self._createSendData(),
          dataType: 'json',
          success: function ( res ) {
            location.href = '/registration_thanks';
          },
          error: function ( e ) {
            console.log( e );
            alert( '失敗' );
            if ( e.message === 'a user was already exist on db.' ) {
              return self._showValidate( [
                {
                  name: 'name',
                  reason: 'serverError'
                }
              ] );
            }
          }
        } );
      };

      self._createSendData = function ( questionType, draft ) {
        return {
          displayName: $( '[name="displayName"]' ).val(),
          name: $( '[name="name"]' ).val(),
          password: $( '[name="password"]' ).val(),
          gender: Number( $( '[name="gender"]' ).val() ),
          occupation: $( '[name="occupation"]' ).val(),
          birthYear: $( '[name="birthYear"]' ).val(),
          birthMonth: $( '[name="birthMonth"]' ).val(),
          birthDay: $( '[name="birthDay"]' ).val(),
          hiredYear: $( '[name="hiredYear"]' ).val(),
          hiredMonth: $( '[name="hiredMonth"]' ).val(),
          hiredDay: $( '[name="hiredDay"]' ).val(),
          country: $( '[name="country"]' ).val(),
          languageSet:
            $.makeArray( $( '[name="languageSet"]' ) ).map( function ( element ) {
              return element.value;
            } ) || [],
          roles:
            $.makeArray( $( '[name="roles"]' ) ).map( function ( element ) {
              return element.value;
            } ) || [],
          skillSet:
            $.makeArray( $( '[name="skillSet"]' ) ).map( function ( element ) {
              return element.value;
            } ) || [],
          goal: $( '[name="goal"]' ).val(),
          profilePicture: self.profilePicture || ''
        };
      };

      self.arrayReducer = function ( accumulator, currentValue, currentIndex ) {
        accumulator[ currentIndex ] = currentValue;
        return accumulator;
      };
      self.init();
    };
  } )( R, dateFns );
  if ( $( '.registration' ).length ) var registration = new Registration();
} );
