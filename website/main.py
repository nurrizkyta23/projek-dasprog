import os  

if __name__ == "__main__":
    sistem_operasi = os.name
    
    print(" SELAMAT DATANG DI PROGRAM ")
    print(" DATABASE MENU RESTAURANT")
    print(" =========================")
    
    while(True):
        match sistem_operasi:
            case "posix" : os.system("clear")
            case "nt" : os.system("cls")
        print(f"1. Read Data ")
        print(f"2. Create Data ")
        print(f"3. Update Data ")
        print(f"4. Delete Data ")

        user_option = input("Masukkan Opsi: ")
        
        print("\n===============\n")
        
        match user_option:
            case "1": print("Read Data")
            case "2": print("Create Data")
            case "3": print("Update Data")
            case "4": print("Delete Data")