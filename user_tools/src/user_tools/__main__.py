""" user tools app """

import random

from user_tools.args import get_args

def append_chars_to_pool(
    first_letter: str,
    last_letter: str,
    pool: list[str]) -> None:
    """ append chars to the char pool """

    for code in range(ord(first_letter), ord(last_letter) + 1):
        pool.append(chr(code))


if __name__ == "__main__":

    args = get_args()

    char_pool: list[str] = []

    append_chars_to_pool('0', '9', char_pool)
    append_chars_to_pool('A', 'Z', char_pool)
    append_chars_to_pool('a', 'z', char_pool)

    char_pool.append('!')
    char_pool.append('@')
    char_pool.append('%')
    char_pool.append('*')
    char_pool.append('_')
    char_pool.append('-')

    generated_password = []

    for _ in range(args.password_length):
        char_pool_index = random.randrange(0, len(char_pool))
        generated_password.append(char_pool[char_pool_index])

    print("".join(generated_password))

    # print(len(char_pool))
    # print(len("Lucas"))
    # print(char_pool.__len__())
    # print("Lucas".__len__())
