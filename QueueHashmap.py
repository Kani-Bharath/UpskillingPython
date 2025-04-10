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

#DIcttionar comprehension

myMap = {i : 2*i for i in range (3)}
print(myMap)

#looping through maps

myMap = {"alice": 90, "bob": 70}
for key in myMap:
    print(key,myMap[key])

for val in myMap.values():
    print(val)

for key, val in myMap.items():
    print(key,val)

#Tuples are like arrays but immutable

tup = (1,2,3)
print(tup)
print(tup[0])
print("check tup")
print(tup[-1])

#Can't modify

#tup[0] = 0

#Can be used as key for hashmap/set

myMap = {(1,2):3}
print(myMap[(1,2)])

mySet = set()
mySet.add((1,2))

print((1,2)in mySet)

#Lists can't be keys
#myMap[[3,4]] = 5
