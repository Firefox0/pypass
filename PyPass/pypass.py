import argparse
import pyperclip

import password_s


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--amount", type=int, default=1, help="Amount of passwords to generate.")
    parser.add_argument("-c", "--copy", action="store_true", help="Copy output to clipboard.")
    parser.add_argument("-p", "--print", action="store_true", help="Print output.")
    parser.add_argument("-w", "--write", type=str, help="Write output to file.")
    args = parser.parse_args()

    passwords = password_s.get_passwords(args.amount)
    if args.print:
        print(passwords)
    if args.copy:
        pyperclip.copy(passwords)
    if args.write:
        password_s.save_password(passwords, args.write)


if __name__ == "__main__":
    main()
