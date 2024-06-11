import random as r
levels = [1000, 2000, 5000, 10000, 20000, 50000, 120000, 320000]
operation = ['+', '-', '*', '/', '%', '//', '**']
total_amount = 0
for i in range(len(levels)):
    a = r.randint(1, 10)
    b = r.randint(1, 10)
    applied_operation = r.choice(operation)
    ans = eval(f'{a} {applied_operation} {b}')
    print(f'\nQuestion for Rs {levels[i]}:')
    print(f'What is {a} {applied_operation} {b}')
    ans_list = [r.randint(1, 100), r.randint(1, 100), r.randint(1, 100), ans]
    r.shuffle(ans_list)
    print(f'1. {ans_list[0]}            2. {ans_list[1]}')
    print(f'3. {ans_list[2]}            4. {ans_list[3]}')
    choice = int(input("Enter Choice(1-4): "))
    if choice == 1:
        if ans_list[0] == ans:
            print(f"You Won Rs. {levels[i]}")
            total_amount += levels[i]
        else:
            print("You Lost! Try again next time.")
            break
    elif choice == 2:
        if ans_list[1] == ans:
            print(f"You Won Rs. {levels[i]}")
            total_amount += levels[i]
        else:
            print("You Lost! Try again next time.")
            break
    elif choice == 3:
        if ans_list[2] == ans:
            print(f"You Won Rs. {levels[i]}")
            total_amount += levels[i]
        else:
            print("You Lost! Try again next time.")
            break
    elif choice == 4:
        if ans_list[3] == ans:
            print(f"You Won Rs. {levels[i]}")
            total_amount += levels[i]
        else:
            print("You Lost! Try again next time.")
            break
    else:
        print("Invalid Choice")

print("\n\nTotal Amount Won: Rs.", total_amount)
