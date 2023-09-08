class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


    #Даем оценки студентами лектору
    def rate_lecturer(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.finished_courses or course in self.courses_in_progress \
                and course in lector.courses_attached:
            if course in lector.grades:
                lector.grades[course] += [grade]
            else:
                lector.grades[course] = [grade]
        else:
            return 'Ошибка'
    #Считаем авг студента для "Средней оценки за ДЗ"
    def average_grades(self):
        value = [f'{sum(value) / len(value)}' for key, value in self.grades.items()]
        return ', '.join(value)
    #Итерируемя по курсам и печатаем их "В процессе изучения"
    def courses_in_prog_func(self):
        for i in self.courses_in_progress:
            return i
    #Итерируемя по курсам и печатаем их "Завершенные курсы"
    def finished_func(self):
        if len(self.finished_courses) != 0:
            for name in self.finished_courses:
                return name
        else:
            return ('Пока нет завершенных курсов')
    #Меняем описание объекта класса Student
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за домашние задания: {self.average_grades()} \n' \
              f'Курсы в процессе изучения: {self.courses_in_prog_func()} \nЗавершенные курсы: {self.finished_func()}'
        return res
    #Ищем среднюю всех студентов для сравнения __lt__
    @property
    def avg_grade(self):
        total_grades = []
        for k, v in self.grades.items():
            total_grades.extend(v)
        return sum(total_grades) / len(total_grades)
    #Метод для сравнения средней объектов класса Student
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Lecturer')
        return self.avg_grade < other.avg_grade

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    #Считаем среднюю для __str__
    def avr_grades(self):
        value = [f'{sum(value) / len(value)}' for key, value in self.grades.items()]
        return ', '.join(value)

    # Меняем описание объекта класса Lecturer
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.avr_grades()}'
        return res
    #Ищем среднюю всех лекторов для сравнения __lt__
    @property
    def avg_grade(self):
        total_grades = []
        for k, v in self.grades.items():
            total_grades.extend(v)
        return sum(total_grades) / len(total_grades)
    #Метод для сравнения средней объектов класса Lecturer
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer')
        return self.avg_grade < other.avg_grade

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
    #Метод для выставления оценок менторами студентам
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    # Меняем описание объекта класса Reviewer
    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}'
        return res

#Линия лекторов
awesome_lecturer = Lecturer('Kirill', 'Ivanov')
awesome_lecturer.courses_attached += ['Python']

awesome_lecturer_1 = Lecturer('Andrey', 'Losev')
awesome_lecturer_1.courses_attached += ['Python']


#Линия студентов
best_student = Student('Ruoy', 'Eman', 'male')
best_student.courses_in_progress += ['Python']

best_student_2 = Student('Zura', 'Dzug', 'male')
best_student_2.courses_in_progress += ['Python']

best_student.rate_lecturer(awesome_lecturer, 'Python', 10)
best_student.rate_lecturer(awesome_lecturer, 'Python', 9)
best_student.rate_lecturer(awesome_lecturer, 'Python', 8)

best_student.rate_lecturer(awesome_lecturer_1, 'Python', 8)
best_student.rate_lecturer(awesome_lecturer_1, 'Python', 10)
best_student.rate_lecturer(awesome_lecturer_1, 'Python', 7)

#Линия ревьюера
cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor_1 = Reviewer('Andy', 'Bringman')
cool_mentor_1.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor_1.rate_hw(best_student_2, 'Python', 6)
cool_mentor_1.rate_hw(best_student_2, 'Python', 6)
cool_mentor_1.rate_hw(best_student_2, 'Python', 7)








#Принты всех методов студента
print('***Все методы студента***')

print(best_student) #описание стдента 1
print()
print(best_student_2) #описание стдента 2
print()
print(best_student < best_student_2) #сравнение оценки по средней за курсы
print()

print('***Все методы Лектора***')

print(awesome_lecturer) #описание лектора 1
print()
print(awesome_lecturer_1) #описание лектора 2
print()
print(awesome_lecturer > awesome_lecturer_1) #сравнение оценки по средней за курсы
print()

print('***Все методы Ревьюера***')
print(cool_mentor)
print()
print(cool_mentor_1)
print()



#подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса
def avg_students_grade(course, students):
    course_grades = []
    for student in students:
        if student.grades.get(course):
            course_grades.extend(student.grades[course])
    return sum(course_grades) / len(course_grades)
print('***Подсчет средней оценки за домашние задания по всем студентам в рамках конкретного курса***')
print(round(avg_students_grade('Python', [best_student, best_student_2]), 2))

#подсчет средней оценки за лекции всех лекторов в рамках курса
def avg_lecturers_grade(course, lecturers):
    course_grades = []
    for lecturer in lecturers:
        if lecturer.grades.get(course):
            course_grades.extend(lecturer.grades[course])
    return sum(course_grades) / len(course_grades)

print('***Подсчет средней оценки за домашние задания по всем лекторам в рамках конкретного курса***')
print(round(avg_lecturers_grade('Python', [awesome_lecturer, awesome_lecturer_1]), 2))
