function input_varidate(element, obj) {
  var value = $.trim($(element).val());
  var varidate = true;
  var message = "";
  if (obj.message) message = obj.message;
  switch (obj.type) {
    case 'email':
      var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
      if (!value.match(mailformat)) varidate = 'メールアドレスの形式で入力してください';
      if (!value.match(/^[A-Za-z0-9@.]*$/)) varidate = '半角英数字で入力してください';
      break;
    case 'half':
      if (!value.match(/^[A-Za-z0-9]*$/)) varidate = '半角英数字で入力してください';
      break;
    case 'half-number':
      if (!value.match(/^[0-9]*$/)) varidate = '半角数字で入力してください';
      break;
    case 'kana':
      if (value.match(/[\u4E00-\u9FFF]/)) varidate = 'ひらがな・カタカナ・半角英数字で入力してください';
      console.log(varidate);
      break;
    case 'password':
      value = value.replace(/\s+/g, "");
      $(element).val(value);
      if (value.match(/\s+/g)) {
        varidate = 'スペースを含まないでください';
      }else{
        if (!value.match(/^[A-Za-z0-9]*$/)) {
          varidate = 'パスワードの形式が不正です';
        } else {
          if (value.match(/^[A-Za-z]*$/) || value.match(/^[0-9]*$/)) {
            varidate = 'パスワードの形式が不正です';
          }
        }
      }
      break;

  }
  if (obj.maxLength && value.length > obj.maxLength) varidate = '上限の' + obj.maxLength + '文字を超えています';
  if (obj.minLength && value.length < obj.minLength) varidate = obj.minLength + '文字以上で入力してください';
  if (message) message = message + 'が';
  if (obj.required && value == '') varidate = message + '入力されていません';
  if (varidate != true && obj.ex) varidate += obj.ex;
  return varidate;
}

function input_errorMessage(element, status) {
  if (status) {
    $(element).addClass("error-field").attr("placeholder", status);
    $(element).addClass('red-placeholder-class');
  } else {
    $(element).removeClass("error-field").attr("placeholder", '');
    $(element).removeClass('red-placeholder-class');
  }
}

function input_errorElement(element, status, parent ,dom = "p") {
  $(parent).find('.error-element').remove();
  if (status) {
    $(parent).append('<' + dom + ' class="error-element m-0 color-red"><small>' + status + '</small></' + dom + '>');
    $(element).addClass("error-field");
    $(element).addClass('red-placeholder-class');
  } else {
    $(element).removeClass("error-field");
    $(element).removeClass('red-placeholder-class');
  }
}
