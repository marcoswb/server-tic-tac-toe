from dotenv import load_dotenv
import os

load_dotenv()


def get_environment_variable(variable):
    return os.environ.get(variable)
