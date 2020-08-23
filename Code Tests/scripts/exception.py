"""
except HTTPException as e:
    print(f'ERRO API EXTERNA {e.args}')
except Exception as e:
    await mobile_test.notify(ERROR_TYPE,ERROR_EXECUTION_MSG, user.token, user.email)
print(f'ERRO AO EXECUTAR O TESTES {str(e)}')
# raise HTTPException(400, str(e))

"""

lista = []

class UnAcceptedValueError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)


try:
    for p in lista:
        lista[0] +=1
except UnAcceptedValueError as e:
    print("Received error:", e.data)
# except KeyboardInterrupt as e:
#     print('Caught KeyboardInterrupt')
# except ZeroDivisionError as e:  
#     print("Zero Division Exception Raised." )
# except OverflowError as e:  
#     print("OverFlow Exception Raised.")
# except AssertionError as e:  
#     print ("Assertion Exception Raised.")
# except AttributeError as e:
#     print ("Attribute Exception Raised.")
# except LookupError as e:  
#     print ("Key Error Exception Raised.")
# except NameError as e:  
#     print ("NameError: name 'ans' is not defined")
# except TypeError as e:
#     print ('TypeError Exception Raised')
# except IndexError as e:
#     e.err = ('lista vazia',)
#     raise ValueError
# except ValueError as e:
#     print (f'ValueError: could not convert string to float: {e.err}')

