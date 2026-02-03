from faker import Faker
import pandas as pd

fake = Faker('en_in')
Faker.seed(42)
data = [[fake.name(), fake.address(), fake.email(),fake.phone_number()] for _ in range(100)]
df = pd.DataFrame(data, columns=['Name', 'Address', 'Email', 'Phone Number'])
print(df)