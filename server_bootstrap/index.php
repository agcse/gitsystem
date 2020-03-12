<!DOCTYPE html>
<html>

<head>
    <title>DS Oulu 2019-2020</title>
    <h2> This is the Git-powered distributed system for file sharing. Welcome, Stranger! </h2>
    <style>
    td, tr {
        padding: 10px;
        border-radius: 5px;
        background-color: #fff;
        text-align: center;
    }
    </style>

    <?php
    function startsWith($haystack, $needle)
    {
        $length = strlen($needle);
        return (substr($haystack, 0, $length) === $needle);
    }

    function endsWith($haystack, $needle)
    {
        $length = strlen($needle);
        if ($length == 0) {
            return true;
        }

        return (substr($haystack, -$length) === $needle);
    }
    ?>
</head>

<body>
    <?php
    // extract git repositories:
    $paths = scandir('/var/www/html/git/');
    $git_repos = array();
    foreach ($paths as $path) {
        if (endsWith($path, '.git')) {
            $git_repos[] = $path;
        }
    }

    // handle form submit requests:
    if (isset($_POST['register_user'])) {
        $cmd = sprintf('../git_tools/server_tools/register_user.sh %s %s', $_POST['user_name'], $_POST['user_pwd']);
        exec($cmd);
        header('Location: index.php');
        exit();
    }

    if (isset($_POST['create_repo'])) {
        $cmd = sprintf('../git_tools/server_tools/create_repo.sh %s.git', $_POST['repo_name']);
        exec($cmd);
        header('Location: index.php');
        exit();
    }

    if (isset($_POST['delete_repo'])) {
        $cmd = sprintf('../git_tools/server_tools/delete_repo.sh %s', $_POST['repo_name']);
        exec($cmd);
        header('Location: index.php');
        exit();
    }
    ?>

    <table>
    <td> <!-- register user  -->
    <h4>Register New User:</h4>
    <form name='register' method='POST' action=''>
        Name: <input type='text' name='user_name' placeholder='my_name' /></br>
        Password: <input type='password' name='user_pwd' /></br>
        <input type='submit' name='register_user' value='Register' />
    </form>
    </td>

    <td> <!-- create new repo  -->
    <h4>Create New Repository:</h4>
    <form name='create_repo' method='POST' action=''>
        Name: <input type='text' name='repo_name' placeholder='my_new_best_repo' /></br>
        <input type='submit' name='create_repo' value='Create' />
    </form>
    </td>

    <td> <!-- delete old repo  -->
    <h4>Delete Existing Repository:</h4>
        <table>
        <?php foreach ($git_repos as $repo) {?>
        <tr>
        <form name='delete_repo' method='POST' action=''>
            Name: <?php print($repo); ?></br>
            <input type='hidden' name='repo_name' value='<?php echo htmlspecialchars($repo); ?>'>
            Action: <input type='submit' name='delete_repo' value='Delete' /></br>
        </form>
        </br>
        </tr>
        <?php } ?>
        </table>
    </td>
    <table>
</body>

</html>