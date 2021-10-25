n_of_tries = 3
i = 0
secret_key = '1324'
while i < n_of_tries:

    print('Please insert The secret key:')

    a = input()

    if a == secret_key:
        print('Congrats! UNLOCK')
        break
    else:
        i = i + 1
        if i == n_of_tries:
            print('TOO MANY FAILED ATTEMPTS')
        else:
            print('Wrong key, try again')
