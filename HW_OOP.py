class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def _average_grade(self):
        sum_course_grade = sum(map(sum, self.grades.values()))
        len_grade = 0
        for grade in self.grades:
            len_grade += len(self.grades[grade])
        return sum_course_grade / len_grade

    def rate_lecture(self, lecturer, course, lecture_grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecture_grades:
                lecturer.lecture_grades[course] += [lecture_grade]
            else:
                lecturer.lecture_grades[course] = [lecture_grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_grade()}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            return f'{other.surname} не является студентом'
        else:
            return self._average_grade() < other._average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_grades = {}

    def _average_grade(self):
        sum_lecture_grade = sum(map(sum, self.lecture_grades.values()))
        len_grade = 0
        for grade in self.lecture_grades:
            len_grade += len(self.lecture_grades[grade])
        return sum_lecture_grade / len_grade

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade()}'
        return res

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            return f'{other.surname} не является лектором'
        else:
            return self._average_grade() > other._average_grade()

class Reviewer(Mentor):
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


# ---ПОЛЕВЫЕ ИСПЫТАНИЯ---

# создание экземпляров
student_1 = Student('Михаил', 'Смирнов', 'М')
student_1.courses_in_progress += ['Алгебра', 'Геометрия', 'Физика', 'Астрономия', 'ОБЖ']
student_1.finished_courses += ['Химия', 'Английский']
student_2 = Student('Виктория', 'Иванова', 'Ж')
student_2.courses_in_progress += ['Алгебра', 'Геометрия', 'ОБЖ']
student_2.finished_courses += ['Химия', 'Английский']
mentor_1 = Mentor('Виктор', 'Степанов')
mentor_2 = Mentor('Виктория', 'Степанова')
lecturer_1 = Lecturer('Алексей Васильевич', 'Ким')
lecturer_1.courses_attached += ['Алгебра', 'Геометрия', 'ОБЖ']
lecturer_2 = Lecturer('Анна Юрьевна', 'Зайцева')
lecturer_2.courses_attached += ['Физика', 'Астрономия', 'ОБЖ']
reviewer_1 = Reviewer('Мария Юрьевна', 'Немшилова')
reviewer_1.courses_attached += ['Алгебра', 'Геометрия']
reviewer_2 = Reviewer('Марк Антонович', 'Мухин')
reviewer_2.courses_attached += ['Физика', 'Астрономия']

# получение оценок
reviewer_1.rate_hw(student_1, 'Алгебра', 9)
reviewer_1.rate_hw(student_1, 'Алгебра', 8)
reviewer_1.rate_hw(student_1, 'Алгебра', 9)
reviewer_1.rate_hw(student_1, 'Геометрия', 8)
reviewer_1.rate_hw(student_2, 'Алгебра', 8)
reviewer_1.rate_hw(student_2, 'Алгебра', 10)
reviewer_1.rate_hw(student_2, 'Алгебра', 5)
reviewer_1.rate_hw(student_2, 'Геометрия', 9)
student_1.rate_lecture(lecturer_1, 'Алгебра', 6)
student_2.rate_lecture(lecturer_1, 'Алгебра', 8)
student_1.rate_lecture(lecturer_1, 'ОБЖ', 1)
student_2.rate_lecture(lecturer_2, 'ОБЖ', 2)
student_1.rate_lecture(lecturer_2, 'Физика', 9)
student_1.rate_lecture(lecturer_2, 'Астрономия', 7)

# вывод информации об экземпляре
print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)
print(reviewer_1)
print(reviewer_2)

# сравнение экземпляров
print(student_1 > student_2)
print(student_1 < mentor_2)
print(lecturer_1 > lecturer_2)

# функция для подсчета средней оценки за ДЗ по студентам в рамках конкретного курса
def average_grade_course_hw (student_list, req_course):
  sum_grade = []
  for student in student_list:
    sum_grade.extend(student.grades.get(req_course, []))
  return f'Средний бал студентов по курсу {req_course}: {sum(sum_grade) / len(sum_grade)}'

st_list = [student_1, student_2]
print(average_grade_course_hw(st_list, 'Геометрия'))

# функция для подсчета средней оценки за лекции всех лекторов в рамках курса (в качестве аргумента принимаем список лекторов и название курса).
def lecture_rating(lecturer_list, req_course):
    sum_grade = []
    for lecturer in lecturer_list:
        sum_grade.extend(lecturer.lecture_grades.get(req_course, []))
    return f'Рейтинг лекций по курсу {req_course}: {sum(sum_grade) / len(sum_grade)}'

lec_list = [lecturer_1, lecturer_2]
print(lecture_rating(lec_list, 'ОБЖ'))