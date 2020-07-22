from name_function import formatted_name

print("Please enter the first and last name or enter x to E[x]it")

while True:
    first_name = input("Please enter the first name: ")
    if first_name == "x":
        print("Bye then")
        break

    middle_name = input("Please enter the middle name: ")
    if middle_name == "x":
        print("Bye then")
        break

    last_name = input("Please enter the last name: ")
    if last_name == "x":
        print("Bye then")
        break
    
    result = formatted_name(first_name, last_name, middle_name)
    print("Formatted name is:" + result + ". ")