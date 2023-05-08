"""
Working with Loops
"""
print("Selamat Datang di Permainan Tebak Angka!")
print("Cara mainnya mudah. Kami memilih sebuah angka, dan kamu tinggal menebak angka tersebut.")
import random
number = random.randint(1,20)
isGuessRight = False
while isGuessRight != True:
    guess = input("Silakan tebak angka diantara 1 dan 20: ")
    if int(guess) == number:
        print("Anda menebak {}. Dan tebakannya benar! Anda menang!".format(guess))
        isGuessRight = True
    else:
        print("Anda menebak {}. Maaf tebakan masih salah, Silakan coba lagi.".format(guess))
        
