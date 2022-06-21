from os import getenv

# If there is no such variable in the system, return as in the None example
print(getenv('LDP'))

# If there is no such variable in the system, you can return something, as in the Text example
print(getenv('SPLASH_IMAGE', 'C://imagen.png'))
