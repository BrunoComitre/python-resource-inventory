import pprint
from os import environ

# Set environment variables
environ['USER'] = 'BrunoComitre'
print(environ['USER'])

# Environment variables
print(environ['LANG'])
print(environ['HOME'])

# Is a Dictionary
print(type(environ))

# List
print(list(environ))

# Get the list of user's
# environment variables
env_var = environ

# Print the list of user's
# environment variables
print("User's Environment variable:")
pprint.pprint(dict(env_var), width = 1)

# If there is no such variable in the system, you can return something, as in the None example
print(environ.get('LDP', 'None'))

# If we want to change the environment variables, we can make an assignment in the dictionary
environ['DEBUG'] = 'True'
print(environ['DEBUG'])

environ['DEBUG'] = 'False'
print(environ['DEBUG'])
