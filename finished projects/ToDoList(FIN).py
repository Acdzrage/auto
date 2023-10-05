List = []

def Start_App():
    print('Hi, Would you like to start your App?')
    start_cmd = input('> ')
    while start_cmd.lower() != 'yes' and start_cmd.lower() != 'quit':
        print('''ok let me know when you're ready''')
        start_cmd = input('> ')
    if start_cmd.lower() == 'quit':
        print('OK Bye!')
        quit()
    else:
        App()



def Add():
    added_Task = input(f'''what task do you want to add?
Type "q" to stop adding tasks
> ''').lower()
    while True:
        if added_Task != 'q':
            List.append(added_Task)
            added_Task = input('> ')
        else:
            break
        

def Remove():
    if len(List) != 0:
        show_list()
        while True:
            removed_Task = input(f'''Select the number of the Task you want to delete.
Type "q" to stop removing Tasks
> ''')
            if removed_Task != 'q':
                try:
                    int(removed_Task)
                    if int(removed_Task) > len(List) or int(removed_Task) < 1:
                        print('Type a valid number')
                    else:
                        del List[int(removed_Task) - 1]
                        print(f'''Here's the new List:''')
                        show_list()
                except ValueError:
                    print('Write a number next time')
            else:
                break
    else:
        print('The List is empty') 



def get_command():
    print("Welcome to the main menu")
    command = input(f'''what would you like to do?
> ''')
    return command



def show_list():
    if len(List) == 0:
        print('The List is empty')
    else:
        num = 1
        for i in List:
            print(f'''{num}. {i.title()}''')
            num += 1


def App():
    while True:
        command = get_command()
        if command.lower() == 'quit':
            Start_App()
            break
        elif command.lower() == 'add':
            Add()
        elif command.lower() == 'remove':
            Remove()
        elif command.lower() == 'show list':
            show_list()
        else:
            print('''I'm Sorry, This is an invalid command. Try again.''')
        

if __name__ == "__main__":
    Start_App()


# This is a To Do List Application
# You can add, remove, and see your list. It also has a start function, something like a start screen