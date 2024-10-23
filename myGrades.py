print("Grade Calculator")

def average(marks):
    sum = 0
    for i in marks:
        sum += i

    return sum / len(marks)

def total(marks):
    sum = 0
    for x in marks:
        sum += x

    return sum

marks =[24, 13, 24, 53, 34, 97]
print(f"Your total marks {total(marks)} and you've scored an average of {average(marks)}")
