import json

file = open("students.json")
data = json.load(file)
print(data)

for student in data["Students"]:
    print(f"{student['FirstName']} {student['LastName']}") 
age_sum = 0
for student in data["Students"]:
    age_sum += int(student["Age"])
avg_age = age_sum / len(data["Students"])
print("Average age is")
print(avg_age)