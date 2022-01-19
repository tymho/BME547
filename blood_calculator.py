def interface():
    print("My Program")
    print("Options:")
    print("1 - HDL")
    print("9 - Quit")
    choice = input("Enter your choice: ")
    while choice:
        if choice=='9':
            return
        elif choice=='1':
            HDL_driver()
        choice = input("Enter your choice: ")

def accept_input(test_name):
    entry = input("Enter the {} test result: ".format(test_name))
    return int(entry)

def result_output(test_name, test_val, test_class):
    print("The test value of {} for {} is {}".format(test_name, test_val, test_class))
    return

def check_HDL(HDL_val):
    if HDL_val >= 60:
        return "Normal"
    elif HDL_val >= 40 and HDL_val < 60:
        return "Borderline Low"
    else:
        return "Low"

def HDL_driver():
    HDL_val = accept_input("HDL")
    result_output("HDL", HDL_val, check_HDL(HDL_val))
    
interface()


    
