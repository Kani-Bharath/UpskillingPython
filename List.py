arr = [1,2,3]

#prints the last value
print(arr[-1])

#prints the last but one 
print(arr[-2])
print(arr)



#can be used as a stack
arr.append(4)
arr.append(5)

print(arr)
#Sublist aka slicing
print("slicing")
print(arr[1:3])


arr.pop()
print(arr)

arr.insert(2,7)
print(arr)

arr[0]=0
arr[3]=0

print(arr)


n =5
arr = [1]*n
print(arr)

#Unpacking

a,b,c = [1,2,3]
print(a,b,c)


#Loop through arrays
nums = [1,2,3]

#Using index

for i in range(len(nums)):
    print(nums[i])

#Without index
for s in nums:
    print(s)

    # With index and Enumerate

for i,n in enumerate(nums):
    print(i,n)

# Loop through multiple arraye simultaneously with unpacking

nums1 = [1,3,5]
nums2 = [2,4,6]

for n1,n2 in zip(nums1, nums2):
   print(n1 , n2)

#Reverse

nums = [1,2,3]
nums.reverse()
print(nums)

#Sorting

arr= [5,4,7,3,8]
arr.sort() #Ascending order
print(arr)

arr.sort(reverse= True) #Descending order
print(arr)

arr= ["bob", "alice", "jane", "doe"]
arr.sort()
print(arr)

#Sort based on string length
arr.sort(key=lambda x : len(x))
print(arr)

arr=[i for i in range(5)]
print(arr)
arr= [i+i for i in range(5)]
print(arr)

#List comprehension
arr= [i+i for i in range(5)]
print(arr)

#2D List
arr=[[0]*4 for i in range(4)]
print(arr)

arr = [[1] * 4]  *4
print(arr)
