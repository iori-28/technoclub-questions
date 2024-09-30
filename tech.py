"""
Index yang tersusun rapih

ada array yang berisi ['T', 'E', 'C', 'H', 'N', 'O', 'C', 'L', 'U', 'B'].
guru meminta agar tulisan C saja yang ditampilkan ke dalam layar.
penuhi permintaan guru tersebut.

Contoh
Input:
['T', 'E', 'C', 'H', 'N', 'O', 'C', 'L', 'U', 'B']

Output:
C C
"""
tech = ['T', 'E', 'C', 'H', 'N', 'O', 'C', 'L', 'U', 'B']

# lanjutkan code dibawah ini
tech = ['T', 'E', 'C', 'H', 'N', 'O', 'C', 'L', 'U', 'B']

# Iterate through the list and print 'C' whenever it appears
for huruf in tech:
    if huruf == 'C':
        print(huruf, end=' ')
