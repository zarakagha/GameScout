<!DOCTYPE html>
<html>

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GameScout</title>
    <link rel="stylesheet" href="../css/style.css"/> 
</head>

<body>
    <div id="container">
        <header>
            <h1>SignUp Page</h1>

        </header>
        
            <hr class="line">
    
        <main id="main-center">
            <div class="container">
            <form class="signup-form" action="mainpage.php" method="post">
                <p class="login">

                    <label for="name">First Name</label>
                    <input type="text" name="firstname" required size="15"><br>

                </p>
                <p class="login">
                
                    <label for="lastname">Last Name</label>
                    <input type="text" name="lastname"required size="15"> <br>
                    
                </p>
                <p class="login">
                    <label for="username">Username</label>
                    <input type="text" name="username"required size="15"> 
                </p>
                <p class="login">
    
                    <label for="password">Password</label>
                    <input type="password" name="password"required size="15"><br>

                </p>
                <p class="login">
                    <label for="repassword">Confirm Password</label>
                    <input type="password"  name="repassword"required size="15"> 

                </p>
                <p class="login">
                    <label for="birthday">Date of Birth</label><br>
                    <input type="date" name="birth">

                </p>

                <p class="login">
                   
                    <input type="submit" class="form-submit" value="Signup">
                </p>
            </form>
        </main>
        
    </div>
    <div class="footer">
        <a href="mainpage.php">Already have an Account?</a>
    </div>
</body>

</html>