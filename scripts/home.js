
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

var modal = document.getElementById('id01');
window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

function onSignIn(googleUser) {
  var profile = googleUser.getBasicProfile();
  console.log('ID: ' + profile.getId()); // Do not send to your backend! Use an ID token instead.
  console.log('Name: ' + profile.getName());
  console.log('Image URL: ' + profile.getImageUrl());
  console.log('Email: ' + profile.getEmail()); // This is null if the 'email' scope is not present.
}

function signOut() {
    var auth2 = gapi.auth2.getAuthInstance();
    auth2.signOut().then(function () {
      console.log('User signed out.');
    });
  }

$(document).ready(setUp);
