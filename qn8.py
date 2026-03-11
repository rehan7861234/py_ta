numbers=[5,8,12,3,9]
i=0
largest=numbers[0]
while i<len(numbers):
    if numbers[i]>largest:
        largest=numbers[i]
    i+=1
print("largest number is",largest)
