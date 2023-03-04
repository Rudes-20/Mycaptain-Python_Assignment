numl = []
positive_nums = []
n = int(input("Enter the size of the list: "))
for i in range(n):
    num = int(input("Enter a number: "))
    numl.append(num)
for num in numl:
    if num > 0:
        positive_nums.append(num)
print("The positive numbers in the list are:", positive_nums)
