var oldToken = FB.getAccessToken();
var register_url = window.location.origin + '/api/register'

$("#facebook-btn").on("click", function(){
    FB.login(function(response) {
        console.log(response)
        if (response.authResponse) {
            
            alert("LOGIN SUCCESSFULLY")
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


async function post_register_api(url, data){
    const response = await fetch(url, {
        method : "POST",
        header : {
            'Content-Type' : 'application/json'
        },
        body : JSON.stringify(data),
    });
    return await response
}