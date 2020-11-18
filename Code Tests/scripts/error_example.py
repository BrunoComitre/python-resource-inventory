
except KeyboardInterrupt:
    print('Caught KeyboardInterrupt')
except ZeroDivisionError:  
    print("Zero Division Exception Raised." )
except OverflowError:  
    print("OverFlow Exception Raised.")
except AssertionError:  
    print ("Assertion Exception Raised.")
except AttributeError:
    print ("Attribute Exception Raised.")
except LookupError:  
    print ("Key Error Exception Raised.")
except NameError:  
    print ("NameError: name 'ans' is not defined")
except TypeError:
    print ('TypeError Exception Raised')
except ValueError:
    print ('ValueError: could not convert string to float: \'DataCamp\'')


class UnAcceptedValueError(Exception):   
    def __init__(self, data):    
        self.data = data
    def __str__(self):
        return repr(self.data)


except UnAcceptedValueError as e:
    print("Received error:", e.data)
