""" parse command-line arguments """

from argparse import ArgumentParser, Namespace

def get_args() -> Namespace:
    """ parse and return command-line arguments """

    parser = ArgumentParser()

    parser.add_argument(
        "password_length",
        type=int,
        help="The length of the password")

    return parser.parse_args()
