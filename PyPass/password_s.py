import secrets 


secret = secrets.SystemRandom()
characters = [
            "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z",
            "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z",
            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"
]


def get_password(minimum: int = 15, maximum: int = 20) -> str:
    return "".join(secret.choice(characters) for _ in range(secret.randint(minimum,  maximum)))


def get_passwords(amount: int) -> str:
    passwords_l = []
    for _ in range(amount):
        passwords_l.append(get_password())
    return "\n".join(passwords_l)


def save_password(passwords: str, path: str) -> None:
    try:
        f = open(path, "w+")
    except Exception as e:
        print(e)
        return
    f.write(passwords)
    f.close()
