<?php

require_once("db.php");

function test_input($data) {
    $data = trim($data);
    $data = stripslashes($data);
    $data = htmlspecialchars($data); //encodes
    return $data;
}

$fname = test_input($_POST["firstname"]);
$lname = test_input($_POST["lastname"]);
$uname = test_input($_POST["username"]);
$pwd = test_input($_POST["password"]);

$nameRegex = "/^[a-zA-Z]+$/";
$unameRegex = "/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/";
$passwordRegex = "/^.{8}$/";

if (!preg_match($nameRegex, $fname)) {
    $errors["fname"] = "Invalid First Name";
}
if (!preg_match($nameRegex, $lname)) {
    $errors["lname"] = "Invalid Last Name";
}
if (!preg_match($unameRegex, $uname)) {
    $errors["username"] = "Invalid Username";
}
if (!preg_match($passwordRegex, $pwd)) {
    $errors["password"] = "Invalid Password";
}

$target_file ="";

try {
    $db = new PDO($attr, $db_user, $db_pwd, $options);
} catch (PDOException $e) {
    throw new PDOException($e->getMessage(), (int)$e->getCode());
}
$query = "SELECT * FROM signup WHERE username = '$username'";

$result = $db->query($query);

$match =0;

$row = $result->fetch(\PDO::FETCH_ASSOC);
if($row == true) {
    $match=$row[0];
}
if($match)
{
    $errors["Account already exists"] = "username already exists";
}

if (empty($errors)) {

    $query = "INSERT INTO signup (first_name, last_name, username, password) VALUES ('$firstName', '$lastName', '$username', '$password')";
    $result = $db->exec($query);

    if (!$result) {
        $errors["Database Error:"] = "Cant create account";
    } 

       
        
      
    } 

if (!empty($errors)) {
    foreach($errors as $type => $message) {
        print("$type: $message \n<br />");
    }
}
?>
<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GameScout</title>
    <link rel="stylesheet" href="css/style.css"/> 
    <script src="js/eventHandlers.js"></script>
</head>

<body>
    <div id="container">
        <header>
            <h1>SignUp Page</h1>

        </header>
        
            <hr class="line">
    
        <main id="main-center">
            <div class="container">
            <form class="signup-form" id="signup-form" action="mainpage.php" method="post">
                <p class="signup">

                    <label for="firstname">First Name</label>
                    <input type="text" name="firstname"><br>
                    <p id="error-test-fname" class="error-text hidden">First name is invalid</p>
                </p>
                <p class="signup">
                
                    <label for="lastname">Last Name</label>
                    <input type="text" name="lastname"> <br>
                    <p id="error-test-lname" class="error-text hidden">Last name is invalid</p>
                </p>
                <p class="signup">
                    <label for="email">email</label>
                    <input type="text" name="email"> 
                    <p id="error-text-email" class="error-text hidden">Username is invalid. please enter an email</p>
                </p>
                <p class="signup">
    
                    <label for="password">Password</label>
                    <input type="password" name="password"><br>
                    <p id="error-text-password" class="error-text hidden">Passwords is invalid.</p>
                </p>
                <p class="signup">
                    <label for="repassword">Confirm Password</label>
                    <input type="password"  name="repassword"> 
                    <p id="error-text-repassword" class="error-text hidden">Passwords do not match</p>

                </p>
                <p class="signup">
                   
                    <input type="submit" class="form-submit" value="Signup">
                </p>
            </form>
        </main>
        
    </div>
    <div class="footer">
        <a href="mainpage.php">Already have an Account?</a>
    </div>
</body>
<script src="js/eventRegisterSignup.js"></script>
</html>