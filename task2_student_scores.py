import requests
import matplotlib.pyplot as plt
names=[]
scores=[]
students=[]
total=0
url = "https://api.slingacademy.com/v1/sample-data/files/student-scores.json"
try:
    response=requests.get(url,timeout=10)
    print(response.status_code)
except requests.exceptions.RequestException:
    print("API request failed")
    exit()

data=response.json()

for user in data[:10]:
    student={
        "name":user["first_name"]+" "+user["last_name"],
        "score":user["math_score"] 
    }
    students.append(student)
for student in students:
    total=total+student["score"]
print("Total score:",total)
print("Number of students:",len(students))
average=total/len(students)
print("Average score:",average)
for student in students:
    names.append(student["name"])
    scores.append(student["score"])

plt.figure(figsize=(10, 6))
plt.barh(names,scores)
plt.xlabel("Score")
plt.ylabel("Student")
plt.title("Student Scores")
plt.show()

