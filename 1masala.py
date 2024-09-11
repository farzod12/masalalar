import os
os.system("cls")
class Circle:
  def __init__(self,tel1,tel2,tel3):
      self.modeli=tel1
      self.narxi=tel2
      self.rangi=tel3

  def telefon(self):
    print(f""" modeli : {self.modeli}
    narxi : {self.narxi}
    rangi :{self.rangi}""")

tell1=Circle("nokiya",2500,"qzil")
print("  ")
tell2=Circle("ipxone",300000,"oq")
print("   ")
tell3=Circle("samsung",40000,"yashil")

tellar=[tell1,tell2,tell3]
for tel in tellar:
    print (" ")
    tel.telefon()
    