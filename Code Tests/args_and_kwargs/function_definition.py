# TUTORIAL DE : https://realpython.com/python-kwargs-and-args/

# CORRECT
def correct_function(a, b, *args, **kwargs):
    pass

# WRONG
def wrong_function(a, b, **kwargs, *args):
    pass
