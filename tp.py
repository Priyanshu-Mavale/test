def genarator():
    for i in range(8):
        yield(i)

nums=genarator()
print(nums)
for i in nums:
    print(i)

list=[1,2,3,4]
list.remove(1)
print(list)
list.