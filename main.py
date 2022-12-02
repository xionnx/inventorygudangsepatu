items = {"Nike": {"s38": 3, "s39": 1, "s40": 3},
         "Adidas": {"s38": 3, "s39": 1, "s40": 3},
         "Vans": {"s38": 3, "s39": 1, "s40": 3}}


def main():
    print("=========================================================")
    print("    SELAMAT DATANG DI INVENTORY GUDANG SEPATU GARUDA    ")
    print("=========================================================")
    print("------------------------Menu-----------------------------")
    print("[1] - Tambahkan Barang ke Gudang")
    print("[2] - Lihat Gudang")
    print("[3] - Exit")
    print("=========================================================")
    while True:
        pilihanUser = input("Masukkan Pilihan : ")
        if pilihanUser == '1':
            tambahBarang()
            break
        elif pilihanUser == '2':
            lihatInventory()
            break
        elif pilihanUser == '3':
            break
        else :
            print("Pilihan tidak ada, silahkan masukkan nomor lagi")
            continue


def tambahBarang():
    print()
    print("=======================")
    print("TAMBAH BARANG KE GUDANG")
    print("=======================")
    print()
    while True:
        barangUser = input("Nama Barang : ")
        if barangUser != '':
            break
    while True:
        sizeBarang = input("Ukuran Barang : ")
        if sizeBarang.isdigit():
            break
    while True:
        jumlahBarang = input("Jumlah Barang : ")
        if jumlahBarang.isdigit():
            break
    itemsArray = {barangUser: {"s" + sizeBarang: jumlahBarang}}
    items.update(itemsArray)
    returnToMainMenu("Barangmu telah ditambahkan!")


def lihatInventory():
    print()
    print("LIHAT GUDANG")
    print("------------")
    print()
    print("BARANG")
    print("------")
    print()
    for item in items:
        print(item)
        for size in items[item]:
            print("Size", size.split('s', 1)[
                  1], ", Total :", items[item][size])
        print()
    print("========================================")
    print("        Pilihan yang tersedia :         ")
    print("========================================")
    print("[1] - Tambah/Kurang Stok Barang")
    print("[2] - Hapus Barang")
    print("[3] - Kembali ke Menu")
    print()
    while True:
        pilihanUser = input("Masukkan Pilihan : ")
        if pilihanUser == '1':
            editInventoryItem()
            break
        elif pilihanUser == '2':
            deleteInventoryItem()
            break
        elif pilihanUser == '3':
            main()
            break
        else :
            print("Pilihan tidak ada, silahkan masukkan nomor lagi")
            continue
            

def editInventoryItem():
    print()
    print("TAMBAH/KURANG STOK BARANG")
    print("-------------------------")
    print("========================================")
    print("        Pilihan yang tersedia :         ")
    print("========================================")
    print("[1] - Edit Nama Barang")
    print("[2] - Edit Ukuran Barang")
    print("[3] - Edit Jumlah Barang")
    print("[4] - Kembali")
    print()
    while True:
        pilihanUser = input("Masukkan Pilihan : ").lower()
        if pilihanUser in ['1', '2', '3', '4']:
            break
    if pilihanUser == '4':
        main()

    if pilihanUser == '1':
        print()
        while True:
            itemToChange = input("Masukkan Nama Barang Yang Ingin Di Ubah : ")
            if itemToChange in items:
                break
            else:
                print("Barang Itu Tidak Ada")
                print()

        while True:
            newItemName = input("Masukkan Nama Barang Yang Baru : ")
            if newItemName != '':
                break
        items.update({newItemName: items[itemToChange]})
        del items[itemToChange]

        returnToMainMenu("Nama Barang Telah Di Ubah")

    if pilihanUser == '2':
        print()
        while True:
            itemToChange = input("Masukkan Nama Barang Yang Ingin Di Ubah : ")
            if itemToChange in items:
                break
            else:
                print("Barang Itu Tidak Ada")
                print()

        while True:
            sizeToChange = "s" + input("Masukkan Ukuran Barang Yang Ingin Di Ubah : ")
            if sizeToChange in items[itemToChange]:
                break
            else:
                print("Ukuran Itu Tidak Ada")
                print()
        while True:
            newsizeBarang = "s" + input("Masukkan Ukuran Barang Yang Baru : ")
            if newsizeBarang != '':
                if newsizeBarang in items[itemToChange]:
                    print("Ukuran Itu Sudah Ada!")
                    print()
                else:
                    break

        items[itemToChange].update(
            {newsizeBarang: items[itemToChange][sizeToChange]})
        del items[itemToChange][sizeToChange]

        returnToMainMenu("Ukuran Barang Telah Di Ubah")

    if pilihanUser == '3':
        print()
        while True:
            itemToChange = input("Masukkan Nama Barang Yang Ingin Di Ubah : ")
            if itemToChange in items:
                break
            else:
                print("Barang Itu  Tidak Ada")
                print()

        while True:
            sizeToChange = "s" + input("Masukkan Ukuran Barang Yang Ingin Di Ubah : ")
            if sizeToChange in items[itemToChange]:
                break
            else:
                print("Ukuran Itu Tidak Ada")
                print()
        while True:
            newAmountItem = input("Masukkan Jumlah Barang Baru : ")
            if newAmountItem != '':
                break

        items[itemToChange].update({sizeToChange: newAmountItem})

        returnToMainMenu("Jumlah Barang Telah Berubah")


def deleteInventoryItem():
    print()
    print("======================")
    print("HAPUS BARANG DI GUDANG")
    print("======================")
    print()
    while True:
        itemToDelete = input("Masukkan Nama Barang Yang Ingin Di Hapus : ")
        if itemToDelete in items:
            break
        else:
            print("Barang Itu Tidak Ada")
            print()

    while True:
        confirmation = input(
            "Apa Kamu Yakin Ingin Menghapus Barang Ini ? : ").lower()
        if confirmation in ['ya', 'tidak', 'yes', 'no']:
            break
    if confirmation == 'yes' or confirmation == 'ya':
        del items[itemToDelete]
        returnToMainMenu("Barang Telah Di Hapus")
    else:
        main()


def returnToMainMenu(message):
    while True:
        print()
        back = input(f"{message}. Tekan (M) Untuk Kembali Ke Main Menu : ").lower(
        ) if message != None else input("Tekan (M) Untuk Kembali Ke Main Menu : ").lower()
        if back == 'm':
            main()
            break


main()