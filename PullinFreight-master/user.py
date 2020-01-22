
class User:

    def __init__(self, user_id, first_name, last_name,
                username, phone_number, email,
                address, license_number, license_expire, special_expire, comment, drug_test, carb, mpc, dir):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.license_number = license_number
        self.license_expire = license_expire
        self.drug_test = drug_test
        self.carb = carb
        self.mpc = mpc
        self.dir = dir
        self.special_expire = special_expire
        self.comment = comment
