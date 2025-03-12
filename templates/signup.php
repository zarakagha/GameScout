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
    <link rel="stylesheet" href="../css/style.css"/> 
    <link href='https://unpkg.com/boxicons@2.1.4/css/boxicons.min.css' rel='stylesheet'>
    <script src="js/eventHandlers.js"></script>
</head>

<body id="signup-page" class="ID-body2">
    <div class="wrapper">
            <form action="">
            <div class="logo"><a href="mainpage.php">
                    <img src="../images/GameScout-logo.png" alt=""> 
                </a>
            </div>
            <h1>Sign Up</h1>
            <div class="input-box">
                <input type="text" placeholder="First Name" required>
                <i></i>
            </div>
            <div class="input-box">
                <input type="text" placeholder="Last Name" required>
                <i></i>
            </div>
            <div class="input-box">
                <input class="User" type="text" placeholder="Username" required>
                <i></i>
            </div>
            <div class="input-box">
                <input class="email" type="text" placeholder="Email" required>
                <i></i>
            </div>
            <div class="input-box">
                <input type="password" placeholder="Password" required>
                <i></i>
            </div>
            <button type="submit" class="btn">Sign Up</button>
            <div class="signup-link">
                <p>Already have an account? <a href="login.php">Login</a></p>
            </div>
            </form>
        </div>
</body>
<script src="js/eventRegisterSignup.js"></script>
</html>