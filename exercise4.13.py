makanan = ('Gulai', 'Pempek', 'Rawon', 'Naspad', 'Cakcul')
print("Menu makanan restoran:")
for jenis in makanan:
    print(jenis)

print("\nMencoba mengubah salah satu menu:")

try:
    makanan[0] = 'Bakso'
except TypeError:
    print("Menu tidak dapat diubah karena tuple bersifat tetap.")

makanan = ('Gulai', 'Bakso', 'Rawon', 'Udang Keju', 'Cakcul')

print("\nMenu makanan setelah diperbarui:")
for jenis in makanan:
    print(jenis)