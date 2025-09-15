import datetime
from colorama import Fore, Style, init

init(autoreset=True)

tasks=[]

def show_menu():
    print(f"\n{Fore.CYAN}✨ Welcome to Your Awesome Personal To-Do List ✨")
    print("1. ✍ Add a new task with a deadline ⏰(because you got stuff to do!)")
    print("2. See your Tasks 📃")
    print("3. Mark a task as DONE ✔")
    print("4. Delete a task (bye-bye procrastination!👋)")
    print("5. Exit (but you got this 🐱‍🏍)")
def add_task():
    print(f"\n{Fore.LIGHTGREEN_EX}Let's make life easier! 😍")
    category = input("👉🏼 Category(Work / Personal / Study): ").strip()
    description = input("✍🏼 What's the task you wanna crush today?: ").strip()
    due_date_str = input("🗓 Enter due date (YYYY-MM-DD): ").strip()
    try:
        due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
    except ValueError:
        print(Fore.RED + "🚨 Invalid date format! Please use YYYY-MM-DD.")
        return
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H : %M : %S")
    task = {
        'category': category,
        'description': description,
        'added_at': timestamp,
        'due_date': due_date,
        'status': 'Pending'
    }
    tasks.append(task)
    print(Fore.GREEN + "🎉 Yay! Task added with a deadline! You're a rockstar! 😎")

def show_tasks():
    print(f"\n{Fore.MAGENTA}Here's what's on your plate today 📜:")
    if len(tasks) == 0:
        print(Fore.YELLOW + "Nothing yet... Time to add something fun or important!")
    else:
        today = datetime.date.today()
        for index, task in enumerate(tasks, start=1):
            due = task['due_date']
            status = task['status']
            status_display = Fore.GREEN + "DONE ✔" if status == 'Done' else Fore.YELLOW + "Pending ⏳"
            overdue_note = ""
            if status == 'Pending' and due < today:
                overdue_note = Fore.RED + "Overdue! ⏰"
            print(f"{Fore.BLUE}{index}.[{task['category']}]{task['description']} (added: {task['added_at']}, Due: {due}) - {status_display}{overdue_note}")
def mark_done():
    show_tasks()
    if len(tasks) == 0:
        return
    try:
        task_num = int(input("\nWhich task did you finish? Type the number 👉🏼 : "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['status'] = 'Done'
            print(Fore.GREEN + "🎉 Woohoo! Task marked as DONE ✔")
        else:
            print(Fore.YELLOW + "🧐 That number doesn't look right. Try again..?")
    except ValueError:
        print(Fore.YELLOW + "🚧 Please type a number next time 😛")
def delete_task():
    show_tasks()
    if len(tasks) == 0:
        return
    try:
        task_num = int(input("\nWhich one you want to delete? Type the number 👉🏼 "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(Fore.RED + f"🎇 Boom! Removed: [{removed['category']}] {removed['description']}. You're killing it! 🎊")
        else:
            print(Fore.YELLOW + "Hmm 🤔, that nnumber doesn't look right. Try again?")
    except ValueError:
        print(Fore.YELLOW + "⚠ Oops, please type a number next time 😅")

#Main Program Loop
while True:
    show_menu()
    choice = input("\nWhat's your choice (1-5)? ").strip()
    if choice == '1':
        add_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        mark_done()
    elif choice == '4':
        delete_task()
    elif choice == '5':
        print(Fore.CYAN + "\n👋 Catch ya later! Keep slaying those tasks 🔥")
        break
    else:
        print(Fore.YELLOW + "😀 Pick 1, 2, 3, 4, or 5 -easy peasy 😜")