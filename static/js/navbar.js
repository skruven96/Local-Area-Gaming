var currentPage = 'home';

function loadPage(page) {
    currentPage = page;
    $('.items').find('*').css('background-color', 'transparent');
    $('.login').css('background-color', 'transparent');
    $('.logout').css('background-color', 'transparent');

    if (page === 'home') {
        $('.navbar').css('background-color', '#FF5722');
        $('.navitem-home').css('background-color', '#E64A19');
    } else if (page === 'seats') {
        $('.navbar').css('background-color', '#4CAF50');
        $('.navitem-seats').css('background-color', '#388E3C');
    } else if (page === 'tournaments') {
        $('.navbar').css('background-color', '#9E9E9E');
        $('.navitem-tournaments').css('background-color', '#616161');
    } else if (page === 'mypages') {
        $('.navbar').css('background-color', '#00BCD4');
        $('.navitem-mypages').css('background-color', '#0097A7');
    } else {
        $('.navbar').css('background-color', '#9C27B0');
        $('.login').css('background-color', '#7B1FA2');
    }

    $.ajax({
        url: page + '/',
        type: 'GET',
        data: {},
        success: function(string) {
            $('.content').html(string);
        }
    });
}

function loadPlayerPage(player) {
    var name = player.html();

    $.ajax({
        url: 'player/' + name + '/',
        type: 'POST',
        data: {},
        success: function(string) {
            $('.content').html(string);
        }
    });
}