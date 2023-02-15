import json


def load_students(students):
    """
    Получаем список доступных идентификационных номеров студентов
    """
    json_students = open(students)
    json_students_ = json_students.read()
    python_students = json.loads(json_students_)
    students_list = []
    for student in python_students:
        students_list.append(student["pk"])
    return students_list


def load_professions(professions):
    """
    Получаем список доступных направлений разработки
    """
    with open(professions) as json_professions:
        json_professions_ = json_professions.read()
        python_professions = json.loads(json_professions_)
        professions_list = []
        for profession in python_professions:
            professions_list.append(profession["title"])
        return professions_list


def get_student_by_pk(pk):
    """
    Получаем по номеру студента его имя и изученные навыки
    """
    json_pk = open("students.json")
    json_pk_ = json_pk.read()
    python_pk = json.loads(json_pk_)
    for number in python_pk:
        if pk == number["pk"]:
            return number["full_name"], number["skills"]


def get_profession_by_title(name_of_direction):
    """
    Получаем требуемые навыки для введённого направления разработки
    """
    with open("professions.json") as json_title:
        json_title_ = json_title.read()
        python_title = json.loads(json_title_)
        for title_name in python_title:
            if name_of_direction == title_name["title"]:
                return title_name["skills"]


def check_fitness(student, profession):
    """
    Получаем словарь соответствия навыков конкретного студента с желаемым направлением разработки
    """
    skills_by_number_ = set(student)
    name_of_direction_ = set(profession)
    has_skills = skills_by_number_.intersection(name_of_direction_)
    lack_skills = name_of_direction_.difference(skills_by_number_)
    percentage = len(has_skills) / len(name_of_direction_) * 100
    converted_has_skills = ", ".join(list(has_skills))
    converted_lack_skills = ", ".join(list(lack_skills))
    overall_data = {
        "has": converted_has_skills,
        "lacks": converted_lack_skills,
        "fit_percent": int(percentage)
    }
    return overall_data


# Cписок идентификационных номеров студентов и доступных направлений разработки
ids = load_students("students.json")
needed_professions = load_professions("professions.json")

# Условие при вводе недоступного идентификационного номера
pk = int(input("Введите номер студента: "))
if pk not in ids:
    quit("Нет такого студента")

# Выводим имя студента и навыки, которые у него есть
name_by_number, skills_by_number = get_student_by_pk(pk)
amount_of_skills = ", ".join(skills_by_number)
print(f"Студент: {name_by_number}, знает: {amount_of_skills}")

# Условие при вводе несуществующего направления
name_of_direction = input(f"Выберите специальность для оценки студента {name_by_number}: ")
if name_of_direction not in needed_professions:
    quit("У нас нет такой специальности")
name_of_direction_ = get_profession_by_title(name_of_direction)

# Выводим финальный результат
final_info = check_fitness(skills_by_number, name_of_direction_)
print(f"Пригодность {final_info['fit_percent']}")
print(f"{name_by_number} знает {final_info['has']}")
print(f"{name_by_number} не знает {final_info['lacks']}")
