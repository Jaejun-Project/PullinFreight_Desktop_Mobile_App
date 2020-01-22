SELECT * FROM bill_of_ladings;

SELECT MAX(bill_id) AS recent_bill_id FROM bill_of_ladings;

SELECT LAST_INSERT_ID() FROM bill_of_ladings;

/* stores the currently available jobs */
SELECT * FROM current_jobs;

/*job_link pairs the users and jobs*/
SELECT * FROM job_link;

SELECT * FROM shippers;

SELECT * FROM users;

SELECT * FROM bill_of_ladings 
WHERE user_name = 'max';

SELECT job_id, shipper_name, current_jobs.user_name, start_date, start_time, pay_type, rate, origin, destination, comments FROM current_jobs
    JOIN users
        ON users.username = current_jobs.user_name
WHERE user_name = 'max';

SELECT job_id, shipper_name, current_jobs.user_name, start_date, start_time, pay_type, rate, origin, destination, comments FROM current_jobs
    JOIN users
        ON users.username = current_jobs.user_name
    WHERE user_name = 'max' AND start_date >= DATE(NOW());

SELECT job_id, shipper_name, current_jobs.user_name, start_date, start_time, pay_type, rate, origin, destination, comments FROM current_jobs
    JOIN users
        ON users.username = current_jobs.user_name
WHERE user_name = 'max'
    AND start_date >= DATE(NOW());
    
SELECT DATE(NOW());
    
SET GLOBAL time_zone = 'America/Los_Angeles';
    
SELECT NOW();


SET time_zone = 'America/Los_Angeles';
    

/* INSERT */
INSERT INTO current_jobs(shipper_name, user_name, start_date, start_time, pay_type, rate, origin, destination, comments)
VALUES ('Anytime', 'max', '2018-11-13', '17:00', 'Per Hour', 5, 'Lorenzo', 'USC', 'Hello World');


INSERT INTO current_jobs(shipper_name, user_name, start_date, start_time, pay_type, rate, origin, destination, comments)
VALUES ('Nikias', 'max', '2018-12-19', '00:12', 'Per Load', 10, 'USC', 'Lorenzo', 'Hello World fron Pointy thing');

INSERT INTO current_jobs(job_id, shipper_id, type, start_date, start_time, end_time, origin, destination, status)
VALUES (2, 3, 'Earth loading again', '2018-10-31', '00:00', '24:00', 'USC', 'LAX', 3);

-- "Per Hour" OR "Per Load" 
INSERT INTO bill_of_ladings(date, bill_number, shipper_name, user_name, rate, rate_type, origin, destination, loads, start_time, end_time, hours_worked)
	VALUES ('2018-5-12', '1234567', 'Max Nikias', 'max', 12, 'Per Hour', 'LAX', 'USC', 5, '8:45', '16:30', 0);
    
INSERT INTO bill_of_ladings(date, bill_number, shipper_name, user_name, rate, rate_type, origin, destination, loads, start_time, end_time, hours_worked)
	VALUES ('2018-9-10', '213333', 'Max Nikias', 'max', 12, 'Per Hour', 'LAX', 'USC', 5, '8:45', '16:30', 0);
    
INSERT INTO bill_of_ladings(date, bill_number, shipper_name, user_name, rate, rate_type, origin, destination, loads, start_time, end_time, hours_worked)
	VALUES ('2018-3-25', '22323113', 'Max Nikias', 'aarav', 12, 'Per Load', 'LAX', 'Lorenzo', 5, '8:45', '16:30', 0);
    
INSERT INTO bill_of_ladings(date, bill_number, shipper_name, user_name, rate, rate_type, origin, destination, loads, start_time, end_time, hours_worked)
	VALUES ('2018-12-30-6', '12323', 'Max Nikias', 'max', 12, 'Per Hour', 'Lattc', 'USC', 10, '8:45', '16:30', 0);
    
    
UPDATE users
SET first_name = 'dfsf', last_name='dfsdf', phone_number='13123', email='dsfsdf', address='sdfdsfd', license_number='sdfsdfsf'
WHERE username = 'aarav';

SELECT job_id, shipper_name, current_jobs.user_name, start_date, start_time, pay_type, rate, origin, destination, comments FROM current_jobs
    JOIN users
        ON users.username = current_jobs.user_name
    WHERE user_name = 'max';

    
INSERT INTO job_link(user_id, bill_id)
VALUES(14, 37);

DELETE FROM current_jobs WHERE user_name = 'max';

DELETE FROM job_link WHERE user_id = 15;

DELETE FROM bill_of_ladings WHERE user_name = 'max';

DELETE FROM current_jobs WHERE user_name= 'max';