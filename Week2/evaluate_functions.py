from sort_functions import *

LENGTH_RATIO = 2
BASE_LENGTH = 1000
to_sort_arr1 = list(range(BASE_LENGTH,0,-1))
to_sort_arr2 = list((range(BASE_LENGTH*LENGTH_RATIO,0,-1)))

time_taken1 = insert_with_time(to_sort_arr1)
time_taken2 = insert_with_time(to_sort_arr2)

print("Reverse List, time taken for 1000 elements: ", time_taken1)
print("Reverse List, time taken for 2000 elements: ", time_taken2)


to_sort_arr3 = [random.randint(-10000, 10000) for _ in range(BASE_LENGTH)]
to_sort_arr4 = [random.randint(-10000, 10000) for _ in range(BASE_LENGTH*LENGTH_RATIO)]
time_taken3 = insert_with_time(to_sort_arr3)
time_taken4 = insert_with_time(to_sort_arr4)
print(f"Random List Time taken for {BASE_LENGTH} elements: ", time_taken3)
print(f"Random List Time taken for {BASE_LENGTH*LENGTH_RATIO} elements: ", time_taken4)