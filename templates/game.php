<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GameScout</title>
    <link rel="stylesheet" href="../css/style.css"/> 
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0&icon_names=search" /> 
    <link href="https://fonts.cdnfonts.com/css/motiva-sans" rel="stylesheet">
</head>

<body class="mainpage-body">
        <nav class="nav_bar">
            <div class="nav_div">
                <div class="logo"><a href="mainpage.php">
                    <img src="../images/GameScout-logo.png" alt=""> </a></div>
                    <div class="search">
                        <span class="material-symbols-outlined">search</span>
                        <input class="input-search" type="search" placeholder="Search for Games">
                    </div>
                <ul>
                    <li>
                        <div class="dropdown">
                            <a class="drop-button">
                                <img class="navdiv-icon" src="../images/person.png" alt="">
                            </a>
                            <div class="dropdown-content">
                                <a href="login.php">Log In</a>
                                <a href="signup.php">Sign Up</a>
                            </div>
                        </div>
                    </li>
                    <li><a href=""><img class="navdiv-icon" src="../images/heart.png" alt=""></a></li>
                    <li><a href=""><img class="navdiv-icon" src="../images/Logout.png" alt=""></a></li>
                </ul>
            </div>
        </nav>

        <div class="game-banner" style="background-image: url(../images/Game-Wallpapers/Doom.jpg)"></div>
        <div class="game-text">
            <div class="split-container">
                <div class="split-left">
                    <img src="../images/Game-Cards/Doom.jpg" object-fit: contain; alt="">
                </div>
                <div class="split-right">
                    <h1 style="font-size:50px">Game Title</h1>
                    <br> Game Descriptions<br>
                    <table >
                        <tr>
                            <td>Genre</td>
                            <td>Shooter</td>
                        </tr>
                        <tr>
                            <td>Release Date</td>
                            <td>May 13, 2016</td>
                        </tr>
                        <tr>
                            <td>Rating</td>
                            <td>9/10</td>
                        </tr>
                    </table>
                    <table>
                        <tr>
                            <th style="font-size:25px">Store</th>
                            <th style="font-size:25px">Cost</th>
                        </tr>
                        <tr>
                            <td><a href="https://store.playstation.com/en-ca/pages/latest" target="_blank">Playstation</a></td>
                            <td>$19.99</td>
                        </tr>
                        <tr>
                            <td><a href="https://www.microsoft.com/en-ca/store/games" target="_blank">Microsoft</a></td>
                            <td>$19.99</td>
                        </tr>
                        <tr>
                            <td><a href="https://www.nintendo.com/en-ca/store/games" target="_blank">Nintendo</a></td>
                            <td>$19.99</td>
                        </tr>
                        <tr>
                            <td><a href="https://store.steampowered.com/" target="_blank">Steam</a></td>
                            <td>$19.99</td>
                        </tr>
                    </table>
                    <button class="game-btn">Add to Wishlist</button>
                </div>
            </div>
        </div>
        
        <div class="footer">
            <div class="footerColumn1">
                <h3>Other Game Stores</h3>
                <a href="https://store.playstation.com/en-ca/pages/latest?gad_source=1&gclid=EAIaIQobChMIi8qlrYvRiwMVrAytBh33ZAicEAAYASAAEgJ9CPD_BwE&gclsrc=aw.ds" target="_blank">Playstation</a>
                <a href="https://www.microsoft.com/en-ca/store/games" target="_blank">Microsoft</a>
                <a href="https://www.nintendo.com/en-ca/store/games/?utm_source=sw&utm_medium=pdpd&utm_id=C1090-01&utm_campaign=C1090-01&gad_source=1&gclid=EAIaIQobChMI1Oqb3IvRiwMVY83CBB0YjALfEAAYASAAEgJg5fD_BwE&gclsrc=aw.ds" target="_blank">Nintendo</a>
                <a href="https://store.steampowered.com/" target="_blank">Steam</a>
            </div>
            <div class="footerColumn2">
                <h3>Creators</h3>
                <a href="">Snaoll</a>
                <a href="">Ordnary45</a>
                <a href="">zarakagha</a>
            </div>
        </div>
</body>

</html>