
function displaySidebar() {
    if($('#sidebar').css('display')== "none"){
        $('#sidebar').css({display:'block'});
        $('.column').css({width:'33.3%'});
        $('#right').css({ left:'33.3%'});
        $('.tap').css({right:'30%'});
    }
    else if($('#sidebar').css('display')== "block"){
        $('#sidebar').css({display:'none'});
        $('.column').css({width:'50%'})
        $('#right').css({ left:'50%'})
        $('.tap').css({right:'-50px'})
    }
}
function setUp(){
    $('.tap').on('click', displaySidebar);
}

$(document).ready(setUp);