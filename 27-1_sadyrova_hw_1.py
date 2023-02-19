class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Person fullname:{self.fullname} age:{self.age} is_married: {self.is_married} ')


person = Person('Asanov Askar Asanovich', 25, 'yes')
person.introduce_myself()


class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        _marks = {}


student_1 = Student('Urmatov Azim Urmatovich', 21, 'no', marks={'student1': {'mathematics': 5, 'literature': 4, 'chemistry': 4, 'informatics': 5, 'physics': 5, 'biology': 3}})


class Teacher(Person):
    salary=30000
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience=experience


    def count_salary(self):
        if self.experience > 3:
            print(self.salary+self.experience*self.salary*0.05)
        else:
            print(self.salary)

teacher_1=Teacher('Malikova Alina Malikovna', 45, 'yes', 20)
teacher_1.count_salary()


_marks = {'student1': {'mathematics': 5, 'literature': 4, 'chemistry': 4, 'informatics': 5, 'physics': 5, 'biology': 3}}

_marks_new = dict()
for name, sub_dict in _marks.items():
    values = sub_dict.values()
    _marks_new = sum(values) / len(values)

print(f'Teacher fullname:{teacher_1.fullname} age:{teacher_1.age} is_married: {teacher_1.is_married}, experience: {teacher_1.experience}, salary: {teacher_1.count_salary()} ')
print(f'Student fullname:{student_1.fullname} age:{student_1.age} is_married: {student_1.is_married}, _marks{_marks} ')
print(_marks_new)

