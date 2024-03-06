'''
let's calculate an average value of list elements
'''

def calculate_average(arr):
    '''
    method calculates an average value
    :param arr: list of elements
    :return:    0 if the list has zero size,
                False if elements are not numbers,
                average value if ok
    '''
    count = len(arr)

    if count == 0:
        return 0

    for el in arr:
        if not isinstance(el, (int, float)):
            return False

    return sum(arr) / count


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)

nums = []
result = calculate_average(nums)
print("The average is:", result)

nums = ['abc', 7, 'asd']
result = calculate_average(nums)
print("The average is:", result)
