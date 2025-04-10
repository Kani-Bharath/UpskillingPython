#Can modify objects but not reassign 
#unless using nonlocal keyword

def double(arr,val):
    def helper():
        #Modifying array works
        for i, n in enumerate(arr):
            arr[i] *= 2
        # will only modify val in the helper scope
        #val *= 2

        nonlocal val
        val *= 2
    helper()
    print(arr,val)

nums = [1,2]
val = 3

double(nums,val)