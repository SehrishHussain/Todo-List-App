
while True:
    user_action = input("Type add, edit, show, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo: ') + "\n"

            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()  # returns a list
            file.close()

            # new_todos = []
            # for item in todos:
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)
            # new_todos = [item.strip('\n') for item in todos]
            # print(todos)

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)
        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            todos[number] = input("Enter a todo: ")
        case 'complete':
            number = int(input('Number of todo to complete: '))
            todos.pop(number-1)
        case 'exit':
            break
print ("bye")