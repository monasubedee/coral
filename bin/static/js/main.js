//default settings
	UA__SP = navigator.userAgent.match(/(iPhone|iPad|iPod|Android)/i);

//setting_base
	//チェックボックス色変更
	$(function () {
		$('.checkbox-occupation').on('click',function(){
	  		$(this).next().toggleClass('text__blue');
		});
	});
	//トグル
	$(function () {
	    $('.content__sector-select-inner').hide();
		$('.checkbox-industry').click(function(event){
			var $this = $(event.currentTarget);
			var attrbiute = $this.attr("data-for");
			$('.content__sector-select-inner[data-target="'+attrbiute+'"]').slideToggle(200);
		});
	
	});
	//フリーワード
	$(function () {
		$('.content__role__new-word').click(function( event ){
			const $this = $( event.currentTarget );
			let roleVal = $('.form-sector__role-mid').val();
	  		
	  		let $addRole = $('<div class="content__word-tag"><div class="text__blue">'+roleVal+'</div><div class="close"></div></div>');
			$addRole.find('.close').on("click", function () {
				$addRole.remove();
			})
			$('.form-sector__role-wrapper').after($addRole);
		})
	});
	$(function () {
		$('.content__team__new-word').click(function(){
	  		let roleVal = $('.form-sector__team-large').val();
	  		let addRole = '<div class="content__word-tag"><div class="text__blue">'+roleVal+'</div><div class="close"></div></div>'
			$('.form-sector__team-wrapper').after($addRole);
		})
	});
	
	
	$(function () {
	  $('.close').on('click',function(){
		$(this).parent().remove();
		})
	});

//setting_member
	//一斉チェック
	$(function(){
		$('.content__article-heading .article-list__check').on('change',function(){
			$('input[type="checkbox"]').prop('checked', this.checked);
		})	
	})

	//内容のソート
	$(function(){
		const userSort = $('.article-heading__sort');
		const userPos = $('.article-heading__user-pos');
		const userPosList = $('.article-list__user-pos');
		const userStat = $('.article-heading__user-stat');
		const userStatList = $('.article-list__user-stat');

		userSort.click(function(){
			let flg = $(this).hasClass('active');
			let sortItem = $(this).parent().attr('class');
			let userSortElm = $(this);

			if (sortItem == 'article-heading__user-pos'){
				var userTxt = userPosList;
			} else if (sortItem == 'article-heading__user-stat'){
				var userTxt = userStatList;
			}
			var $arr = $('.content__member-list').sort(function(a, b){
				if (flg) {
					userSortElm.removeClass('active');
					return ($(a).find(userTxt).text() > $(b).find(userTxt).text() ? 1 : -1);
				}else{
					userSortElm.addClass('active');
					return ($(a).find(userTxt).text() < $(b).find(userTxt).text() ? 1 : -1);
				}
			});
			
			$arr.each(function(){
				$(this).appendTo('.contente__member-list-wrapper');
			});
			return false
		});

		//validation
		const valids = $('body').find($('[aria-invalid="false"]')).length;

		if(valids == 0){
			$('.contact__button').prop('disabled',false);
		}
		
		$('input,select').on('change keyup' , function(event){
			if($(this).attr('aria-invalid') != undefined){
				let invalidAlert = $(this).siblings('.form-company__invalid');
				if($(this).val() == ''){
					$(this).attr('aria-invalid','true');
					invalidAlert.attr('aria-hidden','false');
					$('.contact__button').prop('disabled',true);
				} else {
					$(this)[0].tagName !== 'option' ? $(this).attr('aria-invalid','false') : $(this).parent().attr('aria-invalid','false');
					invalidAlert.attr('aria-hidden','true');
					$('.contact__button').prop('disabled',false);
				}
			}
			if($('body').find($('[aria-invalid="false"]'+':not(:placeholder-shown)')).length == valids) {
					$('.contact__button').prop('disabled',false);
			} else {
					$('.contact__button').prop('disabled',true);
			}
		})
	});

//setting_company
	$(function(){
		$('.form__billing').hide();
		$('[name="billing"]').on('change', function (event) {
			$(this).prop('checked',
				function(){
					$('.form__billing').slideToggle(200);
				}
			)
		})

		//validation								
		$('input').on('change keyup' , function(event){
			if($(this).attr('aria-invalid') != undefined){
				let invalidAlert = $(this).siblings('.form-company__invalid');	
				if($(this).val() == ''){
					$(this).attr('aria-invalid','true');
					invalidAlert.attr('aria-hidden','false');
				} else {
					$(this).attr('aria-invalid','false');
					invalidAlert.attr('aria-hidden','true');
				}
			}
		})
	})

//solve_glossary
	$(function(){
		//星をつけるけす
		$('.star').click(function(){
			if($(this).attr('src').indexOf('1')!==-1){
				$(this).attr('src','img/star-2.png');
			}else{
				$(this).attr('src','img/star-1.png');
				}
		});
	//ハートをつけるけす
		$('.like').click(function(){
			if($(this).attr('src').indexOf('1')!==-1){
				$(this).attr('src','img/like2.png');
			}else{
				$(this).attr('src','img/like1.png');
				}
		});
	});

//animation動作設定
$(function(){
	if(!UA__SP){
		$('[data-anime-hover]').hover(function(){
			$(this).addClass('anime');
		},function(){
			$(this).removeClass('anime');
		});
		$('[data-anime-click]').on('click',function(){
			$(this).toggleClass('anime');
		});
	}
})