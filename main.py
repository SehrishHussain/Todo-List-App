
while True:
    user_action = input("Type add, edit, show, complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input('Enter a todo:  ') + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'show':
            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            for index, item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index + 1}-{item}"
                print(row)

        case 'edit':
            number = int(input("Number of the todo to edit: "))
            number = number - 1
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            new_todo = input("Enter a new todo: ")
            todos[number] = f"{new_todo}\n"

            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input('Number of todo to complete: '))
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            todos_to_remove = todos[number - 1].strip('\n')

            print(f"Todo {todos_to_remove} was removed from the list")
            todos.pop(number-1)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'exit':
            break

print("bye")