var selectedTicket = '';

function pickSeat(seat) {
    if (selectedTicket != '') {
        $.ajax({
            url: 'queries/pick_seat',
            type: 'POST',
            data: {
                ticket: selectedTicket,
                seat: seat
            },
            success: function (result) {
                if (result == 'success') {

                }
            }
        });
        selectedTicket = '';
    }
}

function pickTicket(ticket) {
    selectedTicket = ticket;
}