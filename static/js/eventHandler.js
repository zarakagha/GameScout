
function validatefname(fname) {
	let nameRegEx = /^[a-zA-Z]+$/;

	if (nameRegEx.test(fname))
		return true;
	else
		return false;
}

function validatelname(lname) {
    let nameRegEx = /^[a-zA-Z]+$/;
    
    if (nameRegEx.test(lname))
        return true;
   
    else
        return false;
}

function validatePWD(pwd) {
    let pwdRegEx =/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{8,}$/;
	if (pwdRegEx.test(pwd))
		return true;
	else
		return false;
}
function validateUsername(username) {
    let usernameRegEx = /^[a-zA-Z0-9\-_.]{5,12}$/;
        if (usernameRegEx.test(username))
            return true;
        else
            return false;
}
function validateEmail(email) {
    let emailRegEx = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
        if (emailRegEx.test(email))
            return true;
        else
            return false;
}

function validateLogin(event) 
{
    console.log("validateLogin called");
    let username =document.getElementById('username');
    let password =document.getElementById('password');
    let formIsValid = true;

    if(!validateUsername(username.value))
    {
      username.classList.add("errorborder");
      var errortext = document.getElementById("error-text-username");
      errortext.classList.remove("hidden");
      formIsValid = false;
    }
    else
    {
        username.classList.remove("errorborder");
        var errortext = document.getElementById("error-text-username");
		errortext.classList.add("hidden");
        
    }
    if(!validatePWD(password.value))
    {
        password.classList.add("errorborder");
        var errortext = document.getElementById("error-text-password");
        errortext.classList.remove("hidden");
        event.preventDefault();
        formIsValid = false;
       
    }
    else
    {
        password.classList.remove("errorborder");
        var errortext = document.getElementById("error-text-password");
        errortext.classList.add("hidden");
        
    }
    if (!formIsValid) {
        event.preventDefault();
    }
}
function validateSignup(event)  
{

    
    let fname =document.getElementById('firstname');
    let lname =document.getElementById('lastname');
    let username =document.getElementById('username');
    let email = document.getElementById('email');
    let password =document.getElementById('password');
    let formIsValid = true;

    if(!validatefname(fname.value))
    {
        fname.classList.add("errorborder");
        var errortext = document.getElementById("error-text-fname");
        fname.classList.remove("hidden");
        formIsValid = false;
    }
    else
    {
        fname.classList.remove("errorborder");
        var errortext = document.getElementById("error-text-fname");
        errortext.classList.add("hidden");
    }
    if(!validatelname(lname.value))
    {
        lname.classList.add("errorborder");
        var errortext = document.getElementById("error-text-lname");
        lname.classList.remove("hidden");
        formIsValid = false;
    }
    else
    {
        lname.classList.remove("errorborder");
        var errortext = document.getElementById("error-text-lname");
        errortext.classList.add("hidden");
    }
    if(!validateUsername(username.value))
    {
        username.classList.add("errorborder");
        var errortext = document.getElementById("error-text-username");
        username.classList.remove("hidden");
        formIsValid = false;
    }
    else
    {
        username.classList.remove("errorborder");
        var errortext = document.getElementById("error-text-username");
        errortext.classList.add("hidden");
    }
    if(!validateEmail(email.value))
    {
        email.classList.add("errorborder");
        var errortext = document.getElementById("error-text-email");
        username.classList.remove("hidden");
        formIsValid = false;
    }
    else
    {
        email.classList.remove("errorborder");
        var errortext = document.getElementById("error-text-email");
        errortext.classList.add("hidden");
    }
    if(!validatePWD(password.value))
    {
        password.classList.add("errorborder");
        var errortext = document.getElementById("error-text-password");
        password.classList.remove("hidden");
        formIsValid = false;
    }
    else
    {
        password.classList.remove("errorborder");
        var errortext = document.getElementById("error-text-password");
        errortext.classList.add("hidden");
    }
    if (!formIsValid) {
        
        event.preventDefault();
    }

}