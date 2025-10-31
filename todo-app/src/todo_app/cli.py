import argparse
from todo_app.services import TodoService

def main():
    parser = argparse.ArgumentParser(description='To-Do Application CLI')
    parser.add_argument('command', choices=['add', 'list', 'remove'], help='Command to execute')
    parser.add_argument('--task', type=str, help='Task description for add/remove commands')
    
    args = parser.parse_args()
    service = TodoService()

    if args.command == 'add':
        if args.task:
            service.add_task(args.task)
            print(f'Task added: {args.task}')
        else:
            print('Error: Task description is required for adding a task.')
    
    elif args.command == 'list':
        tasks = service.list_tasks()
        print('To-Do List:')
        for task in tasks:
            print(f'- {task}')
    
    elif args.command == 'remove':
        if args.task:
            service.remove_task(args.task)
            print(f'Task removed: {args.task}')
        else:
            print('Error: Task description is required for removing a task.')

if __name__ == '__main__':
    main()