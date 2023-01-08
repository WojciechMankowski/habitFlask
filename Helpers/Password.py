import crypt
from string import ascii_uppercase


def is_lenght_valid(password):
    return len(password) >= 8


def encrypt(password):
    return crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))


def check_encrypted(password, hashed):
    return crypt.crypt(password, hashed) == hashed


def how_uper_case(password):
    # print(1 for c in password if c in ascii_uppercase)
    for c in password:
        print(c )
        if c in ascii_uppercase:
            print(c)

        return sum(1 for c in password if c in ascii_uppercase)


def is_special_char(password):
    return any(not c.isalnum() for c in password)


def is_number(password):
    return any(c.isdigit() for c in password)


def is_password(password):
    return is_lenght_valid(password) and how_uper_case(password) >= 2 and \
        is_special_char(password) and is_number(password)


if __name__ == '__main__':
    # print(how_uper_case('12345678'))
    # print(is_special_char('12345678'))
    # print(is_password("haslo"))
    print(is_password("hwojtek92!"))
