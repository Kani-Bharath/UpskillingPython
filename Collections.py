#Queues(double ended queue)


from collections import deque
queue =deque()
queue.append(1)
queue.append(2)
queue.append(2)
print(queue)

queue.popleft()
print(queue)
queue.appendleft(1)
print(queue)

queue.pop()
print()


#Hashset

mySet = set()
mySet.add(1)
mySet.add(2)
mySet.add(2) #No duplicates

print(1 in mySet)
print(2 in mySet)
print(3 in mySet)

mySet.remove(2)
print(2 in mySet)

#list to set
print(set([1,2,3]))

#Set comprehension

mySet={i for i in range(5)}
print(mySet)

#Hashmap(aka dict)
myMap = {}
myMap["alice"] = 88
myMap["bob"]=77
print(myMap)
print(len(myMap))

myMap["alice"] = 80
print(myMap["alice"])

print("alice" in myMap)

myMap = { "alice" : 90, "bob" : 70}
print(myMap)