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
    
    $sql_tz = "SET time_zone = 'America/Los_Angeles';";
    $mysqli->query($sql_tz);

    $sql = "SELECT job_id, broker_name, shipper_name, current_jobs.user_name, start_date, start_time, pay_type, rate, origin, destination, comments, status FROM current_jobs
    JOIN users
        ON users.username = current_jobs.user_name
    WHERE user_name = '".$username."'
    AND start_date > DATE(NOW()) AND status <> 'declined' status <> 'completed'
    ORDER by start_date, start_time;";
    $results = $mysqli->query($sql);

    // var_dump($results);

    $json_results = json_encode('');
    if ($results->num_rows > 0) {
        while($row[] = $results->fetch_assoc()) {
            $json_results = json_encode($row);
        }
    }
    
    echo $json_results;
    $mysqli->close();  
?>