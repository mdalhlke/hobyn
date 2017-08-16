
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

  function shuffle(o){ //v1.0
      for(var j, x, i = o.length; i; j = Math.floor(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
      return o;
  };

  $(document).ready(function() {
    var images = ['/styles/Images/001.jpg', '/styles/Images/002.jpg', '/styles/Images/003.jpg', '/styles/Images/004.jpg', '/styles/Images/005.jpg', '/styles/Images/006.jpg', '/styles/Images/007.jpg', '/styles/Images/008.jpg', '/styles/Images/009.jpg', '/styles/Images/010.jpg'];
    images = shuffle(images);

    $('.column').each(function(i){
        $(this).css({
          'background-image': 'url(' + images[i] + ')'});
    });
});
