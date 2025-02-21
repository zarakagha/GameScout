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