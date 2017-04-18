# Create a function called `odd_average` that takes a list of numbers as parameter
# and returns the average value of the odd numbers in the list
# Create basic unit tests for it with at least 3 different test cases
class OddAvg():
    def odd_average(self, num_list=[]):
        self.odd_list = []
        for i in num_list:
            if i % 2 != 0:
                self.odd_list.append(i)
        average = sum(self.odd_list)/(len(self.odd_list))
        return average

example_list = OddAvg()

print(example_list.odd_average([2,3,5,0,6,7,1]))
