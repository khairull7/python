class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item, quantity):
        self.items.append((item, quantity))

    def calculate_total(self):
        total = 0
        for item, quantity in self.items:
            total += item.price * quantity
        return total

    def print_receipt(self, customer_name, payment):
        print("========== Struk Pembelian ==========")
        print(f"Pelanggan: {customer_name}")
        for item, quantity in self.items:
            print(f"{item.name} (x{quantity}): Rp {item.price * quantity}")
        total = self.calculate_total()
        print(f"Total: Rp {total}")
        print(f"Bayar: Rp {payment}")
        print(f"Kembalian: Rp {payment - total}")
        print("=====================================")

def main():
    # Daftar menu makanan
    food_menu = [
        Item("Nasi Goreng", 15000),
        Item("Mie Goreng", 12000),
        Item("Ayam Bakar", 20000),
        Item("Sate Ayam", 25000),
        Item("Soto Ayam", 18000)
    ]

    # Daftar menu minuman
    drink_menu = [
        Item("Teh Manis", 5000),
        Item("Es Jeruk", 7000),
        Item("Kopi Hitam", 8000),
        Item("Jus Alpukat", 10000),
        Item("Es Teh Tawar", 6000)
    ]

    order = Order()
    
    print("=== Selamat datang di program kasir ===")

    # Input nama pelanggan
    customer_name = input("Masukkan nama pelanggan: ")

    # Memilih menu makanan
    while True:
        print("\n=== Menu Makanan ===")
        for idx, item in enumerate(food_menu, start=1):
            print(f"{idx}. {item.name} - Rp {item.price}")

        food_choice = input("Pilih nomor menu makanan (atau ketik 'selesai' untuk lanjut ke minuman): ")
        if food_choice.lower() == 'selesai':
            break

        try:
            food_choice = int(food_choice)
            if 1 <= food_choice <= len(food_menu):
                quantity = int(input(f"Berapa porsi {food_menu[food_choice-1].name}? "))
                order.add_item(food_menu[food_choice-1], quantity)
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Input tidak valid. Coba lagi.")

    # Memilih menu minuman
    while True:
        print("\n=== Menu Minuman ===")
        for idx, item in enumerate(drink_menu, start=1):
            print(f"{idx}. {item.name} - Rp {item.price}")

        drink_choice = input("Pilih nomor menu minuman (atau ketik 'selesai' untuk menyelesaikan pesanan): ")
        if drink_choice.lower() == 'selesai':
            break

        try:
            drink_choice = int(drink_choice)
            if 1 <= drink_choice <= len(drink_menu):
                quantity = int(input(f"Berapa gelas {drink_menu[drink_choice-1].name}? "))
                order.add_item(drink_menu[drink_choice-1], quantity)
            else:
                print("Pilihan tidak valid. Coba lagi.")
        except ValueError:
            print("Input tidak valid. Coba lagi.")

    # Jika tidak ada pesanan yang dibuat
    if not order.items:
        print("Tidak ada pesanan yang dibuat.")
        return

    # Menghitung total pembayaran
    total = order.calculate_total()
    print(f"Total yang harus dibayar: Rp {total}")

    # Meminta input pembayaran
    while True:
        try:
            payment = int(input("Masukkan jumlah uang yang dibayarkan: Rp "))
            if payment >= total:
                break
            else:
                print("Uang yang dibayarkan kurang. Coba lagi.")
        except ValueError:
            print("Input tidak valid. Coba lagi.")

    # Mencetak struk pembelian
    order.print_receipt(customer_name, payment)

if __name__ == "__main__":
    main()
