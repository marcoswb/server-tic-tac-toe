from dotenv import load_dotenv
import os
import bcrypt

load_dotenv()


def get_environment_variable(variable):
    return os.environ.get(variable)


def valid_json_input(data_json, keys):
    for key in keys:
        if not data_json.get(key):
            return False

    return True


def encrypt_password(password):
    salt = bcrypt.gensalt()
    password_hash = bcrypt.hashpw(str(password).encode(), salt)
    return password_hash.decode('utf-8')
