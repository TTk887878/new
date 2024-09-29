import s_taper
from s_taper.consts import *
from faker import Faker
import random

fake = Faker("ru_RU")
# schema = {
#     "user_id": INT + KEY,
#     "name": TEXT,
#     # "age": FLT,
#     # "first": BLN
# }
schema = {
    "user_id": INT + KEY,
    'name': TEXT,
    "age": INT
}
users = s_taper.Taper('users', 'data.db').create_table(schema)
user = users.write([1, "name", 1])
# for p in range(2,3001):
#     users.write([p,fake.first_name(),random.randint(1,878788787877)])
user_1 = users.read("user_id", 644)
print(user_1)
users_1 = users.read_all()
anq = 0
for usa in users_1:
    if 1000000<=usa[2] <= 1000000000000:
        print(usa)
        anq += 1

print(f"{anq}-людей")
print(f"процент людей {round(anq/len(users_1)*100,2)}")
users.delete_row("user_id",15)