class BOL:
    def __init__(self, bill_id,date, bill_number,broker_name, shipper_name, user_name, rate_type, origin, destination, start_time, end_time, hours_loads, rate):
        self.bill_id = bill_id
        self.date = date
        self.bill_number = bill_number
        self.broker_name = broker_name
        self.shipper_name = shipper_name
        self.user_name = user_name
        self.origin = origin
        self.destination = destination
        self.start_time = start_time
        self.end_time = end_time
        self.hours_loads = hours_loads
        self.rate = rate
        self.rate_type = rate_type
