# for i in range(1,6,2):
#     print(i)

# for i in range(0,6,2):
#     print(i)


# for i in range(10, 0, -1):
#     print(i)

lst = [10,20,30,40,50]

for i in range(0, len(lst)):
    print(lst[i])

for i in range(len(lst)-1, -1, -1):
    print(lst[i])

lst1= []

for i in lst:
    print(i)
    if i %2 == 0:
        lst1.append(i)

print(lst1)


name = "Python"

for c in name:
    print(c)

listN = [1,2,3,4,5]

for i in listN:
    if i == 2:
        print(i)
        # break
        # continue
    print(i)