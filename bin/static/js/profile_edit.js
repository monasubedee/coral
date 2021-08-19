$( function () {
  var ProfileEdit = ( function ( R, dateFns ) {
    return function () {
      var self = this;

      self.init = function () {
        self.$birthYear = $( '[name="birthYear"]' );
        self.$birthMonth = $( '[name="birthMonth"]' );
        self.$birthDay = $( '[name="birthDay"]' );
        self.$hireYear = $( '[name="hireYear"]' );
        self.$hireMonth = $( '[name="hireMonth"]' );
        self.$hireDay = $( '[name="hireDay"]' );
        self.$buttonAddLanguage = $( '.profile-edit__add-language' );
        self.$buttonAddRole = $( '.profile-edit__add-role' );
        self.$buttonAddSkill = $( '.profile-edit__add-skill' );
        self.$buttonSubmit = $( '.profile-edit__submit' );
        self.$buttonImageSelect = $( '.profile-edit__add-picture' );
        self.$filePicture = $( '.profile-edit__input-file' );
        self.$deleteLanguage = $( '.profile-edit__delete-language' );
        self.initSelectDate();

        self.$deleteLanguage.on( 'click', self.deleteLanguage );
        self.$buttonAddLanguage.on( 'click', self._addLanguage );
        self.$buttonAddRole.on( 'click', self._addRole );
        self.$buttonAddSkill.on( 'click', self._addSkill );
        self.$buttonSubmit.on( 'click', self.submit );
        self.$filePicture.on( 'change', self._onChangeFile );
      };

      self.initSelectDate = function () {
        var maxYear = dateFns.getYear( new Date() );
        var yearRange = R.range( 1940, maxYear + 1 );
        yearRange.forEach( function ( year ) {
          self.$birthYear.append(
            '<option value="' + year + '">' + year + '</option>'
          );
        } );

        self.$birthYear.val(
          dateFns.getYear( self.$birthYear.attr( 'data-birth-date' ) )
        );
        self.$birthMonth.val(
          dateFns.getMonth( self.$birthMonth.attr( 'data-birth-date' ) ) + 1
        );

        self.appendDayOption(
          new Date(
            dateFns.getYear( self.$birthYear.attr( 'data-birth-date' ) ),
            dateFns.getMonth( self.$birthYear.attr( 'data-birth-date' ) )
          )
        );

        self.$birthDay.val(
          dateFns.getDate( self.$birthDay.attr( 'data-birth-date' ) )
        );

        var maxHiredYear = dateFns.getYear( new Date() );
        var yearRange = R.range( 1940, maxHiredYear + 1 );
        yearRange.forEach( function ( year ) {
          self.$hireYear.append(
            '<option value="' + year + '">' + year + '</option>'
          );
        } );
        self.$hireYear.val(
          dateFns.getYear( self.$hireYear.attr( 'data-hire-date' ) )
        );

        self.$hireMonth.val(
          dateFns.getMonth( self.$hireMonth.attr( 'data-hire-date' ) ) + 1
        );

        self.$hireDay.val(
          dateFns.getDate( self.$hireDay.attr( 'data-hire-date' ) )
        );
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
        $( '[name="roles[]"]' ).length &&
          $( '.profile-edit__role-list' ).attr( 'aria-hidden', 'false' );
      };

      self._addRole = function () {
        var value = $( '[name="role"]' ).val();
        if ( !value ) return;

        $( '[name="role"]' ).val( '' );
        var deleteButton = $(
          '<button class="create__description__topic-remove"></button>'
        );
        var input = $( '<input type="hidden"name="roles[]">' ).val( value );
        var item = $( '<li class="create__description__topic-item"></li>' )
          .append( value )
          .append( deleteButton )
          .append( input );
        $( '.profile-edit__role-list' ).append( item );
        self._showRoleLabels();
      };

      self._showSkillSetLabels = function () {
        $( '[name="skillset[]"]' ).length &&
          $( '.profile-edit__role-list' ).attr( 'aria-hidden', 'false' );
      };

      self._addSkill = function () {
        var value = $( '[name="skill"]' ).val();
        if ( !value ) return;

        $( '[name="skill"]' ).val( '' );
        var deleteButton = $(
          '<button class="create__description__topic-remove"></button>'
        );
        var input = $( '<input type="hidden"name="skillSet[]">' ).val( value );
        var item = $( '<li class="create__description__topic-item"></li>' )
          .append( value )
          .append( deleteButton )
          .append( input );
        $( '.profile-edit__skill-list' ).append( item );
        self._showSkillSetLabels();
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
        };
      };

      self._showLanguageLabels = function () {
        $( '[name="languageSet"]' ).length &&
          $( '.profile-edit__language-list' ).attr( 'aria-hidden', 'false' );
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
          '<button class="create__description__topic-remove profile-edit__delete-language"></button>'
        );
        var input = $( '<input type="hidden"name="languageSet">' ).val( value );

        var item = $( '<li class="create__description__topic-item"></li>' )
          .append( value )
          .append( deleteButton )
          .append( input );
        $( '.profile-edit__language-list' ).append( item );
        deleteButton.on( 'click', self.deleteLanguage );
        self._showLanguageLabels();
      };

      self.deleteLanguage = function ( event ) {
        var $this = $( event.currentTarget );
        $this.parent().remove();
        if ( !$( '.create__description__topic-item' ).length )
          $( '.profile-edit__language-list' ).attr( 'aria-hidden', 'true' );
      };

      self.submit = function () {
        console.log( self._createSendData() );
        $.ajax( '/api/profile_edit', {
          cache: false,
          type: 'POST',
          data: self._createSendData(),
          dataType: 'json',
          success: function () {
            location.href = '/mypage';
          },
          error: function () {
            alert( '失敗' );
          }
        } );
      };

      self._createSendData = function ( questionType, draft ) {
        return {
          displayName: $( '[name="displayName"]' ).val(),
          gender: Number( $( '[name="gender"]' ).val() ),
          occupationId: Number( $( '[name="occupationId"]' ).val() ),
          birthYear: $( '[name="birthYear"]' ).val(),
          birthMonth: $( '[name="birthMonth"]' ).val(),
          birthDay: $( '[name="birthDay"]' ).val(),
          hireYear: $( '[name="hireYear"]' ).val(),
          hireMonth: $( '[name="hireMonth"]' ).val(),
          hireDay: $( '[name="hireDay"]' ).val(),
          countryId: Number( $( '[name="countryId"]' ).val() ),
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

      self.init();
    };
  } )( R, dateFns );
  if ( $( '.profile-edit' ).length ) var profileEdit = new ProfileEdit();
} );
