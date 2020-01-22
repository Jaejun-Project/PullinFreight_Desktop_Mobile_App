<?php
    require "DBConfig.php";

    // Create connection
    $con = mysqli_connect($HostName, $HostUser, $HostPass, $DatabaseName);

    $json = file_get_contents('php://input');
    
    // decoding the received JSON and store into $obj variable.
    $obj = json_decode($json, true);
    
    if ($con->connect_errno) {
        echo $con->connect_error;
        exit();
    } 

    $username = $obj['username'];


    $sql = "SELECT * FROM bill_of_ladings
                JOIN job_link
                    ON bill_of_ladings.bill_id = job_link.bill_id
                JOIN users
                    ON job_link.user_id = users.user_id
            WHERE username = '".$username."';";

    $results = $con->query($sql);

    $json_results = $json_results = json_encode('');
    if ($results->num_rows > 0) {
        while($row[] = $results->fetch_assoc()) {
            $json_results = json_encode($row);
        }
    }

    echo $json_results;

    $con->close();
?>