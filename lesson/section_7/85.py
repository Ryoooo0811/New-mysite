class Person(object):
  def __init__(self, age = 1):
    self.age = age
  
  def drive(self):
    if self.age >= 18:
      print('ok')
    else:
      raise Exception('No drive')

class Baby(Person):
  def __init__(self, age = 1):
    if age < 18:
      super().__init__(age)
    else:
      raise ValueError

class Adult(Person):
  def __init__(self, age = 18):
    if age >= 18:
      super().__init__(age)
    else:
      raise ValueError

baby = Baby()
adult = Adult()

class Car(object):
  def __init__(self, model = None):
    self.model = model
  def run(self):
    print('run')
  
  def ride(self, person):
    person.drive()

car = Car()
car.ride(adult)

# class ToyotaCar(Car):
#   def run(self):
#     print('fast')

# class TeslaCar(Car):
#   def __init__(self, model = 'Model S', enable_auto_run = False, passwd = '123'):
#     super().__init__(model)
#     self.__enable_auto_run = enable_auto_run
#     self.passwd = passwd
  
#   @property
#   def enable_auto_run(self):
#     return self._enable_auto_run
  
#   @enable_auto_run.setter
#   def enable_auto_run(self, is_enable):
#     if self.passwd == '456':
#       self._enable_auto_run = is_enable
#     else:
#       raise ValueError
  
#   def run(self):
#     print(self.__enable_auto_run)
#     print('super fast')
  
#   def auto_run(self):
#     print('auto run')

# tesla_car = TeslaCar('Model S', passwd = '111')
# tesla_car.run()
# # print(tesla_car.__enable_auto_run)
# print("\n")



# class T(object):
#   pass

# t = T()
# t.name = 'Mike'
# t.age = 20
# print(t.name)