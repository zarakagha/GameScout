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
	if (pwd.length === 8)
		return true;
	else
		return false;
}

function validateUsername(uname) {

    let unameRegEx = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
        if (unameRegEx.test(uname))
            return true;
        else
            return false;
}

function validateLogin(event) 
{
    let username =document.getElementById('username');
    let password =document.getElementById('password');
    let formisvalid = true;

    if(!validateUsername(username.value))
    {
      username.classList.add("errorborder");
      var errortext = document.getElementById("error-text-username");
      errortext.classList.remove("hidden");
      event.preventDefault();
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
       
    }
    else
    {
        password.classList.remove("errorborder");
        var errortext = document.getElementById("error-text-password");
        errortext.classList.add("hidden");
        
    }
    if(formisvalid===true)
    {
        console.log("Validation passed");
    }
}
function validateSignup(event)  
{
    let fname =document.getElementById('firstname');
    let lname =document.getElementById('lastname');
    let username =document.getElementById('email');
    let password =document.getElementById('password');
    let password2 =document.getElementById('repassword');
    let formisvalid = true;

    if(!validatefname(fname.value))
    {
        fname.classList.add("errorborder");
        var errortext = document.getElementById("error-text-fname");
        fname.classList.remove("hidden");
        event.preventDefault();
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
        event.preventDefault();
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
        var errortext = document.getElementById("error-text-email");
        username.classList.remove("hidden");
        event.preventDefault();
    }
    else
    {
        username.classList.remove("errorborder");
        var errortext = document.getElementById("error-text-email");
        errortext.classList.add("hidden");
    }
    if(!validatePWD(password.value))
    {
        password.classList.add("errorborder");
        var errortext = document.getElementById("error-text-password");
        password.classList.remove("hidden");
        event.preventDefault();
    }
    else
    {
        password.classList.remove("errorborder");
        var errortext = document.getElementById("error-text-password");
        errortext.classList.add("hidden");
    }
    if(password.value!== password2.value)
    {
        password2.classList.add("errorborder");
        var errortext = document.getElementById("error-text-repassword");
        password2.classList.remove("hidden");
        event.preventDefault();
    }
    else
    {
        password2.classList.remove("errorborder");
        var errortext = document.getElementById("error-text-repassword");
        errortext.classList.add("hidden");
    }
    if(!formisvalid===true)
    {
    
      console.log("Validation successful");
    }
}