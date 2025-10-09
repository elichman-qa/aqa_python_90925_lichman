class Student:

    def __init__(self, name, last_name, age, list_of_grades):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.list_of_grades = list_of_grades

    def add_grade(self, new_grade):
        self.list_of_grades.append(new_grade)

    def middle_grade(self):
        if not self.list_of_grades:
            return 0
        else:
            return int(sum(self.list_of_grades)/len(self.list_of_grades))

    def about_student(self):
        print(f'Сдудент на імʼя: {self.name} {self.last_name}, рік народження: {self.age}')
        print(f"Має такий перелік оцінок:{self.list_of_grades}")
        print(f"Середній бал з яких становить: {self.middle_grade()}")


student_01 = Student("Антон","Птушкін", 1999, [75, 79, 88])
student_01.add_grade(50)
student_01.about_student()

student_02 = Student("Petro", "Vishybailo", 2003, list(range(71, 76)))
student_02.add_grade(36)
student_02.about_student()
