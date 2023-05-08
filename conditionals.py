"""
Working With Conditionals
"""
userReply = input("Apakah anda ingin mengirim paket? (Masukan ya atau tidak) ")
if userReply == "ya":
    print("Kami dapat membantu anda mengirim paket!")
else:
    print("Silakan datang kembali bila anda ingin mengirim paket. Terima kasih.")
userReply = input("Apakah and ingin membeli materai, membeli amplop atau mau foto copy? ")
if userReply == "materai":
    print("Kami punya beberapa desain model materai yang bisa anda pilih.")
elif userReply == "amplop":
    print("Kami punya beberapa ukuran amplop yang bisa anda pilih.")
elif userReply == "foto copy":
    copies = input("Mau copy berapa rangkap? (Masukan angka) ")
    print("Ini sudah jadi {} rangkap.".format(copies))
else:
    print("Terima kasih, silakan datang kembali.")

