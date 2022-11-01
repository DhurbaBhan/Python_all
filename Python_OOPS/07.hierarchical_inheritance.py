class Person:
    def show_person(self):
        print("This is show_person.")
class Student(Person):
    def show_student(self):
        print('This is show_student.')
class Dhurba(Person):
    def show_dhurba(self):
        print("This is show_dhurba")
d=Dhurba()
s=Student()
s.show_person()
d.show_dhurba()
d.show_person()
       