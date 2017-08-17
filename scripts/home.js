
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

function runme() {
    var arr = [
      "/personal_hobby?name=acting",
      "/personal_hobby?name=archery",
      "/personal_hobby?name=baking",
      "/personal_hobby?name=coding",
      "/personal_hobby?name=cooking",
      "/personal_hobby?name=cycling",
      "/personal_hobby?name=dancing",
      "/personal_hobby?name=drawing",
      "/personal_hobby?name=fishing",
      "/personal_hobby?name=geocaching",
      "/personal_hobby?name=hiking",
      "/personal_hobby?name=ice%20skating",
      "personal_hobby?name=knitting,%20crochet",
      "/personal_hobby?name=learning%20a%20new%20language",
      "/personal_hobby?name=learning%20a%20new%20musical%20instrument",
      "/personal_hobby?name=martial%20arts",
      "/personal_hobby?name=origami",
      "/personal_hobby?name=photography",
      "/personal_hobby?name=playing%20pool",
      "/personal_hobby?name=poetry%20writing",
      "/personal_hobby?name=puzzles%20solving",
      "/personal_hobby?name=reading",
      "/personal_hobby?name=rock%20climbing",
      "/personal_hobby?name=rollerblading",
      "/personal_hobby?name=running",
      "/personal_hobby?name=sailing",
      "/personal_hobby?name=scrapbooking",
      "/personal_hobby?name=snorkeling",
      "/personal_hobby?name=swimming",
      "/personal_hobby?name=table%20tennis",
      "/personal_hobby?name=volunteering",
      "/personal_hobby?name=watching%20anime",
      "/personal_hobby?name=yoga",
    ];
    var value = arr[Math.floor(Math.random() * arr.length)];
    // alert("Would navigate to : " + value);
     window.location = value;     // remove the comment at the beginning to actually navigate
}

//   function shuffle(o){ //v1.0
//       for(var j, x, i = o.length; i; j = Math.floor(Math.random() * i), x = o[--i], o[i] = o[j], o[j] = x);
//       return o;
//   };
//
//   $(document).ready(function() {
//     var images = ['/styles/Images/001.jpg', '/styles/Images/002.jpg', '/styles/Images/003.jpg', '/styles/Images/004.jpg', '/styles/Images/005.jpg', '/styles/Images/006.jpg', '/styles/Images/007.jpg', '/styles/Images/008.jpg', '/styles/Images/009.jpg', '/styles/Images/010.jpg'];
//     images = shuffle(images);
//
//     $('.column').each(function(i){
//         $(this).css({
//           'background-image': 'url(' + images[i] + ')'});
//     });
// });
