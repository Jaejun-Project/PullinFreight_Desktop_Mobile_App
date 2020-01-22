import mysql.connector
from mysql.connector import errorcode
from user import User
from shipper import Shipper
from broker import Broker
from current_jobs import Current_job
from bill_of_lading import BOL
from datetime import datetime, timedelta

class Database:

    config = {
        'user': '',
        'password': '',
        'host': '',
        'database': '',
        'raise_on_warnings': True
    }

    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    def __init__(self):
        self.users_list = []
        self.shippers_list = []
        self.current_jobs_list = []


    def get_usernames(self):
        query = ("SELECT username FROM users ORDER BY username ASC")
        self.cursor.execute(query)

        username_list = []

        for username in self.cursor:
            username_list.append(str(username[0]))

        return username_list

    def get_users(self):
        query = "SELECT users.*, expirations.drug_test, expirations.carb, expirations.mpc, expirations.dir From users join  expirations ON users.username = expirations.driver_username"
        self.cursor.execute(query)
        self.users_list = []
        for users in self.cursor:
            user = User(users[0], users[1], users[2], users[3], users[4], users[5], users[6], users[7], users[8], users[9], users[10], users[11], users[12], users[13], users[14])
            self.users_list.append(user)
        return self.users_list
    def get_user(self, user_id):
        query = "SELECT users.*, expirations.drug_test, expirations.carb, expirations.mpc, expirations.dir From users join  expirations ON users.username = expirations.driver_username WHERE users.user_id = %s"
        val = (user_id,)
        self.cursor.execute(query, val)
        for users in self.cursor:
            user = User(users[0], users[1], users[2], users[3], users[4], users[5], users[6], users[7], users[8], users[9], users[10], users[11], users[12], users[13], users[14])
            return user


    def add_user(self, first_name, last_name, username, phone_number, email, address, license_number, license_expire, insurance_expire, drug_test_expire, carb_expire, mpc_expire, dir_expire, special_expire, comment):
        query = "INSERT INTO users (`first_name`, `last_name`, `username`, `phone_number`, `email`, `address`, `license_number`, `license_expire`, `special_expire`, `comment`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (first_name, last_name, username, phone_number, email, address, license_number, license_expire, special_expire, comment)
        self.cursor.execute(query, val)
        self.cnx.commit()
        query = "INSERT INTO expirations (`driver_username` ,`insurance`, `drug_test`, `carb`, `mpc`, `dir`) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (username, insurance_expire, drug_test_expire, carb_expire, mpc_expire, dir_expire)
        self.cursor.execute(query, val)
        self.cnx.commit()
        return


    def update_user(self, user_id, username, first_name, last_name, phone_number, email, address, insurance_expire, drug_test_expire, carb_expire, mpc_expire, dir_expire, special_expire, comment, license_number, license_expire):
        query = "UPDATE users SET first_name = %s, last_name = %s, phone_number = %s, email = %s, address = %s, special_expire = %s, comment = %s, license_number = %s, license_expire =%s WHERE user_id = %s"
        val = (first_name, last_name, phone_number, email, address, special_expire, comment, license_number, license_expire, user_id)
        self.cursor.execute(query, val)
        self.cnx.commit()
        query = "UPDATE expirations SET insurance = %s, drug_test = %s, carb = %s, mpc = %s, dir = %s WHERE driver_username = %s"
        val = (insurance_expire, drug_test_expire, carb_expire, mpc_expire, dir_expire, username)
        self.cursor.execute(query, val)
        self.cnx.commit()
        return

    def delete_user(self, user_id, username):
        query = "DELETE FROM users WHERE user_id = %s"
        val = (user_id, )
        self.cursor.execute(query, val)
        self.cnx.commit()
        query = "DELETE FROM expirations WHERE driver_username = %s"
        val = (username, )
        self.cursor.execute(query, val)
        self.cnx.commit()
        return

    def get_shippernames(self):
        query = ("SELECT name FROM shippers ORDER BY name ASC")
        self.cursor.execute(query)

        shippername_list = []

        for shipper_name in self.cursor:
            shippername_list.append(str(shipper_name[0]))

        return shippername_list

    def get_shippers(self):
        query = ("SELECT * FROM shippers ORDER BY name ASC")
        self.cursor.execute(query)
        self.shippers_list = []

        for shippers in self.cursor:
            shipper = Shipper(shippers[0], shippers[1], shippers[2], shippers[3], shippers[4], shippers[5])
            self.shippers_list.append(shipper)

        return self.shippers_list

    def update_shipper(self, shipper_id, name, address, origin, destination, comments):
        query = "UPDATE shippers SET name= %s, address= %s, origin=%s, destination=%s, comments=%s WHERE shipper_id = %s"
        val = (name, address, origin, destination, comments, shipper_id)
        self.cursor.execute(query, val)
        self.cnx.commit()
        return

    def get_shipper(self, shipper_id):
        query = "SELECT * FROM shippers WHERE shipper_id = %s"
        val = (shipper_id, )
        self.cursor.execute(query, val)
        for shippers in self.cursor:
            shipper = Shipper(shippers[0], shippers[1], shippers[2], shippers[3], shippers[4], shippers[5])
            self.shippers_list.append(shipper)
            return shipper

    def add_shipper(self, name, address, origin, destination, comments):
        query = "INSERT INTO shippers (name, address, origin, destination, comments) VALUES (%s, %s, %s, %s, %s)"
        val = (name, address, origin, destination, comments)
        self.cursor.execute(query, val)
        self.cnx.commit()

    def delete_shipper(self, shipper_id):
        query = "DELETE FROM shippers WHERE shipper_id = %s"
        val = (shipper_id, )
        self.cursor.execute(query, val)
        self.cnx.commit()
        return

    def get_current_jobs(self):
        query = ("SELECT * FROM current_jobs ORDER BY start_date DESC")
        self.cursor.execute(query)
        current_jobs_list = []

        for jobs in self.cursor:
            job = Current_job(jobs[0], jobs[1], jobs[2], jobs[3], jobs[4], jobs[5], jobs[6], jobs[7], jobs[8], jobs[9], jobs[10], jobs[11])
            current_jobs_list.append(job)

        return current_jobs_list

    def get_current_job_by_id(self, job_id):
        query = "SELECT * FROM current_jobs WHERE job_id = %s"
        val = (job_id,)
        self.cursor.execute(query, val)

        for jobs in self.cursor:
            job = Current_job(jobs[0], jobs[1], jobs[2], jobs[3], jobs[4], jobs[5], jobs[6], jobs[7], jobs[8], jobs[9], jobs[10], jobs[11])

        return job

    def add_job(self, shipper_name, broker_name, user_name, date, time, pay_type, rate, origin, destination, comments):
        query = "INSERT INTO current_jobs (`shipper_name`,`broker_name`, `user_name`, `start_date`, `start_time`, `pay_type`, `rate`, `origin`, `destination`, `comments`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (shipper_name, broker_name, user_name, date, time, pay_type, rate, origin, destination, comments)
        self.cursor.execute(query, val)
        self.cnx.commit()
        return

    def edit_job(self, shipper_name, broker_name, user_name, date, time, pay_type, rate, origin, destination, comments, job_id):
        query = "UPDATE current_jobs SET status = 'pending', `shipper_name`=%s, `broker_name`=%s, `user_name`=%s, `start_date`=%s, `start_time`=%s, `pay_type`=%s, `rate`=%s, `origin`=%s, `destination`=%s, `comments`=%s WHERE job_id =%s "
        val = (shipper_name, broker_name, user_name, date, time, pay_type, rate, origin, destination, comments, job_id)
        self.cursor.execute(query, val)
        self.cnx.commit()
        return

    def delete_job(self, job_id):
        query = "DELETE FROM current_jobs WHERE job_id = %s"
        val = (job_id,)
        self.cursor.execute(query, val)
        self.cnx.commit()
        return

    def get_bols(self):
        query = "SELECT * FROM bill_of_ladings ORDER BY bill_id DESC"
        self.cursor.execute(query)
        bols = []

        for bill in self.cursor:
            bol = BOL(bill[0], bill[1], bill[2], bill[3], bill[4], bill[5], bill[6], bill[7], bill[8], bill[9], bill[10], bill[11],bill[12])
            bols.append(bol)

        return bols

    def edit_bol(self, bill_id, date, bill_number,broker_name ,shipper_name, user_name, rate_type, origin, destination, start_time, end_time, hours_loads, rate):
        query = "UPDATE bill_of_ladings SET `date`=%s, `bill_number`=%s, `broker_name`=%s, `shipper_name`=%s, `user_name`=%s, `rate_type`=%s, `origin`=%s, `destination`=%s, `start_time`=%s, `end_time`=%s, `hours_loads`=%s, `rate`=%s WHERE bill_id =%s"
        val = (date, bill_number, broker_name, shipper_name, user_name, rate_type, origin, destination, start_time, end_time, hours_loads, rate, bill_id)
        self.cursor.execute(query, val)
        self.cnx.commit()
        return

    def add_bol(self, date, bill_number, broker_name ,shipper_name, user_name, rate_type, origin, destination, start_time, end_time, hours_loads, rate):

        user_id = self.get_user_id(user_name)

        query = "INSERT INTO bill_of_ladings (`date`, `bill_number`,`broker_name`, `shipper_name`, `user_name`, `rate_type`, `origin`, `destination`, `start_time`, `end_time`, `hours_loads`, `rate`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (date, bill_number, broker_name, shipper_name, user_name, rate_type, origin, destination, start_time, end_time, hours_loads, rate)
        self.cursor.execute(query, val)
        self.cnx.commit()

        bill_id = self.get_last_bill_id()

        query = "INSERT INTO job_link (`user_id`, `bill_id`) VALUES (%s, %s)"
        val = (user_id, bill_id)
        self.cursor.execute(query, val)
        self.cnx.commit()
        return

    def get_last_bill_id(self):
        query = "SELECT MAX(bill_id) FROM bill_of_ladings"
        self.cursor.execute(query)

        for id in self.cursor:
            bill_id = id[0]
            return bill_id

    def get_user_id(self, username):
        query = "SELECT user_id FROM users WHERE username = %s"
        val = (username, )
        self.cursor.execute(query, val)

        for id in self.cursor:
            user_id = id[0]
            return user_id

    def delete_bol(self, bill_id):
        query = "DELETE FROM job_link WHERE bill_id = %s"
        val = (bill_id,)
        self.cursor.execute(query, val)
        self.cnx.commit()

        query = "DELETE FROM bill_of_ladings WHERE bill_id = %s"
        val = (bill_id,)
        self.cursor.execute(query, val)
        self.cnx.commit()
        return

    def get_bol_invoiced(self, broker_name, from_date, to_date):
        query = "SELECT * FROM bill_of_ladings WHERE broker_name = %s AND (date >= %s AND date <=%s) ORDER BY date ASC"
        val = (broker_name, from_date, to_date)
        self.cursor.execute(query, val)
        bols = []

        for bill in self.cursor:
            bol = BOL(bill[0], bill[1], bill[2], bill[3], bill[4], bill[5], bill[6], bill[7], bill[8], bill[9],
                      bill[10], bill[11], bill[12])
            bols.append(bol)

        return bols

    def get_driver_logs(self, driver_username, from_date, to_date):
        query = "SELECT * FROM bill_of_ladings WHERE user_name = %s AND (date >= %s AND date <=%s) ORDER BY date ASC"
        val = (driver_username, from_date, to_date)
        self.cursor.execute(query, val)
        bols = []

        for bill in self.cursor:
            bol = BOL(bill[0], bill[1], bill[2], bill[3], bill[4], bill[5], bill[6], bill[7], bill[8], bill[9],
                      bill[10], bill[11], bill[12])
            bols.append(bol)

        return bols

    def get_brokernames(self):
        query = ("SELECT broker_name FROM brokers ORDER BY broker_name ASC")
        self.cursor.execute(query)

        brokername_list = []

        for broker_name in self.cursor:
            brokername_list.append(str(broker_name[0]))

        return brokername_list

    def get_brokers(self):
        query = ("SELECT * FROM brokers ORDER BY broker_name ASC")
        self.cursor.execute(query)
        self.brokers_list = []

        for brokers in self.cursor:
            broker = Broker(brokers[0], brokers[1], brokers[2])
            self.brokers_list.append(broker)

        return self.brokers_list

    def update_broker(self, broker_id, name, address):
        query = "UPDATE brokers SET broker_name= %s, address= %s WHERE broker_id = %s"
        val = (name, address, broker_id)
        self.cursor.execute(query, val)
        self.cnx.commit()
        return

    def get_broker(self, broker_id):
        query = "SELECT * FROM brokers WHERE broker_id = %s"
        val = (broker_id, )
        self.cursor.execute(query, val)
        for brokers in self.cursor:
            broker = Broker(brokers[0], brokers[1], brokers[2])
            self.brokers_list.append(broker)
            return broker
    def get_broker_by_name(self, broker_name):
        query = "SELECT * FROM brokers WHERE broker_name = %s"
        val = (broker_name,)
        self.cursor.execute(query, val)
        result = self.cursor.fetchone()
        broker = Broker(result[0],result[1],result[2])
        return broker
        # for brokers in self.cursor:
        #     broker = Broker(brokers[0], brokers[1], brokers[2])
        #     self.brokers_list.append(broker)
        #     return broker

    def add_broker(self, name, address):
        query = "INSERT INTO brokers (broker_name,  address) VALUES (%s, %s)"
        val = (name, address)
        self.cursor.execute(query, val)
        self.cnx.commit()

    def delete_broker(self, broker_id):
        query = "DELETE FROM brokers WHERE broker_id = %s"
        val = (broker_id, )
        self.cursor.execute(query, val)
        self.cnx.commit()
        return
    def refresh(self):
        self.cnx.commit()

p = Database()
p.get_users()
