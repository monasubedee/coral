"use strict";

$(function () {
  var error_obj = {
    company: false,
    department: false,
    name: false,
    email: false,
    tel: false,
    contents: false,
    policy: false
  };
  $("#confirm").on("click", function () {
    $("html, body").animate({
      scrollTop: 0
    }, 400);
    $(".contact__confirm").remove();
    error_obj.company = input_varidate("#company", {
      required: true,
      maxLength: 100
    });
    error_obj.department = input_varidate("#department", {
      maxLength: 100
    });
    error_obj.name = input_varidate("#name", {
      required: true,
      maxLength: 100
    });
    error_obj.email = input_varidate("#email", {
      required: true,
      type: "email",
      maxLength: 100
    });
    error_obj.tel = input_varidate("#tel", {
      required: true,
      type: "half-number",
      maxLength: 11
    });
    error_obj.contents = input_varidate("#contents", {
      required: true,
      maxLength: 2000
    });

    if ($('#policy').prop('checked') != true) {
      error_obj.policy = '同意されていません';
    } else {
      error_obj.policy = true;
    }

    var varidate = true;

    for (var id in error_obj) {
      if (error_obj.hasOwnProperty(id)) {
        if (error_obj[id] !== true) {
          input_errorElement("#" + id, error_obj[id], "." + id + "--wrap");
          varidate = false;
        } else {
          input_errorElement("#" + id, "", "." + id + "--wrap");
          $("." + id + "--wrap").append('<p class="contact__confirm">' + $("#" + id).val().replace(/\r?\n/g, "<br>") + "</p>");
        }
      }
    }

    if (varidate) {
      $(".contact").addClass("confirm");
    }
  });
  $("#back").on("click", function () {
    $("html, body").animate({
      scrollTop: 0
    }, 400);
    $(".contact").removeClass("confirm");
  });
  $("#send").on("click", function () {
    var obj = {};
    var company = document.getElementById("company").value;
    var dept = document.getElementById("department").value;
    var full_name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var phone = document.getElementById("tel").value;
    var contents = document.getElementById("contents").value;
    obj = {
      companyName: company,
      deptName: dept,
      fullName: full_name,
      inquiry_msg: contents,
      mail: email,
      phone: phone
    };
    $.ajax({
      type: "POST",
      url: "/introduction/contact/",
      headers: {
        "Content-Type": "application/json"
      },
      data: JSON.stringify(obj),
      success: function success(data) {
        if (data["result"] == "ok") {
          window.location.href = "/introduction/contact/thanks/";
        } else {
          console.log("Fail");
        }
      }
    });
  });
});