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