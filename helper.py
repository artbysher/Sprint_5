from faker import Faker

faker = Faker()

def create_user_credentials(domain='ya.ru'):
    name = faker.name()

    name_str = name.replace(" ","")
    random_number = faker.random_number(digits=3)
    email = f"{name_str}{random_number}@{domain}"

    password = faker.password(length=6, special_chars=False, digits=True, upper_case=False, lower_case=False)
    return name, email, password  # Возвращаем кортеж (name,email, password)

