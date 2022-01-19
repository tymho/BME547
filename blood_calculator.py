def interface():
    print("My Program")
    print("Options:")
    print("9 - Quit")
    choice = input("Enter your choice: ")
    while choice:
        if choice=='9':
            return
        choice = input("Enter your choice: ")
   
interface()
