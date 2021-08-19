$(function(){
	$("#doClip").click(function(){
		var textData = JSON.stringify({
			"questionId":$("#questionId").val()
		});
		$.ajax( '/api/clip', {
			type: 'POST',
			cache: false,
			data: textData,
			contentType:'application/json',
			success: function () {
				alert("クリップは送信されました．");
				// doClipボタンの色を変更する．
			},
			error: function () {
				alert("クリップが送信できませんでした．");
			}
		} );            
	});
});