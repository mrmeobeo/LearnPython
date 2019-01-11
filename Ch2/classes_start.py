#
# Example file for working with classes
#

class myClass():
  def method1(self):
    print("Myclass Method1")

  def method2(sefl, Somestring):
    print("Myclass Method2 " + Somestring)

class MeoClass(myClass):
  def method1(self):
    myClass.method1(self)
    print("Meoclass Method1")

  def method2(sefl, Somestring):
    print("Meoclass Method2 ")

def main():
  c = myClass()
  c.method1()
  c.method2("MEOMEO")

  c2=MeoClass()
  c2.method1()
  c2.method2("MEOMEO")
  
if __name__ == "__main__":
  main()
