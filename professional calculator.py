import math

history_list = []

def show_menu():
    print("\n-----MAIN MENU-----")
    print("\n1-Perform New Operation")
    print("2-View History")
    print("3-Delete a Specific Record")
    print("4-Reset History")
    print("5-Close")

    while True:
        choice = input("Please Select the Operation You Want to Perform : ")
        try:
            if choice in ["1", "2", "3", "4", "5"]:
                return choice
            else:
                print("Invalid selection")
                print("Please write the number of the operation you want to perform from the menu")
        except Exception as h:
            print(f"Error! {h} Please repeat the process")

def calculator():
    print("--Select the Operation to be Performed--")
    print("1-Addition\n2-Subtraction\n3-Multiplication\n4-Division\n5-Power\n6-Modulo\n7-Factorial")
    operation = input("Select (1-7) : ").strip()

    while True:
        try:
            y = int(input("How many numbers do you want to enter for the operation : "))
            if operation in ["1","2","3","4","5","6"] and y >= 2:
                break
            elif operation == "7" and y >= 1:
                break
            else:
                print("Please enter at least 2 numbers")
        except ValueError:
            print("Please enter an integer")

    numbers_list = []

    for x in range(y):
        while True:
            try:
                z = float(input("Enter the number you want to be processed = "))
                numbers_list.append(z)
                break
            except ValueError:
                print("Please enter an integer or a decimal number")

    result = numbers_list[0]

    if operation == "1":
        result = sum(numbers_list)

    elif operation == "2":
        for s in numbers_list[1:]:
            result -= s

    elif operation == "3":
        for s in numbers_list[1:]:
            result *= s

    elif operation == "4":
        for s in numbers_list[1:]:
            if s != 0:
                result /= s
            else:
                return "The divisor cannot be 0"

    elif operation == "5":
        for s in numbers_list[1:]:
            result **= s
    
    elif operation == "6":
        for s in numbers_list[1:]:
            if s != 0:
                result %= s
            else:
                return "Modulo of 0 cannot be taken"

    elif operation == "7":
        print("\n---Advanced Factorial Results---")
        for s in numbers_list:
            if s < 0:
                print(f"{s} is negative, so the operation cannot be performed")
            elif s.is_integer():
                f_res = math.factorial(int(s))
                print(f"{int(s)}! = {f_res}")
                history_list.append(float(f_res))
            else:
                g_res = math.gamma(s + 1)
                history_list.append(round(g_res, 4))
        return "Factorial operation completed"
    else:
        return "Please enter one of the numbers on the screen"
    
    history_list.append(result)
    return f"The results of the operations you performed = {result}"

def repeat_operation():
    while True:
        result_message = calculator()
        print(result_message)
        soru = input("Do you want to perform another operation?\n1-Yes\n2-No\n")
        try:
            if soru == "1":
                continue
            elif soru == "2":
                print("Returning to Main Menu...")
                break
            else:
                print("You entered an invalid selection. Returning to Main Menu...")
                break
        except Exception as e:
            print(f"An error occurred: {e}")

def app_center():
    while True:
        main_choice = show_menu()

        if main_choice == "1":
            print("Connected to New Operation section")
            repeat_operation()

        elif main_choice == "2":
            print("\n----OPERATION HISTORY---")
            if not history_list:
                print("There is no saved operation yet")
            else:
                for rank, answer in enumerate(history_list, 1):
                    print(f"{rank}. operation result : {answer}")

        elif main_choice == "3":
            if not history_list:
                print("Your history list is empty")
                print("No data found to delete")
            else:
                want_to_see = input("Would you like to see your history list before deleting? (y/n) : ").lower()
                if want_to_see in ["y", "yes"]:
                    print("\n----CURRENT HISTORY----\n")
                    for rank, answer in enumerate(history_list, 1):
                        print(f"{rank}. operation = {answer}")
                    print("________________________\n")
                else:
                    print("Okay, proceeding without looking...")

                try:
                    to_be_deleted = int(input("Enter the operation number you want to delete : "))
                    deleted_value = history_list.pop(to_be_deleted - 1)
                    print(f"Operation number {to_be_deleted} ({deleted_value}) has been successfully deleted")
                except:
                    print("Error! Please enter a valid number from the list")
                    
        elif main_choice == "4":
            if not history_list:
                print("History is already empty, nothing to clear")
            else:
                is_sure = input("All history will be deleted. Are you sure you want to proceed? (y/n) : ").lower()
                if is_sure in ["y", "yes"]:
                    history_list.clear()
                    print("Operation history completely cleared")
                else:
                    print("Operation cancelled")
                    print("Returning to main menu")

        elif main_choice == "5":
            print("Program closing...")
            break

if __name__ == "__main__":
    app_center()