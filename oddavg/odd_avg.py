# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases

def odd_average(num_list=[]):
    odd_list = []
    for i in num_list:
        if i % 2 != 0:
            odd_list.append(i)
    average = sum(odd_list)/(len(odd_list)+1)
    return average

print(odd_average([2,3,7,13,6]))
