numbers = [121,122,123,124,125]

print(numbers)
print(numbers[0])
print(numbers[4])
print(numbers[len(numbers)-1])
print(numbers[-1])
numbers[0] = 120
print(numbers)

numbers.append(126)
print(numbers)

numbers.insert(1,121)
print(numbers)

numbers.remove(126)
print(numbers)

removed = numbers.pop()
print(removed)
print(numbers)

numbers = [128,122,125,120,123]

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(numbers.index(122))

numbers.extend([131,132,133])
print(numbers)

lst1 = [1,2,3]
lst2 = [4,5,6]
lst3 = lst1+lst2
print(lst3)
print(120  in numbers)
print(120 not in numbers)

print(numbers[1:3])

print(numbers.count(120))