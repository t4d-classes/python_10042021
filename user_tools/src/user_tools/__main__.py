""" user tools app """

import random


if __name__ == "__main__":

    password_length = int(input("Please enter a password length: "))
    print("Password length: " + str(password_length))

    char_pool = []

    char_pool.append('A')
    char_pool.append('B')
    char_pool.append('C')
    char_pool.append('1')
    char_pool.append('2')
    char_pool.append('3')

    # print(len(char_pool))
    # print(char_pool)
    # print(",".join(char_pool))

    generated_password = []

    for _ in range(password_length):
        char_pool_index = random.randrange(0, len(char_pool))
        generated_password.append(char_pool[char_pool_index])

    print("".join(generated_password))



