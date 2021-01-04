"""
public =  métodos e atributos que podem ser acessados dentro e fora da classe
protected = atributos que podem ser acessados apenas dentro da classe ou das filhas daquela classe
private = atributo ou método só está disponível dentro da classe
_protected
__private
"""
    
class Database:
    def __init__(self):
        self.data = {}  # public
        self._data = {}  # protected
        self.__data = {}  # private
        
    @property
    def data(self):
        return self.__data
    
    # @data.setter
    # def data(self, data):
    #     self.__data = data
 
    def insert(self, id, name):
        if 'clients' not in self.data:
            self.data['clients'] = {id: name}
        else:
            self.data['clients'].update({id:name})
                
    def list(self):
        for id, name in self._data['clients'].items():
            print(id, name)
    
    def delete(self,id):
        del self.__data['clients'][id]
        
database = Database()
database.insert(1, "João")
database.insert(2, "Maria")
database.insert(3, "José")
print(database.data)

database.delete(3)
print(database.data)

database.list()
print()

database.__data = "Outro Valor"
print(database.__data)
print(database._Database__data)
