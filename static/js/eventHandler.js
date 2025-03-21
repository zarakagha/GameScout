//function to check regex on the first name
function validatefname(fname) {
	let nameRegEx = /^[a-zA-Z]+$/; //allows only capital and lowercase letters

	if (nameRegEx.test(fname))//tests to see if input matches the regex requirments
		return true;
	else
		return false;
}
//function to check regex on the last name
function validatelname(lname) {
    let nameRegEx = /^[a-zA-Z]+$/;
    
    if (nameRegEx.test(lname))//tests to see if input matches the regex requirments
        return true;
   
    else
        return false;
}
//function to check regex on the password
function validatePWD(pwd) {
    let pwdRegEx =/^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z\d\W_]{8,}$/;  //regex for a password that requires a capital and a number but allows special chars with a minimum requirment of 8 chars
	if (pwdRegEx.test(pwd))//tests to see if input matches the regex requirments
		return true;
	else
		return false;
}
//function to check regex on the first name
function validateUsername(username) {
    let usernameRegEx = /^[a-zA-Z0-9\-_.]{5,12}$/;//variable with the regex of a username that is letters and numbers with the length between 5 to 12
        if (usernameRegEx.test(username)) //tests to see if input matches the regex requirments
            return true;
        else
            return false;
}
//function to check regex on the email
function validateEmail(email) {
    let emailRegEx = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;// variable with the regex of a valid email
        if (emailRegEx.test(email))
            return true;
        else
            return false;
}

function validateLogin(event) //function the validates frontend input with on screen error handling 
{
    console.log("validateLogin called");
    let username =document.getElementById('username'); //gets username from the username id textbox in login.html
    let password =document.getElementById('password'); //gets password from the password id textbox in login.html
    let formIsValid = true;

    if(!validateUsername(username.value)) //calls regex validator for  username
    {
      username.classList.add("errorborder"); 
      var errortext = document.getElementById("error-text-username"); //gets the username error
      errortext.classList.remove("hidden"); //displays error
      formIsValid = false; 
    }
    else
    {
      username.classList.remove("errorborder");
      var errortext = document.getElementById("error-text-username"); //gets the username error
		  errortext.classList.add("hidden"); //hides error
        
    }
    if(!validatePWD(password.value)) //calls regex validator for password
    {
        password.classList.add("errorborder");
        var errortext = document.getElementById("error-text-password"); //gets password error
        errortext.classList.remove("hidden"); //displays password error
        formIsValid = false;
       
    }
    else
    {
        password.classList.remove("errorborder");
        var errortext = document.getElementById("error-text-password"); //gets password error
        errortext.classList.add("hidden"); //hides password error
        
    }
    //checks to see if any input is false
    if (!formIsValid) {
        event.preventDefault(); 
    }
}
function validateSignup(event)  
{

    
    let fname =document.getElementById('firstname');//gets firstname from the firstname id textbox in signup.html
    let lname =document.getElementById('lastname');//gets lastname from the lastname id textbox in signup.html
    let username =document.getElementById('username');//gets username from the username id textbox in signup.html
    let email = document.getElementById('email');//gets email from the email id textbox in signup.html
    let password =document.getElementById('password');//gets password from the password id textbox in signup.html
    let formIsValid = true;

    if(!validatefname(fname.value))//calls regex validator for firstname
    {
        fname.classList.add("errorborder");
        var errortext = document.getElementById("error-text-fname");//gets firstname error
        errortext.classList.remove("hidden");//displays firstname error
        formIsValid = false;
    }
    else
    {
        fname.classList.remove("errorborder");
        var errortext = document.getElementById("error-text-fname");//gets firstname error
        errortext.classList.add("hidden");//hides firstname error
    }
    if(!validatelname(lname.value))//calls regex validator for lastname
    {
        lname.classList.add("errorborder");
        var errortext = document.getElementById("error-text-lname");//gets lastname error
        errortext.classList.remove("hidden");//displays lastname error
        formIsValid = false;
    }
    else
    {
        lname.classList.remove("errorborder");
        var errortext = document.getElementById("error-text-lname");//gets lastname error
        errortext.classList.add("hidden");//hides lastname error
    }
    if(!validateUsername(username.value))//calls regex validator for username
    {
        username.classList.add("errorborder");
        var errortext = document.getElementById("error-text-username");//gets username error
        errortext.classList.remove("hidden");//displays username error
        formIsValid = false;
    }
    else
    {
        username.classList.remove("errorborder");
        var errortext = document.getElementById("error-text-username");//gets username error
        errortext.classList.add("hidden");//hides username error
    }
    if(!validateEmail(email.value))//calls regex validator for email
    {
        email.classList.add("errorborder");
        var errortext = document.getElementById("error-text-email");//gets email error
        errortext.classList.remove("hidden");//displays email error
        formIsValid = false;
    }
    else
    {
        email.classList.remove("errorborder");
        var errortext = document.getElementById("error-text-email");//gets email error
        errortext.classList.add("hidden");//hides email error
    }
    if(!validatePWD(password.value))//calls regex validator for password
    {
        password.classList.add("errorborder");
        var errortext = document.getElementById("error-text-password");//gets password error
        errortext.classList.remove("hidden");//displays password error
        formIsValid = false;
    }
    else
    {
        password.classList.remove("errorborder");
        var errortext = document.getElementById("error-text-password");//gets password error
        errortext.classList.add("hidden");//hides password error
    }
    //checks to see if any input is false
    if (!formIsValid) {
        
        event.preventDefault();
    }

}

// Function to filter table rows based on input value
function filterTable() {
    var input, filter, table, tr, td, i, txtValue;

    //Get the input value and convert to uppercase for comparison
    input = document.getElementById("myInput");
    filter = input.value.toUpperCase();

    //Get the table and rows
    table = document.getElementById("wishlistGames");
    tr = table.getElementsByTagName("tr");
  
    //Loop through all table rows, except first row (header)
    for (i = 0; i < tr.length; i++) {
      td = tr[i].getElementsByTagName("td")[1];
      if (td) {
        txtValue = td.textContent || td.innerText;
        if (txtValue.toUpperCase().indexOf(filter) > -1) {  //Id text matches the filter, display it, otherwise hide it
          tr[i].style.display = "";
        } else {
          tr[i].style.display = "none";
        }
      }
    }
}

// Function to sort table rows alphabetically
  function sortAlphabetically(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("wishlistGames");
    switching = true;
    dir = "asc"; 

    //Loop until no switching is needed
    while (switching) {   
      switching = false;
      rows = table.rows;

      //Loop through all table rows, except first row (header)
      for (i = 1; i < (rows.length - 1); i++) {
        shouldSwitch = false;

        //Get the current row and the next row
        x = rows[i].getElementsByTagName("TD")[n];
        y = rows[i + 1].getElementsByTagName("TD")[n];

        //Checks the two rows and switches them based on direction
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

      //If a switch is needed, switch the rows
      if (shouldSwitch) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        switchcount ++;      
      } else if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
  }

  // Function to sort table rows numerically based on the specified column
  function sortNumerically(n) {
    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.getElementById("wishlistGames");
    switching = true;
    dir = "asc"; 

    //Loop until no switching is needed
    while (switching) {
      switching = false;
      rows = table.rows;

      //Loop through all table rows, except first row (header)
      for (i = 1; i < (rows.length - 1); i++) {
        shouldSwitch = false;

        //Get the current row and the next row
        x = rows[i].getElementsByTagName("TD")[n];
        y = rows[i + 1].getElementsByTagName("TD")[n];

        //Checks the two rows and switches them based on direction
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

      //If a switch is needed, switch the rows
      if (shouldSwitch) {
        rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
        switching = true;
        switchcount ++;      
      } else if (switchcount == 0 && dir == "asc") {
        dir = "desc";
        switching = true;
      }
    }
}