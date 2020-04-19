$(document).ready(function() {
	$("#about-btn").click( function(event){
		alert("you clicked the button using JQuery");
	});
});


$("#about-btn").click( function(event) {
	msgstr = $("#msg").html()
	msgstr = msgstr + "ooo";
	$("#msg").html(msgstr)
});

// $(".ouch").click( function(event){
// 	alert("You clicked me! ouch");
// });

// $("p").hover( function(){
// 	$(this).css('color','red');
// },
// function(){
// 	$(this).css('color','blue');
// });

$.("#likes").click( function(event) {
	var catid;
	catid = $(this).attr("data-catid");
	$.get('/rango/like/', {category_id : catid}, function(data){
		$("#like_count").html(data);
		$('#likes').hide();
	});
});

$('#suggestion').keyup(function(){
	var query;
	query = $(this).val();
	$.get('/rango/suggest/', {suggestion : query}, function(data){
		$('#cats').html(data);
	};
});

$.("#page").click( function(event){
	var title;
	var url;
	var catid;
	catid = $(this).attr("data-catid");
	title = $(this).attr("data-title");
	url = $(this).attr("data-url");

	var me = $(this);


	$.get('/rango/add/', {category_id : catid, title : title, url : url}, function(data){
			$('#pages').html(data);
			me.hide();
	});
});