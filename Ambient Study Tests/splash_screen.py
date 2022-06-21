from os import getenv
from time import sleep
from urllib import response

from dotenv import dotenv_values, load_dotenv
from httpx import get
from PySimpleGUI import PopupAnimated
from sqlalchemy import create_engine

load_dotenv()

print(dotenv_values())

# Example of a Splash Screen
PopupAnimated(
    getenv('SPLASH_IMAGE'),
    location=(300, 200)
)

# Example of a requesting a Splash Screen
def request_example(number):
    URL = f'{getenv("ROUTE_SEARCH_API")}{number}'
    response = get(URL).json()

    name = response['name']

    return name

# Example of Database Splash Screen
engine = create_engine(getenv('DATABASE_URL'))  # type: ignore

sleep(5)
PopupAnimated(None)
