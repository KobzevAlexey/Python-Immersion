from typing import TypeAlias
import json
from student import Student

STUDENT_FILE = 'student.json'
STUDENT_TYPE: TypeAlias = dict[str, dict[str, dict[str, list[int]]]]


def load_students(path: str) -> STUDENT_TYPE:
    with open(path, 'r', encoding='UTF-8') as file:
        result = json.load(file, parse_int=int)
    return result


if __name__ == '__main__':
    students_base = []
    students = load_students(STUDENT_FILE)
    for student, marks in students.items():
        students_base.append(Student(*student.split()))
        students_base[-1].marks = marks['marks']
        students_base[-1].tests = marks['tests']

    for student in students_base:
        print(student)
