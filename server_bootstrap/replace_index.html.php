<!DOCTYPE html>
<html>

<head>
    <title>DS Oulu 2019-2020</title>
    <h2> This is the Git-powered distributed system for file sharing. Welcome, Stranger! </h2>
</head>

<body>

    <?php
echo "<h2>PHP is Fun!</h2>";
echo "Hello world!<br>";
echo "I'm about to learn PHP!<br>";
echo "This ", "string ", "was ", "made ", "with multiple parameters.";
?>

    <!-- 1. create new repo  -->
    <h4>Create New Repository:</h4>
    <form name='create_repo' method='GET' action=''>
        Name: <input type='text' name='repo_name' placeholder='my_new_best_repo' /></br>
        <input type='submit' value='Create' />
    </form>
    </br>

    <!-- 2. delete old repo  -->
    <h4>Delete Existing Repository:</h4>
    <form name='delete_repo' method='GET' action=''>
        Name: <input type='text' name='repo_name' placeholder='my_old_worst_repo' /></br>
        <input type='submit' value='Delete' />
    </form>
    </br>

    <!-- 3. register user  -->
    <h4>Register New User:</h4>
    <form name='register' method='GET' action=''>
        Name: <input type='text' name='user_name' placeholder='my_name' /></br>
        Password: <input type='password' name='user_pwd' /></br>
        <input type='submit' value='Register' />
    </form>
    </br>
</body>

</html>