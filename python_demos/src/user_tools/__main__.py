""" user tools app """

from user_tools.args import get_args

from user_tools.password_generator import PasswordGenerator


def password_generator_tool() -> None:
    """ password generator tool """

    args = get_args()

    if args.command_name == "generate_password":

        password_generator = PasswordGenerator(
            not args.exclude_numbers,
            not (args.exclude_letters or args.exclude_uppercase_letters),
            not (args.exclude_letters or args.exclude_lowercase_letters),
            not args.exclude_symbols,
        )

        print(password_generator.generate_password(args.password_length))

    elif args.command_name == "generate_passwords":

        password_generator = PasswordGenerator(
            not args.exclude_numbers,
            not (args.exclude_letters or args.exclude_uppercase_letters),
            not (args.exclude_letters or args.exclude_lowercase_letters),
            not args.exclude_symbols,
        )

        generated_passwords = password_generator.generate_passwords(
            args.number_of_passwords,
            args.password_length)

        print("\n".join(generated_passwords))

    else:

        print("Invalid command")


if __name__ == "__main__":

    password_generator_tool()