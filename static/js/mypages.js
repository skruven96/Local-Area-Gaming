
function pay(ticket) {
	$('.how-to-pay').css('height', '548px');

	$('.how-to-pay .sum').html('200');
	$('.how-to-pay .message').html(ticket);
}

function orderTicket() {
	$.ajax({
		url: 'queries/order_ticket',
		type: 'POST',
		data: {},
		success: function(result) {
			loadPage('mypages');
		}
	});
}

function giveAway(ticket) {
	var user = 'skruven'

	$.ajax({
		url: 'queries/give_ticket',
		type: 'POST',
		data: {
			'to_user': user
		},
		success: function(result) {
			if (result == "user doesn't exist") {

			} else if (result == "ticket ain't payed") {
				
			} else {
				loadPage('mypages');
			}
		}
	});
}
