<?php
    require "DBConfig.php";

    // Create connection
    $mysqli = mysqli_connect($HostName, $HostUser, $HostPass, $DatabaseName);

    $json = file_get_contents('php://input');
    
    // decoding the received JSON and store into $obj variable.
    $obj = json_decode($json, true);
    
    if ($mysqli->connect_errno) {
        echo $mysqli->connect_error;
        exit();
    } 

    $username = $obj['username'];       

    $sql = "SELECT * FROM expirations
    WHERE driver_username = '".$username."';";

    $results = $mysqli->query($sql);

    if ($results == false) {
        echo $mysql->error;
        exit();
    }

    $json = NULL;
    $row[] = $results->fetch_assoc();
    $json = json_encode($row);

    echo $json;
    $mysqli->close();
?>