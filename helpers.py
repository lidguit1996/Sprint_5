import random as rd

class Helpers:
    @staticmethod
    def generate_email():
        return f"yuri_hanalainen_12_{rd.randint(000, 999)}@yandex.ru"

    @staticmethod
    def generate_password():
        return f'Password{rd.randint(000, 999)}'