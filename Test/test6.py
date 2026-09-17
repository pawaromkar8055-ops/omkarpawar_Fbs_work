class Vehicle:
    
    def __init__(self,wheels,person):
        self.wheels=wheels
        self.person=person
        
    def toll(self):
        return 0
    
class TwoWheeler(Vehicle):
    def toll(self):
        basic_toll=20
        
        if self.person>2:
            exter_person=self.person-2
            exter_charge=exter_person*10
        else:
            exter_charge=0
            
        return basic_toll+exter_charge
    
class ThreeWheeler(Vehicle):
    def toll(self):
        basic_toll=30
        if self.person>3:
                    exter_person=self.person-3
                    exter_charge=exter_person*20
        else:
                    exter_charge=0
                    
        return basic_toll+exter_charge
class FourWheeler(Vehicle):
    def toll(self):
        basic_toll=40
        
        if self.person>4:
                    exter_person=self.person-4
                    exter_charge=exter_person*30
        else:
                    exter_charge=0
                    
        return basic_toll+exter_charge       

class Heavyvechicle(Vehicle):
    def toll(self):
        basic_toll=60
        
        if self.person>6:
            exter_person=self.person-6
            exter_charge=exter_person*100
        else:
            exter_charge=0
                            
        return basic_toll+exter_charge

while True:

    print("\n===== TOLL PLAZA =====")
    print("1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Thank you!")
        break

    wheels = int(input("Enter number of wheels: "))
    persons = int(input("Enter number of persons: "))

    if choice == 1:
        v = TwoWheeler(wheels, persons)

    elif choice == 2:
        v = ThreeWheeler(wheels, persons)

    elif choice == 3:
        v = FourWheeler(wheels, persons)

    elif choice == 4:
        v = Heavyvechicle(wheels, persons)

    else:
        print("Invalid choice!")
        continue

    
    print("Total Toll = Rs.", v.toll())