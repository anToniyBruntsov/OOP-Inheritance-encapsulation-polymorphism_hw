from typing import Union, Any, List


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_hw = 0.0
    def __str__(self):
        self._average_hw_calculation()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_hw}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
    def __gt__(self, other):
        self._average_hw_calculation()
        Student._average_hw_calculation(other)
        return self.average_hw > other.average_hw
    def rate_lection(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_lecturer:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def _average_hw_calculation(self):
        if len(self.grades) > 0:
            __average = 0.0
            __i = 0
            for __course in self.grades:
                __grades = self.grades[__course]
                __average += sum(__grades)
                __i += len(__grades)
                self.average_hw = '%.1f' % (__average / __i)
        else:
            self.average_hw = 0.0
class Mentor:
    def __init__(self, name, surname,):
        self.name = name
        self.surname = surname
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_lecturer = []
        self.average = 0.0
    def __str__(self):
        self._average_calculation()
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average}'
    def __gt__(self, other):
        self._average_calculation()
        Lecturer._average_calculation(other)
        return self.average > other.average
    def _average_calculation(self):
        if len(self.grades) > 0:
            __average = 0.0
            __i = 0
            for __course in self.grades:
                __grades = self.grades[__course]
                __average += sum(__grades)
                __i += len(__grades)
                self.average = '%.1f' % (__average / __i)
        else:
            self.average = 0.0
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_reviewer = []
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_reviewer and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
def course_average_grade_hw(student_list, course):
    curse_garde = []
    for student in student_list:
        if course in student.grades:
            curse_garde.extend(student.grades[course])
        else:
            break
    course_average = sum(curse_garde) / len(curse_garde)
    return print(f'Средняя оценка за домашнии задания на курсе {course}: {course_average}')
def lection_average_grade(lecturer_list, course):
    curse_garde = []
    for lecturer in lecturer_list:
        if course in lecturer.grades:
            curse_garde.extend(lecturer.grades[course])
        else:
            break
    course_average = sum(curse_garde) / len(curse_garde)
    return print(f'Средняя оценка за лекцию на курсе {course}: {course_average}')

# adding copies of classes
# add students
first_student = Student('Юлия', 'Марченко', 'жен')
first_student.courses_in_progress += ['Python']
first_student.courses_in_progress += ['Git']
first_student.finished_courses += ['Java']
first_student.finished_courses += ['Основы програмирования']
second_student = Student('Виктор', 'Белов', 'муж')
second_student.courses_in_progress += ['Python']
second_student.courses_in_progress += ['Git']
second_student.finished_courses += ['Основы програмирования']

# add reviwers
first_mentor = Reviewer('Константин', 'Неклюдов')
first_mentor.courses_reviewer += ['Python']
first_mentor.courses_reviewer += ['Git']
second_mentor = Reviewer('Егоров', 'Кирилл',)
second_mentor.courses_reviewer += ['Python']
second_mentor.courses_reviewer += ['Java']

# add lecturer
first_lecturer = Lecturer('Густав', 'Мюллер',)
first_lecturer.courses_lecturer += ['Python']
first_lecturer.courses_lecturer += ['Git']
second_lecturer = Lecturer('Андоей', 'Кротов')
second_lecturer.courses_lecturer += ['Java']
second_lecturer.courses_lecturer += ['Git']

# set grades
# for students
first_mentor.rate_hw(second_student, 'Python', 8)
first_mentor.rate_hw(second_student, 'Git', 7)
first_mentor.rate_hw(second_student, 'Git', 10)
second_mentor.rate_hw(first_student, 'Python', 10)
second_mentor.rate_hw(first_student, 'Python', 6)
first_mentor.rate_hw(first_student, 'Git', 10)
# for lecturers
second_student.rate_lection(second_lecturer, 'Git', 10)
second_student.rate_lection(first_lecturer, 'Python', 10)
first_student.rate_lection(second_lecturer, 'Git', 7)
first_student.rate_lection(first_lecturer, 'Git', 9)
second_student.rate_lection(first_lecturer, 'Python', 10)
first_student.rate_lection(second_lecturer, 'Git', 7)

# the runs
print(first_mentor)
print(second_mentor)

print(first_lecturer)
print(first_lecturer.__gt__(second_lecturer))

print(second_lecturer)
print(second_lecturer.__gt__(first_lecturer))

print(first_student)
print(first_student.__gt__(second_student))

print(second_student)
print(second_student.__gt__(first_student))

course_average_grade_hw([first_student, second_student], 'Python')
course_average_grade_hw([first_student, second_student], 'Git')

lection_average_grade([first_lecturer, second_lecturer], 'Python')
lection_average_grade([first_lecturer, second_lecturer], 'Git')
