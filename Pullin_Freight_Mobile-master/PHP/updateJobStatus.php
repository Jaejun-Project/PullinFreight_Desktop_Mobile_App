<?php
    require "DBConfig.php";
    
    // Connecting to MySQL Database.
    $con = mysqli_connect($HostName, $HostUser, $HostPass, $DatabaseName);
    
    // Getting the received JSON into $json variable.
    $json = file_get_contents('php://input');
    
    // decoding the received JSON and store into $obj variable.
    $obj = json_decode($json, true);
    
    // Populate Student name from JSON $obj array and store into $S_Name.
    $job_id = $obj['job_id'];
    $accept = $obj['accept'];
    $status = '';

    if ($accept) {
        $status = 'accepted';
    }else {
        $status = 'declined';
    }
    
    // Creating SQL query and insert the record into MySQL database table.
    $sql = "UPDATE current_jobs
        SET status = '" . $status . "'
        WHERE job_id = '". $job_id ."';";

    if (mysqli_query($con, $sql)) {
        $MSG = 'Job status successfully updated!' ;
        // Converting the message into JSON format.
        $json = json_encode($MSG);
        // Echo the message.
        echo $json ;
    } else {
        $json = json_encode($con->error);
        // Echo the message.
        echo $json ;
    }
 


    mysqli_close($con);
?> 