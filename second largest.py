def find_second_largest(numbers):
       max1 ,max2 = float('-inf'),float('-inf') 
       for i in numbers:
        if i > max1:
             max2 = max1
             max1 = i
        elif i > max2 and i != max1:
            max2 = i
       return max2 if max2 != float('-inf') else None
numbers = [1,2,3,4,5,6]
print("second largest:",find_second_largest(numbers))
def main():
    find_second_largest(numbers)
main()