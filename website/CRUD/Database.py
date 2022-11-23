from .import ops

DB_NAME = "data.txt"
TEMPLATE = {
    "pk" : "XXXXXXX",
    "date_add" : "yyyy-mm-dd",
    "Nama_Menu" : 255*" ",
    "Kategori_Menu" : 255*" ",
    "Harga_Menu" : 255*" ",
    "Stock_Menu" : 255*" ",
    "Masa_Berlaku" : 255*" ",
}
def init_console():
    try:
        with open(DB_NAME, "r") as file:
            print("Database tersedia, init done!")
    except:
        print("Database tidak ditemukan, silahkan membuat database baru")
        ops.create_first_data()
        # with open(DB_NAME, "w", encoding="utf-8") as file:
           
        #     DB_NAME = f"{Nama_Menu},{Kategori_Menu},{Harga_Menu},{Stock_Menu},{Masa_Berlaku}"
        #     file.write(DB_NAME)