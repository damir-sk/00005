from CATimport import cats

class CAT:
    def __init__(self, name=str, age=int, sex=""):
        self.name = name
        self.age = age
        self.sex = sex


    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getSex(self):
        return self.sex


for i in cats:
    cat_pet = CAT(name=i.get("name"),
                      age=i.get("age"),
                      sex=i.get("sex"))
    print('--------------------')
    print(cat_pet.name)
    print(cat_pet.age)
    print(cat_pet.sex)
   

#cats=CAT("Murz",5, "M")

#print('cats.name =', cats.name)
#print('cats.age =', cats.age)
#print('cats.sex =', cats.getSex())
