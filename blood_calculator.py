def interface():
    print("My Program")
    print("Options:")
    print("1 - HDL")
    print("2 - LDL")
    print("3 - Total Cholesterol")
    print("9 - Quit")
    choice = input("Enter your choice: ")
    while choice:
        if choice=='9':
            return
        elif choice=='1':
            HDL_driver()
        elif choice=='2':
            LDL_driver()
        elif choice=='3':
            TC_driver()
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

def check_LDL(LDL_val):
    if LDL_val < 130:
        return "Normal"
    elif LDL_val >= 130 and LDL_val <= 159:
        return "Borderline High"
    elif LDL_val >= 160 and LDL_val <= 189:
        return "High"
    else:
        return "Very High"

def LDL_driver():
    LDL_val = accept_input("LDL")
    result_output("LDL", LDL_val, check_LDL(LDL_val))

def check_total_cholesterol(TC_val):
    if TC_val < 200:
        return "Normal"
    elif TC_val >= 200 and TC_val <= 239:
        return "Borderline High"
    else:
        return "Very High"

def TC_driver():
    TC_val = accept_input("Total Cholesterol")
    result_output("Total Cholesterol", TC_val, check_total_cholesterol(TC_val))

interface()


    
