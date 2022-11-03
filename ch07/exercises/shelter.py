import time


class Animal:
    def __init__(self, name, type):
        self.id = id(self)
        self.name = name
        self.type = type
        self.time_arrived = time.strftime("%d/%m/%Y")
        self.time_adopted = None

  
    def set_adopted(self):
        self.time_adopted = time.strftime("%d/%m/%Y")
        
def main():
      fido = Animal("fido", "cat")
      fido.set_adopted()
  
main()