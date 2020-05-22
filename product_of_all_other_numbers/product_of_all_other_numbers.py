'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # #iterate over the list of integers
    # multip all numbers together 
    # if number is a zero at each index divide the value from total 

    firstNumber = 1 
    zeroNumber = 1 

    for value in arr:
        # if value is not equal to 0
        if value != 0:
            # first number is multiplied and equal to the value 
            firstNumber *= value
              # and the zero number is multiplied and equal to the value 
            zeroNumber *= value
        else:
            # or else the first number is multiplied and equal to the value 
            firstNumber *= value
            # and the zero number is multiplied and equal to 1 
            zeroNumber *= 1

# the new array will be an empty array 
    new_arr = []

# create the next for loop 
    for i in arr:
        if i == 0:
            new_arr.append(zeroNumber)
        else:
            divide = firstNumber // i
            new_arr.append(divide)      

    return new_arr                  


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
