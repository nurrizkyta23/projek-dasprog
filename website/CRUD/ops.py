from . import Database
from .utility import randomizer
from time import time

def create_first_data(Nama_Menu, Kategori_Menu, Harga_Menu, Stock_Menu, Masa_Berlaku):
 
    data = Database.TEMPLATE.copy()
    
    data["pk"] = randomizer(6)
    data["date_add"] = time.strftime("%Y-%m-%d", time)
    data["Nama_Menu"] = Nama_Menu + Database.TEMPLATE["kategori_menu"][len(Nama_Menu):]
    data["Kategori_Menu"] = Kategori_Menu + Database.TEMPLATE["kategori_menu"][len(Kategori_Menu):]
    data["Harga_Menu"] = Harga_Menu + Database.TEMPLATE["kategori_menu"][len(Harga_Menu):]
    data["Stock_Menu"] = Stock_Menu + Database.TEMPLATE["kategori_menu"][len(Stock_Menu):]
    data["Masa_Berlaku"] = Masa_Berlaku + Database.TEMPLATE["kategori_menu"][len(Masa_Berlaku):]
    
    data_str = f'{data["pk"]}, {data["date_add"]}, {data["Nama_Menu"]}, {data["Kategori_Menu"]}, {data["Harga_Menu"]}, { data["Stock_Menu"]}, {data["Masa_Berlaku"]}'
    
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Failed to Load Database")


def create_first_data():
    Nama_Menu = input("Nama Menu :")                    
    Kategori_Menu = input("Kategori Menu : ")
    Harga_Menu = input("Harga Menu : ")
    Stock_Menu = input("Stock Menu : ")
    Masa_Berlaku = input("Masa Berlaku :")
    
    data = Database.TEMPLATE.copy()

    data["pk"] = randomizer(6)
    data["date_add"] = time.strftime("%Y-%m-%d", time)
    data["Nama_Menu"] = Nama_Menu + Database.TEMPLATE["kategori_menu"][len(Nama_Menu):]
    data["Kategori_Menu"] = Kategori_Menu + Database.TEMPLATE["kategori_menu"][len(Kategori_Menu):]
    data["Harga_Menu"] = Harga_Menu + Database.TEMPLATE["kategori_menu"][len(Harga_Menu):]
    data["Stock_Menu"] = Stock_Menu + Database.TEMPLATE["kategori_menu"][len(Stock_Menu):]
    data["Masa_Berlaku"] = Masa_Berlaku + Database.TEMPLATE["kategori_menu"][len(Masa_Berlaku):]
    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    
    data_str = f'{data["pk"]}, {data["date_add"]}, {data["Nama_Menu"]}, {data["Kategori_Menu"]}, {data["Harga_Menu"]}, { data["Stock_Menu"]}, {data["Masa_Berlaku"]}'
    print(data_str)
    
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Failed to write data")


        
def read():
    try:
        with open(Database.DB_NAME, 'r') as file:
            content = file.readlines()
            print(content)
    except:
        print("Failed to Read DATABASE!")