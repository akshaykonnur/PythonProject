

def student_details(name,course='python'):
    print('name: ', name)
    print('course: ', course)
student_details('Akee')
student_details(name = 'Priya', course = 'Data Science')

def calculate_total(*args):
    return sum(args)
print(calculate_total(80,75,90,85,70))

def calculate_average(*args):
    return sum(args)/len(args)
print(calculate_average(80,75,90,85,70))

def student_result(name,*args):
    total = calculate_total(*args)
    average = calculate_average(*args)
    return total, average, name
total, average, name = student_result('Akee',80,75,90,85,70)

print("Name: ", name)
print("Total: ", total)
print("Average: ", average)

def get_result(average):
    if average >= 40:
        return 'Pass'
    else:
        return 'Fail'

result = get_result(average)
print("Result: ", result)