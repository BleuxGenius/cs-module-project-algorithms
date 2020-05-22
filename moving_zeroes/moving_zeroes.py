'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):

    #iterate over array to see every number
    # if number matches 0 move to the end
    # shift everything over to fill moved zero 
    # return the altered list    

    for number in arr:
        if number == 0: 
            # remove zero from the index , append zero
            # shift everything to the left by 1 (happends when you remove number)
            # increment down the for loop (done by the for loop)

            arr.remove(number)
            arr.append(0)
    return arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")