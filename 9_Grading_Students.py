#If the difference between the grade and the next multiple of 5 is less than 3 , round grade up to the next multiple of 5.
#If the value of grade is less than 38 , no rounding occurs as the result will still be a failing grade.

grades = [73, 67, 38, 33]
multiples_grades = []
update_grades = []

for i in grades:
    new = int(i + (5 - i) % 5)
    multiples_grades.append(new)

for x, i  in zip(grades, multiples_grades):
    print(x , i)
    if (i - x) >= 3 or x < 38:
        update_grades.append(x)
        
    else:
         update_grades.append(i)

print(update_grades)


