
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
    let pwdRegEx =/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d\W_]{8,}$/;
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
        errortext.classList.remove("hidden");
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
        errortext.classList.remove("hidden");
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
        errortext.classList.remove("hidden");
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
        errortext.classList.remove("hidden");
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
        errortext.classList.remove("hidden");
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

function filterTable() {
    var input, filter, table, tr, td, i, txtValue;
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();
    table = document.getElementById("wishlistGames");
    tr = table.getElementsByTagName("tr");
  
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[1];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
}

  function sortAlphabetically(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("wishlistGames");
    switching = true;
    dir = "asc"; 
    while (switching) {
      switching = false;
      rows = table.rows;
      for (i = 1; i < (rows.length - 1); i++) {
        shouldSwitch = false;
        x = rows[i].getElementsByTagName("TD")[n];
        y = rows[i + 1].getElementsByTagName("TD")[n];
        if (dir == "asc") {
          if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
            shouldSwitch= true;
            break;
          }
        } else if (dir == "desc") {
          if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
            shouldSwitch = true;
            break;
          }
        }
      }
      if (shouldSwitch) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        switchcount ++;      
      } else {
        if (switchcount == 0 && dir == "asc") {
          dir = "desc";
          switching = true;
        }
      }
    }
  }

  function sortNumerically(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("wishlistGames");
    switching = true;
    dir = "asc"; 
    while (switching) {
      switching = false;
      rows = table.rows;
      for (i = 1; i < (rows.length - 1); i++) {
        shouldSwitch = false;
        x = rows[i].getElementsByTagName("TD")[n];
        y = rows[i + 1].getElementsByTagName("TD")[n];
        if (dir == "asc") {
          if (parseFloat(x.innerHTML) > parseFloat(y.innerHTML)) {
            shouldSwitch = true;
            break;
          }
        } else if (dir == "desc") {
          if (parseFloat(x.innerHTML) < parseFloat(y.innerHTML)) {
            shouldSwitch = true;
            break;
          }
        }
      }
      if (shouldSwitch) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        switchcount ++;      
      } else {
        if (switchcount == 0 && dir == "asc") {
          dir = "desc";
          switching = true;
        }
      }
    }
}