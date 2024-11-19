stok_barang_gudang = []

def menampilkan_barang_gudang():
    if not stok_barang_gudang:
        print('\nBelum ada barang di gudang.')
    else:
        print('\nBarang gudang\n')
        print('Index\t| Nama\t| Kategori\t| Stok masuk\t| Stok keluar\t| Stok total')
    for i, barang in enumerate(stok_barang_gudang):
        print(f"{i}\t| {barang['nama']}\t| {barang['kategori']}\t\t| {barang['stok masuk']}\t\t| {barang['stok keluar']}\t\t| {barang['stok total']}")

def tambah_barang_gudang():
    while True:
        nama_barang = input('Masukan Nama Barang : ').strip().lower()
        kategori = input('Masukan Kategori Barang : ')
        stok_masuk = int(input('Masukan Stok masuk Barang : '))
        stok_keluar = int(input('Masukan Stok keluar Barang : '))
        stok_total = stok_masuk - stok_keluar
        if any(barang['nama'] == nama_barang for barang in stok_barang_gudang):
            print('Barang sudah ada, masukan barang lain.')
        else:
            stok_barang_gudang.append({
                'nama': nama_barang,
                'kategori': kategori, 
                'stok masuk': stok_masuk,
                'stok keluar': stok_keluar, 
                'stok total': stok_total
            })
            print('\nBarang berhasil ditambahkan\n')
            menampilkan_barang_gudang()
        checker = input('\nMau menambahkan barang yang lain? (ya/tidak) = ')
        if checker == 'tidak':
            break
    menampilkan_barang_gudang()
    
def perbarui_stok_gudang():
    while True:
        menampilkan_barang_gudang()
        nama_barang = input('\nMasukkan Nama Barang yang ingin diperbarui: ').strip().lower()
        barang_ditemukan = False 
        for barang in stok_barang_gudang:
            if barang['nama'] == nama_barang:
                barang_ditemukan = True
                print(f'\nBarang ditemukan: {barang}')
                kategori_baru = input('Masukkan kategori baru (biarkan kosong jika tidak ingin mengubah): ').strip()
                stok_masuk_baru = input('Masukkan stok masuk baru (biarkan kosong jika tidak ingin mengubah): ').strip()
                stok_keluar_baru = input('Masukkan stok keluar baru (biarkan kosong jika tidak ingin mengubah): ').strip()
                if kategori_baru:
                    barang['kategori'] = kategori_baru
                if stok_masuk_baru:
                    barang['stok masuk'] += int(stok_masuk_baru)
                if stok_keluar_baru:
                    barang['stok keluar'] += int(stok_keluar_baru)
                barang['stok total'] = barang['stok masuk'] - barang['stok keluar']
                print('Barang berhasil diperbarui')
                menampilkan_barang_gudang()
                break  
        if not barang_ditemukan:
            print('Barang tidak ditemukan di gudang')
        checker = input('\nMau memperbarui barang yang lain? (ya/tidak): ').strip().lower()
        if checker == 'tidak':
            break

def menghapus_barang_gudang():
    while True:
        menampilkan_barang_gudang()
        index_barang = int(input('Masukan index barang yang ingin dihapus : '))
        menampilkan_barang_gudang()
        if index_barang < 0 or index_barang >= len(stok_barang_gudang):
            print('Index tidak valid, silahkan ketik ulang')
        else:
            del stok_barang_gudang[index_barang]
            menampilkan_barang_gudang()
        checker = input('\nMau menghapus barang yang lain? (ya/tidak): ').strip().lower()
        if checker == 'tidak':
            break

while True:
    pilih_menu = input('''
        Stok Gudang PT.Kilan
                       
        List Menu :
        1. Tampilkan Barang
        2. Tambah Barang
        3. Perbarui Stok
        4. Menghapus Barang
        5. Exit Program
                       
        Masukan angka Menu yang ingin dijalankan : ''')
    
    if(pilih_menu == '1'):
        menampilkan_barang_gudang()
    elif(pilih_menu == '2'):
        tambah_barang_gudang()
    elif(pilih_menu == '3'):
        perbarui_stok_gudang()
    elif(pilih_menu == '4'):
        menghapus_barang_gudang()
    elif(pilih_menu == '5'):
        break




