from string import ascii_lowercase, digits
import random


class EmailValidator:
    symbols = ascii_lowercase + digits + "@._"

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        email = "".join(random.choices(cls.symbols, k=random.randrange(0, 99))) + "@gmail.com"
        return email

    @classmethod
    def check_email(cls, email):
        if cls.__is_email_str(email):
            if len(email[:email.find("@")]) > 100 or len(email[email.find("@"):]) > 50:
                return False
            elif ".." in email[:email.find("@")]:
                return False
            elif not set(email).issubset(set(cls.symbols)):
                return False
            elif not set(".").issubset(set(email[email.find("@"):])) or ".." in email[email.find("@"):]:
                return False
            return True
        return False

    @staticmethod
    def __is_email_str(email):
        return type(email) is str

