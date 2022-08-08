class TICKET:
    def __init__(self, name, age, gender, seatnumber, destination):
        self.destination = destination
        self.seatnumber = seatnumber
        self.gender = gender
        self.age = age
        self.name = name

    def display(self):
        print("Name: %s \nAge: %d \nGender: %s \nSeatnumber: %d \nDestination: %s"
              % (self.name, self.age, self.gender, self.seatnumber, self.destination))

obj1 = TICKET("Mr.Falcon", 25, "Male", 45, "New Delhi")
obj1.display()