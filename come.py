"""
Membuat Daftar Penumpang

Tugasmu adalah membuat program yang akan mengonversi data penumpang dari input yang diberikan menjadi list of dictionaries. 
Setiap penumpang memiliki tiga atribut: nama, umur, dan asal planet. 
Program harus meminta input untuk setiap atribut penumpang dan menyimpannya dalam dictionary, lalu memasukkan dictionary tersebut ke dalam list.

Contoh
Input:
Jumlah penumpang: 2

Penumpang 1
Nama: Hanif
Umur: 23
Asal planet: Mars

Penumpang 2
Nama: Rani
Umur: 25
Asal planet: Jupiter

Output:
[
    {'nama': 'Hanif', 'umur': 23, 'asal planet': 'Mars'},
    {'nama': 'Rani', 'umur': 25, 'asal planet': 'Jupiter'}
]
"""
penumpang = []
jumlah_penumpang = int(input("Jumlah penumpang: "))

for i in range(jumlah_penumpang):
    nama = input(f"Penumpang {i+1}\nNama: ")
    umur = int(input("Umur: "))
    asal_planet = input("Asal planet: ")
    
    print()
    
    # lanjutkan code dibawah ini
# List to store passenger information
penumpang = [1]

# Input the number of passengers
jumlah_penumpang = int(input("Jumlah penumpang: "))

# Loop to gather information for each passenger
for i in range(jumlah_penumpang):
    print(f"Penumpang {i + 1}")
    nama = input("Nama: ")
    umur = int(input("Umur: "))
    asal_planet = input("Asal planet: ")
    
    print()  # Print a newline for better readability

    # Create a dictionary for the passenger
    passenger_info = {
        'nama': nama,
        'umur': umur,
        'asal planet': asal_planet
    }
    
    # Append the dictionary to the list
    penumpang.append(passenger_info)

# Print the list of dictionaries
print(penumpang)




