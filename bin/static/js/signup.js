$( function () {
  var ProfileEdit = ( function ( R, dateFns ) {
    return function () {
      var self = this;

      self.init = function () {
        self.$birthYear = $( '[name="birthYear"]' );
        self.$birthMonth = $( '[name="birthMonth"]' );
        self.$birthDay = $( '[name="birthDay"]' );
        self.$hiredYear = $( '[name="hiredYear"]' );
        self.$buttonAddRole = $( '.profile-edit__add-role' );
        self.$buttonAddSkill = $( '.profile-edit__add-skill' );
        self.$buttonSubmit = $( 'profile- edit__submit' );
        self.$buttonImageSelect = $( '.profile-edit__add-picture' );
        self.$filePicture = $( '.profile-edit__input-file' );
        self.initSelectDate();

        self.$buttonAddRole.on( 'click', self._addRole );
        self.$buttonAddSkill.on( 'click', self._addSkill );
        self.$buttonSubmit.on( 'click', self.submit );
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
        self.$hiredYear.val(
          dateFns.getYear( self.$hiredYear.attr( 'data-hired-year' ) )
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

      self.submit = function () {
        $.ajax( '/api//user/profile', {
          cache: false,
          type: 'POST',
          data: self._createSendData(),
          dataType: 'json',
          success: function () {
            location.href = '/create/complete';
          },
          error: function () {
            alert( '失敗' );
          }
        } );
      };

      self._createSendData = function ( questionType, draft ) {
        return {
          name: Number( $( '[name="name"]' ).val() ),
          gender: Number( $( '[name="gender"]' ).val() ),
          birthDate: new Date(
            Number( $( '[name="birthYear"]' ).val() ),
            Number( $( '[name="birthMonth"]' ).val() ) - 1,
            Number( $( '[name="birthDay"]' ).val() ) - 1
          ),
          hiredYear: Number( $( '[name="hiredYear"]' ).val() ),
          country: Number( $( '[name="country"]' ).val() ),
          languageSet: Number( $( '[name="languageSet"]' ).val() ),
          roles:
            $.makeArray( $( '[name="roles[]"]' ) ).map( function ( element ) {
              return element.value;
            } ) || [],
          skillSet:
            $.makeArray( $( '[name="skillSet[]"]' ) ).map( function ( element ) {
              return element.value;
            } ) || [],
          goal: $( '[name="goal"]' ).val(),
          profilePicture: self.profilePicture
        };
      };

      self.init();
    };
  } )( R, dateFns );
  if ( $( '.profile-edit' ).length ) var ProfileEdit = new ProfileEdit();
} );
[ec2-user@ip-172-31-8-61 coral]$ git status
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

	modified:   bin/app.py
	modified:   bin/static/css/style.css
	modified:   bin/templates/challenge.html
	modified:   bin/templates/create.html
	modified:   bin/templates/create_complete.html
	modified:   bin/templates/partials/head.html
	modified:   bin/templates/profile_edit.html
	modified:   bin/templates/question_edit.html
	modified:   bin/templates/question_edit_complete.html
	modified:   bin/templates/registration.html
	modified:   bin/templates/result.html

Untracked files:
  (use "git add <file>..." to include in what will be committed)

	bin/__pycache__/
	bin/guniconf.cnf
	bin/log/
	bin/nohup.out
	bin/static/js/signup.js
	bin/templates/signup.html

no changes added to commit (use "git add" and/or "git commit -a")
[ec2-user@ip-172-31-8-61 coral]$ cat bin/guniconf.cnf
import multiprocessing

workers = 3
worker_class = 'sync'

socket_path = "unix:/home/ec2-user/coral/bin/tmp/kb_coral.sock"
bind = socket_path
accesslog = "/home/ec2-user/coral/bin/log/gunicorn-access.log"
errorlog = "/home/ec2-user/coral/bin/log/gunicorn-error.log"
loglevel = "info"
[ec2-user@ip-172-31-8-61 coral]$ cat bin/static/js/signup.js
$( function () {
  var ProfileEdit = ( function ( R, dateFns ) {
    return function () {
      var self = this;

      self.init = function () {
        self.$birthYear = $( '[name="birthYear"]' );
        self.$birthMonth = $( '[name="birthMonth"]' );
        self.$birthDay = $( '[name="birthDay"]' );
        self.$hiredYear = $( '[name="hiredYear"]' );
        self.$buttonAddRole = $( '.profile-edit__add-role' );
        self.$buttonAddSkill = $( '.profile-edit__add-skill' );
        self.$buttonSubmit = $( 'profile- edit__submit' );
        self.$buttonImageSelect = $( '.profile-edit__add-picture' );
        self.$filePicture = $( '.profile-edit__input-file' );
        self.initSelectDate();

        self.$buttonAddRole.on( 'click', self._addRole );
        self.$buttonAddSkill.on( 'click', self._addSkill );
        self.$buttonSubmit.on( 'click', self.submit );
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
        self.$hiredYear.val(
          dateFns.getYear( self.$hiredYear.attr( 'data-hired-year' ) )
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

      self.submit = function () {
        $.ajax( '/api//user/profile', {
          cache: false,
          type: 'POST',
          data: self._createSendData(),
          dataType: 'json',
          success: function () {
            location.href = '/create/complete';
          },
          error: function () {
            alert( '失敗' );
          }
        } );
      };

      self._createSendData = function ( questionType, draft ) {
        return {
          name: Number( $( '[name="name"]' ).val() ),
          gender: Number( $( '[name="gender"]' ).val() ),
          birthDate: new Date(
            Number( $( '[name="birthYear"]' ).val() ),
            Number( $( '[name="birthMonth"]' ).val() ) - 1,
            Number( $( '[name="birthDay"]' ).val() ) - 1
          ),
          hiredYear: Number( $( '[name="hiredYear"]' ).val() ),
          country: Number( $( '[name="country"]' ).val() ),
          languageSet: Number( $( '[name="languageSet"]' ).val() ),
          roles:
            $.makeArray( $( '[name="roles[]"]' ) ).map( function ( element ) {
              return element.value;
            } ) || [],
          skillSet:
            $.makeArray( $( '[name="skillSet[]"]' ) ).map( function ( element ) {
              return element.value;
            } ) || [],
          goal: $( '[name="goal"]' ).val(),
          profilePicture: self.profilePicture
        };
      };

      self.init();
    };
  } )( R, dateFns );
  if ( $( '.profile-edit' ).length ) var ProfileEdit = new ProfileEdit();
} );
