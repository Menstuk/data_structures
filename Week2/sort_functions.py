import random
import time

def insertion_sort(arr):
    # Explain the function
    """
    This function sorts an array using the insertion sort algorithm.
    """
    for i in range(0,len(arr)):  # Start from index 0
        key = arr[i]
        j = i - 1                       # This is needed for the first element, as python for does not initialize the j. Think what happens for i =0
        for j in range(i - 1, -1, -1):  # Iterate backwards
            if arr[j] > key:            
                arr[j + 1] = arr[j]     # Shift elements to the right
            else:
                break
            j -= 1                      # This is needed for the case that the key needs to be stored at the first position. 
                                        # If this does not exists, the loop will end with j = 0 and the key will be placed at j = 1.
                                        # In every other case this is overwritten by the for loop above.
        arr[j + 1] = key  # Place key in the correct position

def insert_with_time(arr):
    start = time.time() # Start the timer
    insertion_sort(arr) # Call the insertion sort
    end = time.time()   # Stop the timer
    return end - start  # Return the time taken