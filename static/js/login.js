

// var firebaseConfig = {
//     apiKey: "AIzaSyBgHX9VekrMXBgRywEeI46VpZFGA0UhAno",
//     authDomain: "fresherseason2-teamtwo.firebaseapp.com",
//     databaseURL: "https://fresherseason2-teamtwo.firebaseio.com",
//     projectId: "fresherseason2-teamtwo",
//     storageBucket: "fresherseason2-teamtwo.appspot.com",
//     messagingSenderId: "525917873516",
//     appId: "1:525917873516:web:41086181b279acc01bff49",
//     measurementId: "G-1DRDS461L9"
// };
// Initialize Firebase
// firebase.initializeApp(firebaseConfig);
// firebase.analytics();

// var facebook_provider = new firebase.auth.FacebookAuthProvider();
// provider.addScope('user_birthday');
// facebook_provider.addScope('email');

// firebase.auth().useDeviceLanguage();
// facebook_provider.setCustomParameters({
//     'display': 'popup'
//   });



// $("#facebook-btn").on("click", function(event){
//   // event.preventDefault();
//   firebase.auth().signInWithPopup(facebook_provider).then(function(result) {
//     var token = result.credential.accessToken;
//     var user = result.user;
//     console.log('User>>FACEBOOK>>>>', user);
//     console.log("User Email : "+user.email)
//     userId = user.uid;

//   }).catch(function(error) {
//       console.error('Error: hande error here>>>', error.code);
//   })
// })

// $("#signup-btn").on("click", function(event){
//     event.preventDefault();
//     firebase.auth().createUserWithEmailAndPassword($("#email").val(), $("#pass").val()).then(function(result) {
//       var token = result.credential.accessToken;
//       var user = result.user;
//       console.log('User>>FACEBOOK>>>>', user);
//       console.log("User Email : "+user.email)
//       userId = user.uid;
  
//     }).catch(function(error) {
//         console.error('Error: hande error here>>>', error.code);
//     })
//   })




var oldToken = FB.getAccessToken();


$("#facebook-btn").on("click", function(){
    FB.logout(function(response){});
    FB.login(function(response) {
        console.log(response)
        if (response.authResponse && response.authResponse.accessToken != oldToken) {
            console.log('Welcome!  Fetching your information.... ');
            FB.api('/me', {fields: 'name, email'} , function(response) {
            console.log('Good to see you, ' + response.name + '.');
            console.log(response);
            window.location = '/Account/FacebookLogin?isCheckout=false';
         });
        } else {
            console.log('User cancelled login or did not fully authorize.');
            window.location = '/';
        }
        },{
            scope: 'email', 
            return_scopes: true,
            auth_type: 'reauthenticate'
    });
})

FB.getLoginStatus(function(response) {
    if (response.status === 'connected') {
      // The user is logged in and has authenticated your
      // app, and response.authResponse supplies
      // the user's ID, a valid access token, a signed
      // request, and the time the access token 
      // and signed request each expire.
      var uid = response.authResponse.userID;
      var accessToken = response.authResponse.accessToken;
      console.log("THIS USER IS CONNECTED")
    } else if (response.status === 'not_authorized') {
      // The user hasn't authorized your application.  They
      // must click the Login button, or you must call FB.login
      // in response to a user gesture, to launch a login dialog.
    } else {
      // The user isn't logged in to Facebook. You can launch a
      // login dialog with a user gesture, but the user may have
      // to log in to Facebook before authorizing your application.
    }
   });