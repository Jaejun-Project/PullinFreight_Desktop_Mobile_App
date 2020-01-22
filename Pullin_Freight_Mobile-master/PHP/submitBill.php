<?php
    require "DBConfig.php";
    
    // Connecting to MySQL Database.
    $con = mysqli_connect($HostName, $HostUser, $HostPass, $DatabaseName);
    
    // Getting the received JSON into $json variable.
    $json = file_get_contents('php://input');
    
    // decoding the received JSON and store into $obj variable.
    $obj = json_decode($json, true);
    
    // Populate Student name from JSON $obj array and store into $S_Name.
    $bill_number = $obj['bill_number'];
    $start_time = $obj['start_time'];
    $end_time = $obj['end_time'];
    $hours_loads = $obj['hours_loads'];
    $job_id = $obj['job_id'];
    $shipper_name = $obj['shipper_name'];
    $pay_type = $obj['pay_type'];
    $rate = $obj['rate'];
    $date = $obj['date'];
    $origin = $obj['origin'];
    $destination = $obj['destination'];
    $comments = $obj['comments'];
    $username = $obj['username'];
    $broker_name = $obj['broker_name'];


    $sql = "SELECT * FROM users
    WHERE username = '".$username."';";

    $results = $con->query($sql);

    if ($results == false) {
        $json = json_encode($con->error);
        echo $json ;
    }

    $row = $results->fetch_assoc();
    $user_id = $row['user_id'];

    // Creating SQL query and insert the record into MySQL database table.
    $sql_insert_bill = "
        INSERT INTO bill_of_ladings(date, bill_number, broker_name, shipper_name, user_name, rate_type, origin, destination, start_time, end_time, hours_loads, rate)
        VALUES('".$date."', '".$bill_number."', '".$broker_name."', '".$shipper_name."', '".$username. "', '".$pay_type."', '".$origin."', '".$destination."', '".$start_time."', '".$end_time."', '".$hours_loads."', '".$rate."');";
    if(mysqli_query($con, $sql_insert_bill)){
    }
    else{
        echo 'Error inserting into bill';
    }

    $sql_change_job_status = "
        UPDATE current_jobs
        SET status = 'completed'
        WHERE job_id = " . (int)$job_id;
    if (mysqli_query($con, $sql_change_job_status)) {

    }else {
        echo 'Error changing job status';
    }

    $sql_bill_id = "SELECT MAX(bill_id) AS recent_bill_id FROM bill_of_ladings;";
    $results = $con->query($sql_bill_id);
    if ($results == false) {
        echo $mysql->error;
        exit();
    }

    $row = $results->fetch_assoc();
    $bill_id = $row['recent_bill_id'];

    $sql_insert_job_link= "
        INSERT INTO job_link(user_id, bill_id) VALUES(".$user_id.",".$bill_id.");
    ";

    if(mysqli_query($con, $sql_insert_job_link)){
        $MSG = 'Bill of Lading is successfully submitted!' ;
        $json = json_encode($MSG);
        echo $json ;
    }
    else{
        $json = json_encode($con->error);
        echo $json ;
    }

    mysqli_close($con);
?>