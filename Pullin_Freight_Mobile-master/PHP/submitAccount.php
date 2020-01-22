<?php
    require "DBConfig.php";
    
    // Connecting to MySQL Database.
    $con = mysqli_connect($HostName, $HostUser, $HostPass, $DatabaseName);
    
    // Getting the received JSON into $json variable.
    $json = file_get_contents('php://input');
    
    // decoding the received JSON and store into $obj variable.
    $obj = json_decode($json, true);
    
    // Populate Student name from JSON $obj array and store into $S_Name.
    $fname = $obj['fname'];
    $lname = $obj['lname'];
    $email = $obj['email'];
    $phone = $obj['phone'];
    $address = $obj['address'];
    $number = $obj['number'];
    $expire = $obj['expire'];

    $username = $obj['username'];    
    
    // Creating SQL query and insert the record into MySQL database table.
    $sql = "UPDATE users
        SET first_name = '".$fname."', 
        last_name='".$lname."', 
        phone_number='".$phone."', 
        email='".$email."', 
        address='".$address."', 
        license_number='".$number."',
        license_expire= '".$expire."'
        WHERE username = '".$username."';
    ";

    if (mysqli_query($con, $sql)) {
        $MSG = 'Account successfully updated!' ;
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