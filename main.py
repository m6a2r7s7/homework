class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя:{self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания:{Lecturer.average_grade(self)}\n'
        res = res + f'Курсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res
    def compare_persons(self, person_1, person_2):
        if (isinstance(person_1, Student) and isinstance(person_2, Student)) or (isinstance(person_1, Lecturer) and isinstance(person_2, Lecturer)):
            if Lecturer.average_grade(person_1) > Lecturer.average_grade(person_2):
                res = f'Средняя оценка первого участника ({Lecturer.average_grade(person_1)}) больше чем у второго ({Lecturer.average_grade(person_2)})'
                return res
            else:
                res = f'Средняя оценка второго участника ({Lecturer.average_grade(person_2)}) больше чем у первого ({Lecturer.average_grade(person_1)})'
                return res
        else:
            return 'Ошибка'



class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    def average_grade(self):
        res = 0
        for l in self.grades:
            for grade in range(len(self.grades[l])):
                res = res + self.grades[l][grade]
            res = res // len(self.grades[l])
            return res
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}'
        return res

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res

def lecturers_average_grade(list_of_lecturers, course):
    res = 0
    for lecturer in list_of_lecturers:
        for grade in lecturer.grades[course]:
            res = res + grade
    res = res / len(list_of_lecturers)
    return f'Средняя оценка за лекции по курсу {course} равна {res}'
def students_average_grade(list_of_students, course):
    res = 0
    for student in list_of_students:
        for grade in student.grades[course]:
            res = res + grade
    res = res / len(list_of_students)
    return f'Средняя оценка за дз по курсу {course} равна {res}'

first_student = Student('Some', 'Dude', 'M')
second_student = Student('Not', 'Dude', 'F')
print(first_student, '\n')
print(second_student, '\n')

first_lecturer = Lecturer('Some', 'Guy')
second_lecturer = Lecturer('Some', 'Lady')
print(first_lecturer, '\n')
print(second_lecturer, '\n')

first_reviewer = Reviewer('Some', 'Guy')
second_reviewer = Reviewer('Some', 'Lady')
print(first_reviewer, '\n')
print(second_reviewer, '\n')

first_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['JavaScript']
first_lecturer.courses_attached += ['Python']
second_lecturer.courses_attached += ['JavaScript']
first_reviewer.courses_attached += ['Python']
second_reviewer.courses_attached += ['JavaScript']

first_student.rate_lecturer(first_lecturer, 'Python', 10)
first_student.rate_lecturer(first_lecturer, 'Python', 8)
print(first_lecturer.grades)
second_student.rate_lecturer(second_lecturer, 'JavaScript', 7)
second_student.rate_lecturer(second_lecturer, 'JavaScript', 6)
print(second_lecturer.grades, '\n')

print(first_student.compare_persons(first_lecturer, second_lecturer), '\n')

print(first_lecturer.average_grade())
print(second_lecturer.average_grade(), '\n')

first_reviewer.rate_hw(first_student, 'Python', 7)
first_reviewer.rate_hw(first_student, 'Python', 5)
print(first_student.grades)
second_reviewer.rate_hw(second_student, 'JavaScript', 10)
second_reviewer.rate_hw(second_student, 'JavaScript', 7)
print(second_student.grades, '\n')

print(first_student.compare_persons(first_student, second_student), '\n')

print(Lecturer.average_grade(first_student))
print(Lecturer.average_grade(second_student), '\n')

another_lecturer_py = Lecturer('another', 'Dude')
another_lecturer_py.courses_attached += ['Python']
first_student.rate_lecturer(another_lecturer_py, 'Python', 9)
first_student.rate_lecturer(another_lecturer_py, 'Python', 7)
another_lecturer_py.courses_attached += ['JavaScript']
second_student.rate_lecturer(another_lecturer_py, 'JavaScript', 6)
second_student.rate_lecturer(another_lecturer_py, 'JavaScript', 8)

print(lecturers_average_grade([first_lecturer, another_lecturer_py], 'Python'), '\n')

another_student_py = Student('another', 'student', 'x')
another_student_py. courses_in_progress += ['Python']
first_reviewer.rate_hw(another_student_py, 'Python', 10)
first_reviewer.rate_hw(another_student_py, 'Python', 6)

print(students_average_grade([first_student, another_student_py], 'Python'))











