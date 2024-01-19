# salary_module.py

def add_people_and_salaries(people, salaries):
    try:
        num_people = int(input("Введите количество новых людей: "))
        for i in range(num_people):
            person_name = input(f"Введите имя {i + 1}-го человека: ").capitalize()
            person_salary = int(input(f"Введите зарплату {i + 1}-го человека: "))
            people.append(person_name)
            salaries.append(person_salary)
            print(f"{person_name} добавлен(а) с зарплатой {person_salary}")
    except ValueError:
        print("Ошибка: Введите корректные числовые значения для зарплаты.")

