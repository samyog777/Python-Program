positive_count = 0
negative_count = 0
zero_count = 0

while True:
    num = float(input("Enter a number (or 0.1 to stop): "))
    if num == 0.1:
        break
    elif num == 0:
        zero_count += 1
    elif num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1

print("Count of positive numbers entered:", positive_count)
print("Count of negative numbers entered:", negative_count)
print("Count of zero numbers entered:", zero_count)
