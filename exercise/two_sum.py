#	Gives both indexes of the two numbers that sum up to give the target number 
def twosum(num, target):
    index_list = range(len(nums))
for index in index_list:
    first_num = nums[idx]
for indx_j in range(idx + 1,len(nums)):

second_num = nums [idx_j]
num_sum = first_num + second_num
if target == num_sum:
    return [idx, idx_j]
