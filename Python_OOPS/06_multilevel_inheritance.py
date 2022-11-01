class Person:
    def show_person(self):
        print("This is show_person.")
    def takebreath(self):
        print("person is breathing.")    
class Student(Person):
    def show_student(self):
        print('This is show_student.')
    def takebreath(self):
        super().takebreath()
        print("student is breathing.")   
class Dhurba(Student):
    def show_dhurba(self):
        print("This is show_dhurba")
    def takebreath(self):
        super().takebreath()
        print("Dhurba is breathing.")    
d=Dhurba()
# d.show_dhurba()
# d.show_person()
# d.show_student()    
d.takebreath()    