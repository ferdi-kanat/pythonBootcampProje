import os
class Library:
    def __init__(self):
        self.file = "books.txt"

    def list_books(self):
        with open(self.file, "r") as f:
            for line in f:
                kitap_bilgileri = line.strip().split(',')
                print(f"Kitap adı: {kitap_bilgileri[0]}, Yazar: {kitap_bilgileri[1]}, Yayın yılı: {kitap_bilgileri[2]}, Sayfa: {kitap_bilgileri[3]}")


    def add_book(self):
        ad = input("Kitap adini yazin: ")
        yazar = input("Kitap yazarini yazin: ")
        yayin_yili = input("Yayin yilini yazin: ")
        sayfa = input("Sayfa sayisini yazin: ")

        book_info = f"{ad},{yazar},{yayin_yili},{sayfa}\n"
        with open(self.file, "a") as f:
            f.write(book_info)
        print("Kitap eklendi")

    def remove_book(self):
        ad = input("kaldirilacak kitabin adini yazin ")
        gecici_file = "gecici.txt"
        with open(self.file, "r") as f, open(gecici_file, "w") as gecici:
            for line in f:
                if not line.startswith(ad):
                    gecici.write(line)
        os.remove(self.file)
        os.rename(gecici_file, self.file)
        print("Kitap kaldirildi")

    def quit(self):
        print("Programdan cikiliyor")
        exit()


lib = Library()

while True:
    print("** MENU **")
    print("1) Kitaplari listele")
    print("2) Kitap ekle")
    print("3) Kitap kaldır")
    print("q) Cikis")
    choice = input("Hangi islemi yapmak istiyorsunuz:1,2,3,q ")

    if choice == '1':
        lib.list_books()
    elif choice == '2':
        lib.add_book()
    elif choice == '3':
        lib.remove_book()
    elif choice == 'q':
        lib.quit()
    else:
        print("dort secenekten birini secin")
