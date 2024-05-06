fake_users2 = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "John"},
    {"id": 3, "role": "trader", "name": "Matt"},
]

a = list(filter(lambda user: user.get("id") == 20, fake_users2))[0]
fake_users2.append({'sd': 2, 'sdd': 123})
print(a)
