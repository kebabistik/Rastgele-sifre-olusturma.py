import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Şifre uzunluğunu girin: "))
        if length < 4:
            print("Şifre uzunluğu en az 4 olmalıdır!")
        else:
            print("Oluşturulan Şifre:", generate_password(length))
    except ValueError:
        print("Lütfen geçerli bir sayı girin!")
