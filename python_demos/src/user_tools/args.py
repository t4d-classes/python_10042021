""" parse command-line arguments """

from argparse import ArgumentParser, Namespace

def get_args() -> Namespace:
    """ parse and return command-line arguments """

    parser = ArgumentParser()

    parser.add_argument(
        "command_name",
        type=str,
        help="Command to execute.")

    parser.add_argument(
        "-pl",
        "--password-length",
        type=int,
        default=10,
        help="The length of the password")

    parser.add_argument(
        "-np",
        "--number-of-passwords",
        type=int,
        help="The number of passwords")

    parser.add_argument(
        "-xn",
        "--exclude-numbers",
        action="store_true",
        help="Do not include numbers in the generated password"
    )

    parser.add_argument(
        "-xl",
        "--exclude-letters",
        action="store_true",
        help="Do not include letters in the generated password"
    )

    parser.add_argument(
        "-xlc",
        "--exclude-lowercase-letters",
        action="store_true",
        help="Do not include lowercase letters in the generated password"
    )

    parser.add_argument(
        "-xuc",
        "--exclude-uppercase-letters",
        action="store_true",
        help="Do not include uppercase letters in the generated password"
    )

    parser.add_argument(
        "-xs",
        "--exclude-symbols",
        action="store_true",
        help="do not include symbols in the generated password"
    )

    return parser.parse_args()
