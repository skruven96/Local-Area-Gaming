
function show(element) {
    $(".game-div .teams .team").css("height", "61px");
    $(".game-div .teams .more").css("display", "inline-block");
    $(".game-div .teams .less").css("display", "none");
    
    $(element).css("display", "none");
    $(element.parentNode).find(".less").css("display", "inline-block");
    $(element.parentNode).css("height", "300px");
}

function less(element) {
    $(".game-div .teams .team").css("height", "61px");
    $(".game-div .teams .more").css("display", "inline-block");
    $(".game-div .teams .less").css("display", "none");
}

function game(game, left) {
    $(".selector").css("left", left);

    if (game === "dota2") {
        $(".game-dota2").css("left", "calc(50% - 460px)");          $(".game-dota2").css("z-index", "0");
        $(".game-lol").css("left", "calc(100% - 400px)");           $(".game-lol").css("z-index", "1");
        $(".game-hearthstone").css("left", "calc(100% - 200px)");   $(".game-hearthstone").css("z-index", "2");
        $(".game-csgo").css("left", "calc(100% - 70px)");           $(".game-csgo").css("z-index", "3");
    } else if (game === "lol") {
        $(".game-dota2").css("left", "-500px");                     $(".game-dota2").css("z-index", "1");
        $(".game-lol").css("left", "calc(50% - 460px)");            $(".game-lol").css("z-index", "0");
        $(".game-hearthstone").css("left", "calc(100% - 400px)");   $(".game-hearthstone").css("z-index", "1");
        $(".game-csgo").css("left", "calc(100% - 220px)");          $(".game-csgo").css("z-index", "2");
    } else if (game === "hearthstone") {
        $(".game-dota2").css("left", "-700px");                     $(".game-dota2").css("z-index", "2");
        $(".game-lol").css("left", "-520px");                       $(".game-lol").css("z-index", "1");
        $(".game-hearthstone").css("left", "calc(50% - 460px)");    $(".game-hearthstone").css("z-index", "0");
        $(".game-csgo").css("left", "calc(100% - 420px)");          $(".game-csgo").css("z-index", "1");
    } else if (game === "csgo") {
        $(".game-dota2").css("left", "-850px");                     $(".game-dota2").css("z-index", "3");
        $(".game-lol").css("left", "-720px");                       $(".game-lol").css("z-index", "2");
        $(".game-hearthstone").css("left", "-520px");               $(".game-hearthstone").css("z-index", "1");
        $(".game-csgo").css("left", "calc(50% - 460px)");           $(".game-csgo").css("z-index", "0");
    }
}
