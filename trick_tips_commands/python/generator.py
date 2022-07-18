import sys
import os


nums = [i for i in range(10000000)]
def fnc(nums):
    for i in nums:
        yield i * i
    
val = fnc(nums)
print(sys.getsizeof(val))
new_list = list(val)
print(sys.getsizeof(new_list))
# print(val)

# for i in val:
#     print(i)
