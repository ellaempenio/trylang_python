# Task 1: Print student name at an inputted specific index in a set
students = {'John', 'Maria', 'David', 'Samantha'}
index = int(input("Enter index: "))  # get the index as input
students_list = list(students)  # convert set to list
if index >= 0 and index < len(students_list):  # check if index is valid
    print(students_list[index])
else:
    print("Invalid index")

# Task 2: Get the average of all even numbers in a tuple
numbers = (1, 4, 7, 10, 13, 16)
even_numbers = []
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

if len(even_numbers) > 0:
    total = 0
    for num in even_numbers:
        total += num
    average = total / len(even_numbers)
    print("Average of even numbers:", average)
else:
    print("No even numbers found")

# Task 3: Print names of people older than 19 in a dictionary
people = {'users': {'John': 19, 'Emily': 21, 'Sarah': 25, 'Tom': 18}}
for name, age in people['users'].items():
    if age > 19:
        print(name)

# Task 4: Print numbers that appear more than once in a tuple
numbers = (1, 3, 2, 4, 3, 1, 2, 5, 10)
repeated = []
for i in range(len(numbers)):
    count = 0
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1
    if count > 1 and numbers[i] not in repeated:
        repeated.append(numbers[i])

print("Numbers that appear more than once:", repeated)

# Task 5: Print student with the lowest score
students_scores = [('John', 85), ('Maria', 92), ('Tom', 76), ('Sarah', 90)]
min_score = students_scores[0][1]
min_student = students_scores[0][0]

for student, score in students_scores:
    if score < min_score:
        min_score = score
        min_student = student

print(f"Student with the lowest score: {min_student} ({min_score})")
