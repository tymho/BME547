def interface():
    print("My Program")
    print("Options:")
    print("9 - Quit")
    choice = input("Enter your choice: ")
    while choice:
        if choice=='9':
            return
        choice = input("Enter your choice: ")

def accept_input(test_name):
    entry = input("Enter the {} test result: ".format(test_name))
    return int(entry)

def check_HDL(HDL_val):
    if HDL_val >= 60:
        return "Normal"
    elif HDL_val >= 40 and HDL_val < 60:
        return "Borderline Low"
    else:
        return "Low"

    
    
