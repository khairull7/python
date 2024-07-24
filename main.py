class Film:
    def __init__(self, judul, genre, tahun, pendapatan):
        self.judul = judul
        self.genre = genre
        self.tahun = tahun
        self.pendapatan = pendapatan

    def __str__(self):
        return f"{self.judul} ({self.tahun}) - {self.genre}, Pendapatan: Rp{self.pendapatan}"

class PengelolaFilm:
    def __init__(self):
        self.film = []

    def tambah_film(self, film):
        self.film.append(film)
        print(f"Film '{film.judul}' berhasil ditambahkan!")

    def lihat_film(self):
        if not self.film:
            print("Tidak ada film dalam koleksi.")
        else:
            for indeks, film in enumerate(self.film, start=1):
                print(f"{indeks}. {film}")

    def hapus_film(self, indeks):
        try:
            film_dihapus = self.film.pop(indeks - 1)
            print(f"Film '{film_dihapus.judul}' berhasil dihapus!")
        except IndexError:
            print("Indeks film tidak valid!")

def main():
    pengelola = PengelolaFilm()

    while True:
        print("\nSistem Manajemen Film")
        print("1. Tambah Film")
        print("2. Lihat Semua Film")
        print("3. Hapus Film")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            judul = input("Masukkan judul film: ")
            genre = input("Masukkan genre film: ")
            tahun = input("Masukkan tahun film: ")
            pendapatan = float(input("Masukkan pendapatan film: "))

            film = Film(judul, genre, tahun, pendapatan)
            pengelola.tambah_film(film)

        elif pilihan == "2":
            pengelola.lihat_film()

        elif pilihan == "3":
            indeks = int(input("Masukkan indeks film yang akan dihapus: "))
            pengelola.hapus_film(indeks)

        elif pilihan == "4":
            print("Keluar dari Sistem. Selamat tinggal!")
            break

        else:
            print("Pilihan tidak valid! Silakan masukkan opsi yang valid.")

if __name__ == "__main__":
    main()
