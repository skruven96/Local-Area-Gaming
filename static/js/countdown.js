var nextLan = new Date(2014, 11, 4, 17, 0, 0, 0)

setInterval(function() {
	if(nextLan.getTime() - (new Date()).getTime() <= 0)
	{
		$(".countdown .days").html(0);
		$(".countdown .hours").html(0);
		$(".countdown .minutes").html(0);
		$(".countdown .seconds").html(0);
		return;
	}
	
	var delta = new Date(nextLan.getTime() - (new Date()).getTime());
	
	$(".countdown .days").html(delta.getMonth());
	$(".countdown .hours").html(delta.getHours());
	$(".countdown .minutes").html(delta.getMinutes());
	$(".countdown .seconds").html(delta.getSeconds());
}, 1000);
