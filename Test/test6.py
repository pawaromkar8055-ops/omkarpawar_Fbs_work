class Toll:

    def __init__(self, persons):
        self.__persons = persons

    # Getter
    def get_persons(self):
        return self.__persons

    # Setter
    def set_persons(self, persons):
        self.__persons = persons

    def calculate_toll(self):
        return 0


class TwoWheeler(Toll):

    def calculate_toll(self):
        toll = 20

        if self.get_persons() > 2:
            extra = self.get_persons() - 2
            toll = toll + (extra * 10)

        return toll


class ThreeWheeler(Toll):

    def calculate_toll(self):
        toll = 30

        if self.get_persons() > 3:
            extra = self.get_persons() - 3
            toll = toll + (extra * 20)

        return toll


class FourWheeler(Toll):

    def calculate_toll(self):
        toll = 40

        if self.get_persons() > 4:
            extra = self.get_persons() - 4
            toll = toll + (extra * 40)

        return toll


class HeavyVehicle(Toll):

    def calculate_toll(self):
        toll = 60

        if self.get_persons() > 6:
            extra = self.get_persons() - 6
            toll = toll + (extra * 100)

        return toll



while True:

    print("\n===== TOLL PLAZA =====")
    print("1. Two Wheeler")
    print("2. Three Wheeler")
    print("3. Four Wheeler")
    print("4. Heavy Vehicle")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 5:
        print("omkar")
        break

    persons = int(input("Enter number of persons: "))

    if choice == 1:
        t = TwoWheeler(persons)

    elif choice == 2:
        t = ThreeWheeler(persons)

    elif choice == 3:
        t = FourWheeler(persons)

    elif choice == 4:
        t = HeavyVehicle(persons)

    else:
        print("Invalid choice")
        continue

    print("Number of persons =", t.get_persons())
    print("Total Toll = Rs.", t.calculate_toll())