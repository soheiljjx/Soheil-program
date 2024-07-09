def average(*args):
    min = args[0]
    max = args[0]
    for i in args[1:]:
        if i < min :
            min = i
        elif i > max :
            max = i
    return (max,min)

print(average(4,32,2,9,6))