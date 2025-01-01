my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print('my_dict: ', my_dict)
print('my_dict["name"]: ', my_dict['name'])

person = {'name': 'John', 'age': 30, 'city': 'New York'}
print('person: ', person)
print('person["name"]: ', person['name'])

name = person['name']
print('name: ', name)

person['age'] = 31
print('person: ', person)

person['gender'] = 'male'
print('person: ', person)

print(f"name: {person['name']}, age: {person['age']}, city: {person['city']}")

country = person.get('country', 'Unknown') # 키가 없으면 기본값 반환 (get 사용)
print('country: ', country)

person_detail = {'country': '대한민국'}
person.update(person_detail)
print('person detail update: ', person)

print(person.keys())

del person['gender']
print('person gender delete: ', person)

person.clear()
print('person clear: ', person)