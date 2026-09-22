class Base:
   # i = 0, j = 0
   def fun(self):
      print("Base fun.")
   def gun(self):
      print("Base gun.")
   def sun(self):
      print("Base sun.")
   def run(self):
      print("Base run.")

class Derived(Base):
   # x = 0
   def fun(self):
      print("Derived fun.")
   def sun(self):
      print("Derived sun.")

bp: Base = Derived()
bp.fun() # Derived fun
bp.gun() # Base gun
bp.sun() # Derived sun
bp.run() # Base run

    
    
    
    