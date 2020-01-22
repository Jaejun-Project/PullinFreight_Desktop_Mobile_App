<?php
    require "DBConfig.php";
    
    // Connecting to MySQL Database.
    $con = mysqli_connect($HostName, $HostUser, $HostPass, $DatabaseName);
    
    // Getting the received JSON into $json variable.
    $json = file_get_contents('php://input');
    
    // decoding the received JSON and store into $obj variable.
    $obj = json_decode($json, true);
    
    // Populate Student name from JSON $obj array and store into $S_Name.
    $username = $obj['username'];
    
    // Creating SQL query and insert the record into MySQL database table.
    $sql = "
        INSERT INTO users(username) VALUES ('".$username."');
    ";

    if(mysqli_query($con, $sql)){
        // If the record inserted successfully then show the message.
        $MSG = 'New User Successfully Inserted Into MySQL Database.' ;
        // Converting the message into JSON format.
        $json = json_encode($MSG);
        // Echo the message.
        echo $json ;
    }
    else{
        echo 'error inserting to users';
    }

    mysqli_close($con);
?>