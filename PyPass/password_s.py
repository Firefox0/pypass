import secrets 
import string

secret = secrets.SystemRandom()
characters = string.ascii_letters + string.digits


def get_password(minimum: int = 15, maximum: int = 20) -> str:
    """ Generate a single password. """
    length = secret.randint(minimum, maximum)
    while True:
        password = "".join(secret.choice(characters) for _ in range(length))
        if meets_basic_requirements(password):
            break
    return password


def get_passwords(amount: int) -> str:
    """ Generate multiple passwords. """
    return "\n".join(get_password() for _ in range(amount))


def save_password(passwords: str, path: str) -> None:
    """ Write data to file. """
    try:
        f = open(path, "w+")
    except Exception as e:
        print(e)
        return
    f.write(passwords)
    f.close()


def meets_basic_requirements(password: str) -> bool:
    """ Contains at least one uppercase character and one digit. """
    return any(c.isupper() for c in password) and any(c.isdigit() for c in password)
