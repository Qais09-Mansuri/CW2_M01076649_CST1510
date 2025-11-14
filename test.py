from log_hash import register_user, log_in_user

print(log_in_user())
def menu():
    print('*'* 30)
    print('*** Welcome to my system ***')
    print('1.Register')
    print('2.Log in')
    print('3.Exit')
    print('*'* 30)

def main():
    while True:
        menu()
        choice = input('> ')
        if choice == '1':
            register_user()
        elif choice == '2':
            if log_in_user():
                print('You loged in')
            else:
                print('Incorrect log in')
        elif choice == '3':
            print('Good bye!!')
            break

if __name__ == '__main__':
    main()