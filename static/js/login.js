var oldToken = FB.getAccessToken();
var register_url = window.location.origin + '/api/register'
var get_twitter_request_token_url = window.location.origin + '/api/get_twitter_request_token'

$("#facebook-btn").on("click", function(){
    FB.login(function(response) {
        console.log(response)
        if (response.authResponse) {
            var data={provider : "facebook", access_token : response.authResponse.accessToken};

            post_register_api(register_url, data).then(response => {
                if (response){
                    alert("LOGIN SUCCESSFULLY");
                } else {
                    alert("LOGIN FAILED");
                }
            })
        } else {
            console.log('User cancelled login or did not fully authorize.');
            window.location = '/';
        }
        },{
            scope: 'email', 
            return_scopes: true,
            // auth_type: 'reauthenticate'
    });
})

$("#twitter-btn").on("click", function(event){
    event.preventDefault();
    get_twitter_login_api(get_twitter_request_token_url).then(response => {
        console.log(response)
        var oauth_token = response.oauth_token;
        const new_window = open("https://api.twitter.com/oauth/authenticate?oauth_token=" + oauth_token, "popupWindow", "width=600,height=600,scrollbars=yes");
        var pollTimer = window.setInterval(function() {
            if (new_window.closed !== false) { // !== is required for compatibility with Opera
                window.clearInterval(pollTimer);
                var data = {"provider" : "twitter", "oauth_token" : oauth_token}
                post_register_api(register_url, data).then(response => {
                    if (response){
                        alert("LOGIN SUCCESSFULLY");
                    } else {
                        alert("LOGIN FAILED");
                    }
                })
                // alert("Window is closed");

            }
        }, 200);
    })
})

$("form").on("submit", function(event){
    event.preventDefault();
    var passw = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,20}$/;
    if ($("#pass").val().match(passw)){
        var data = {"provider" : "default", "email" : $("#email").val(), "password" : $("#pass").val()}
        post_register_api(register_url, data).then(response => {
            if (response){
                alert("SIGN UP SUCCESSFULLY");
            } else {
                alert("SIGN UP FAILED");
            }
        })
    } else {
        alert("Password format is incorrect")
    }         
})

async function post_register_api(url, data){
    const response = await fetch(url, {
        method : "POST",
        headers : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify(data),
    });
    return await response.json()
}

async function get_twitter_login_api(url){
    const response = await fetch(url, {
        method : "GET",
    });
    return await response.json()
}