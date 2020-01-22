class Current_job:
    def __init__(self, job_id, shipper_name, broker_name ,username, start_date, start_time, pay_type, rate, origin, destination, comments, status):
        self.job_id = job_id
        self.shipper_name = shipper_name
        self.broker_name = broker_name
        self.username = username
        self.start_date = start_date
        self.start_time = start_time
        self.pay_type = pay_type
        self.rate = rate
        self.origin = origin
        self.destination = destination
        self.comments = comments
        self.status = status
