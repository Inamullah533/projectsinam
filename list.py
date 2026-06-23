l =[78,34,87,123,19,863,678,19,780]
largest= l[0]
sec_largest = l[0]

for i in l:
    if i > largest:
        sec_largest = largest
        largest = i
    elif i > sec_largest:
        sec_largest = i
print(largest , sec_largest)