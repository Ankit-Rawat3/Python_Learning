"""Given an array nums.We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example
1:

Input: nums = [1, 2, 3, 4]
Output: [1, 3, 6, 10]
Explanation: Running
sum is obtained as follows: [1, 1 + 2, 1 + 2 + 3, 1 + 2 + 3 + 4].
Example
2:

Input: nums = [1, 1, 1, 1, 1]
Output: [1, 2, 3, 4, 5]
Explanation: Running
sum is obtained as follows: [1, 1 + 1, 1 + 1 + 1, 1 + 1 + 1 + 1, 1 + 1 + 1 + 1 + 1].
Example
3:

Input: nums = [3, 1, 2, 10, 1]
Output: [3, 4, 6, 16, 17]
"""

nums=[1,2,3,4]
sum=0
num=[]
for i in nums:
    sum=sum+i
    num.append(sum)

print(num)
print(sum)

sum2=0
num2=[]
nums2 = [1, 1, 1, 1, 1]
for i in nums2:
    sum2=sum2+i
    num2.append(sum2)

print(num2)
print(sum2)

sum3=0
num3=[]
nums3 = [3, 1, 2, 10, 1]
for i in nums3:
    sum3=sum3+i
    num3.append(sum3)

print(num3)
print(sum3)