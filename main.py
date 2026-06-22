from register import register

while True:
    print("\n=== MENU===")
    print("1. Register")
    print("2. Exit")

    choice = input("choose: ")

    if choice == "1":
        register()

    elif choice =="2":
        break

    else:
        print("invalid choice")