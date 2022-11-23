from . import ops

def read_console():
    data_file = ops.read()
    
    index = "No"
    Nama_Menu = "Nama Menu"
    Kategori_Menu = "Kategori Menu"
    Harga_Menu = "Harga Menu"
    Stock_Menu = "Stock Menu"
    Masa_Berlaku = "Masa Berlaku"
    
    print("\n"+"="*100)
    print(f"{index:4} | {Nama_Menu:40} | {Kategori_Menu:40} | {Harga_Menu:40} | {Stock_Menu:40} | {Masa_Berlaku:40}")
    print("-"*100)
    
    
    print("data")
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        Nama_Menu = data_break[2]
        Kategori_Menu = data_break[3]
        Harga_Menu = data_break[4]
        Stock_Menu = data_break[5]
        Masa_Berlaku = data_break[6]
        
        print(f"{index+1:4} | {Nama_Menu:.40} | {Kategori_Menu:.40} | {Harga_Menu:.10} | {Stock_Menu:5} | {Masa_Berlaku:.10}", end="")
    
    print("\n"+"="*100)