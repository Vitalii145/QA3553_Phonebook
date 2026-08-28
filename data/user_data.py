from faker import Faker

from models.users import User

fake = Faker()
def create_user(username= None,password =None):
    return User(
        username = username if username is not None else fake.unique.email(),
        password = password if password is not None else fake.password(
            length=12, special_chars=True, digits=True, upper_case=True, lower_case=True
        )
    )
EXIYING_USER_EMAIL = 'vitalii.dev2026@outlook.com'
EXIYING_USER_PASSWORD = 'N7!qR4#vL9@xT2'
INVALID_EMAIL = 'vitalii.dev2026outlook.com'
INVALID_PASSWORD = 'NqR4L9@xT2'

def exiting_user():
    return create_user(username=EXIYING_USER_EMAIL, password=EXIYING_USER_PASSWORD)

def invalid_email_user():
    return create_user(username=INVALID_EMAIL, password=EXIYING_USER_PASSWORD)

def invalid_password_user():
    return create_user(username=EXIYING_USER_EMAIL, password=INVALID_PASSWORD)