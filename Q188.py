count = 0
total_sum = 0
minimum = None
maximum = None

while True:
    user_input = input("Enter a number (or 'QUIT' to stop): ")
    
    if user_input == "QUIT":
        break
    
    num = float(user_input)
    total_sum += num
    count += 1
    
    if minimum == None or minimum > num :
        minimum = num
    if maximum == None or num > maximum:
        maximum = num

if count > 0:
    average = total_sum / count
    print(f"Sum: {total_sum}")
    print(f"Average: {average}")
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
else:
    print("No numbers were entered.")