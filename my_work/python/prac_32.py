from faker import Faker
import random
import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta

fake = Faker("en_in")
Faker.seed(42)
departments = ['HR', 'Finance', 'Engineering', 'Marketing', 'Sales']
def generate_employee_data(num_records):
    data = []
    id =  0
    for _ in range(num_records):
        id += 1
        name = fake.name()
        department = random.choice(departments)
        salary = round(random.uniform(30000, 120000), 2)
        phone_number = fake.phone_number()
        date_of_birth = fake.date_of_birth(minimum_age=22, maximum_age=65)
        date_of_joining = fake.date_between(start_date='-10y', end_date='today')
        age = relativedelta(datetime.now(), date_of_birth).years 
        email = fake.email()
        data.append((id, name, age, department, salary, phone_number, date_of_birth, date_of_joining, email))
    return data

if __name__ == "__main__":
    num_records = 1000
    employee_data = generate_employee_data(num_records)
    df = pd.DataFrame(employee_data, columns=['ID', 'Name', 'Age', 'Department', 'Salary', 'Phone Number', 'Date of Birth', 'Date of Joining', 'Email'])
    print(df)