from faker import Faker
from random import randint as RI
import json
import csv

MIN_MARK = 2
MAX_MARK = 5
MIN_TEST = 0
MAX_TEST = 100
MIN_MARK_COUNT = 5
MAX_MARK_COUNT = 10
MIN_TEST_COUNT = 1
MAX_TEST_COUNT = 5
STUDENT_COUNT = 20
SUBJECT_FILE = 'subjects.csv'
STUDENT_FILE = 'student.json'


def load_subjects(file_name: str) -> tuple[str]:
    with open(file_name, 'r', encoding='UTF-8') as file:
        csv_reader = csv.reader(file, dialect='excel')
        result = tuple(next(csv_reader))
    return result


def marks_generator(subjects: tuple[str],
                    min_marks_count: int,
                    max_marks_count: int,
                    min_mark: int, max_mark: int) -> dict[str, tuple[int]]:
    def generator_numbers() -> tuple[int]:
        return tuple([RI(min_mark, max_mark) for _ in range(RI(min_marks_count, max_marks_count))])

    return {sub: generator_numbers() for sub in subjects}


def generator_students(base_students: dict,
                       subjects: tuple,
                       students_count: int = STUDENT_COUNT):
    fake = Faker('ru-RU')
    for _ in range(students_count):
        if RI(0, 1):
            last_name = fake.last_name_male()
            first_name = fake.first_name_male()
            patronymic = fake.middle_name_male()
        else:
            last_name = fake.last_name_female()
            first_name = fake.first_name_female()
            patronymic = fake.middle_name_female()
        base_students[' '.join((last_name, first_name, patronymic))] = {
            'marks': marks_generator(subjects, MIN_MARK_COUNT, MAX_MARK_COUNT, MIN_MARK, MAX_MARK),
            'tests': marks_generator(subjects, MIN_TEST_COUNT, MAX_TEST_COUNT, MIN_TEST, MAX_TEST)}


def create_students_base(dict_to_dump: dict, path: str = STUDENT_FILE):
    with open(path, 'w', encoding='UTF-8') as file:
        json.dump(dict_to_dump, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    base_student = {}
    generator_students(base_student, load_subjects(SUBJECT_FILE))
    create_students_base(base_student)
