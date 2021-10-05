"""
Class for Generating a Password
"""

# functional programming - higher-order function pattern
# def configure_password_generator(
#         include_numbers: bool,
#         include_uppercase: bool,
#         include_lowercase: bool,
#         include_symbols: bool):

#     # configure logic
#     char_pool = []

#     def generate_password(password_length: int = 10):

#         # used char pool
#         return char_pool

    
#     return generate_password


# my_pass_generator = configure_password_generator(True, False, True, True)

# my_pass_generator(10)
    

from random import randrange

class PasswordGenerator:
    """
    Password Generator
    """

    def __init__(
        self,
        include_numbers: bool,
        include_uppercase: bool,
        include_lowercase: bool,
        include_symbols: bool):

        self.char_pool: list[str] = []

        self.include_numbers = include_numbers
        self.include_uppercase = include_uppercase
        self.include_lowercase = include_lowercase
        self.include_symbols = include_symbols

        self.__initialize_char_pool()


    def __append_chars_to_pool(
        self,
        first_letter: str,
        last_letter: str) -> None:
        """ append chars to the char pool """

        for code in range(ord(first_letter), ord(last_letter) + 1):
            self.char_pool.append(chr(code))


    def __initialize_char_pool(self) -> None:
        """ initialize the pool of characters """

        if self.include_numbers:
            self.__append_chars_to_pool('0', '9')

        if self.include_uppercase:
            self.__append_chars_to_pool('A', 'Z')

        if self.include_lowercase:
            self.__append_chars_to_pool('a', 'z')

        if self.include_symbols:
            self.char_pool.append('!')
            self.char_pool.append('@')
            self.char_pool.append('%')
            self.char_pool.append('*')
            self.char_pool.append('_')
            self.char_pool.append('-')


    def generate_password(self, password_length: int = 10) -> str:
        """
        generate and return the password
        following the configured rules
        """

        self.

        generated_password = []

        char_pool_len = len(self.char_pool)

        for _ in range(password_length):
            char_pool_index = randrange(0, char_pool_len)
            generated_password.append(self.char_pool[char_pool_index])

        return "".join(generated_password)

    
    def generate_passwords(
        self,
        number_of_passwords: int,
        password_length: int = 10) -> list[str]:

        """
        generate and return multiple passwords
        following the configured rules
        """

        # generated_passwords = []

        # for _ in range(number_of_passwords):
        #     generated_passwords.append(
        #         self.generate_password(password_length))

        # return generated_passwords

        # list comprehension
        return [
            self.generate_password(password_length)
            for _ in range(number_of_passwords)
        ]
