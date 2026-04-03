arr = [1,2,3,4,5]
print(arr)

print(arr[0])
print(arr[1])
print(arr[2])
print(arr[3])
print(arr[4])   


# print first and last element of the array
print(arr[0], "fist element")
print(arr[-1],"last element")
print(arr[4],"last element")

# print all the element of the array using loop
#for i in arr:
#    print(i)

# print all the element of the array using loop and index
for i in range(len(arr)):
    print(arr[i])

# print only even element of the array
for i in arr:
    if i %2 ==0:
        print(f"number {i} is even")

# Basic operations on array
arrr = [1,2,3]
# add element to array
arrr.append(4)
print(arrr)
# remove lasrt element from array
arrr.pop()
print(arrr)
# insert element at specific index
arrr.insert(1,5)
print(arrr)


# sum of list element
list = [1,2,3,4,5]
sum = 0
for i in list:
    #sum = sum + i
    sum += i
print("sum of list element: ",sum)

# find maximum element in the list
list = [11,2,12,4,6,10]
max = list[0]
for i in list:
    if i > max:
        max = i
print("maximum element in the list: ",max)


# cound event numbers
list = [1,2,3,4,5,6,7,8,9]
count = 0
for i in list:
    if i %2 ==0 :
        count +=1
        print(f"number {i} is even")
print("count of even numbers: ",count)
count_odd = 0
for j in list:
    if j %2 !=0 :
        count_odd +=1
        print(f"number {j} is odd")
print("count of odd numbers: ",count_odd)


list_arr= [1,2,3,4,5]
rev_list = []
r_l = []
for i in range(len(list_arr)-1,-1,-1):
    rev_list.append(list_arr[i])
print("reverse list: ",rev_list)

for j in range(len(list_arr)-1,-1,-2):
    r_l.append(list_arr[j])
print("reverse list: ",r_l)


list_a = [1,2,4,3,5,6,10,12]
larget_el = list_a[0]
# for i in list_a:
#     if i > larget_el:
#         larget_el = i
# print("largest element in the list: ",larget_el)
# second_larget = list_a[0]
# for j in list_a:
#     if j > second_larget and j < larget_el:
#         second_larget = j
# print("second largest element in the list: ",second_larget)


# find third largest element in the list
largest = list_a[0]
second_largest = list_a[0]
third_largest = list_a[0]
for i in list_a:
    if i > largest:
        third_largest = second_largest
        second_largest = largest
        largest = i
    elif i > second_largest and i != largest:
        third_largest = second_largest
        second_largest = i
    elif i > third_largest and i != second_largest and i != largest:
        third_largest = i
print("largest element in the list: ",largest)
print("second largest element in the list: ",second_largest)
print("third largest element in the list: ",third_largest)  