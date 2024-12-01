# Welcome Prompt
print("Welcome To Your Do-To List")

# Start The List
tasks_list = ["My To-Do List"]
for index, task in enumerate(tasks_list[1:], start=1):  # Skip the Title
    print(f"{index}. {task}")

# Menu
while True:
    print("")
    print("Select From the Menu: ")
    print("Add Tasks")
    print("View Tasks")
    print("Delete Tasks")
    print("Quit")
    print("")
    
    user_input = (input(""))  
      

    #   ADDING A TASK

    if user_input == "Add Tasks":
        while True:
            print("")
            try:
                user_input = input("What task would you like to add? ")
                print("")
                if user_input =="":
                    print("Error: Task cannot be empty")
                elif user_input in tasks_list:
                    print("Error: Already exist")
                else:
                    tasks_list.append(user_input)
                    print("Your Do-To List")
                    for index, task in enumerate(tasks_list[1:], start=1):
                        print(f"{index}. {task}")
                        continue
            except Exception as e:
                print(f"An error occurred: {e}")
                
            answer = input("Do you want to add another tasks? Yes or No? ")
            if answer == "No":
                break
    
#   VIEW A TASKS    

    elif user_input == "View Tasks":
        while True:
            try:
                if len(tasks_list) > 1 :
                    print("Your Do-To List")
                    for index, task in enumerate(tasks_list[1:], start=1):  # Start at 1 to skip the Title 
                        print(f"{index}. {task}")
                    print("")
                else:
                    raise ValueError("No tasks to view.")
            except ValueError as e:
                print(f"Error: {e}")
            finally:
                answer2 = input("Would you like to exit? Yes or No ")
                if answer2 == "Yes":
                    break
                
                
                
#   DELETE A TASK

    elif user_input == "Delete Tasks":
        try:
            if len(tasks_list) > 1:
                print("Your Do-To List")
                for index, task in enumerate(tasks_list[1:], start=1):
                    print(f"{index}. {task}")
                
                while True:
                    try:
                        task_number = input("What number on your To-Do List would you like to delete? ") #  Initiate The task_number
                        task_number = int(task_number)
                        
                        if 1 <= task_number < len(tasks_list):    #   Skip the heading in the task list
                            del tasks_list[task_number]
                            for index, task in enumerate(tasks_list[1:], start=1):
                                print(f"{index}. {task}")
                                print("")
                                break
                        else:
                            print ("That list number does not exist")
                            break
                    except:
                        raise ValueError("No tasks to delete.")
                    
                    answer2 = input("Would you like to exit? Yes or No: ")
                    if answer2 == "Yes":
                        break
                    elif answer2 == "No":
                        continue
            else:
                raise ValueError("No tasks to delete.")
                
        except ValueError as e:
            print(f"Error: {e}")  
            
#   QUIT

    elif user_input == "Quit":
            break
    else:
        print("Error: Invalid option. Please select from the menu.")