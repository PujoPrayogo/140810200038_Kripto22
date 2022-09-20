""" TUGAS 2 PRAKTIKUM KRIPTOGRAFI
Nama    : Pujo Prayogo
NPM     : 140810200038
Kelas   : B
"""
def shift_encrypt(text, key):       #Fungsi Enkripsi Shift Cipher
    hasil = ""                      #Deklarasi string hasil (null dulu)
                                
    for i in range(len(text)):      #Traverse tiap huruf pada teks
        char = text[i]              #Assign tiap huruf kata pada var. Char

        if (char.isupper()):        #Enkripsi Huruf Kapital
            hasil += chr((ord(char) + key - 65)% 26 + 65) #+65 karena ASCII
        else:                       #Enkripsi Huruf non-Kapital
            hasil += chr((ord(char) + key - 97)% 26 + 97) #+97 karena ASCII
                                    #chr() print karakter dari ASCII
                                    #ord() return angka ASCII dari karakter
    return hasil                    #Print Hasil

teks = input("Plain text\t: ")      #Input Plain Text yg aPukan dienkripsi
kunci = input("Kunci\t\t: ")        #Input Key Shift Ciphernya
print("Cipher: " + shift_encrypt(teks , int(kunci))) #Melakukan Enkripsi
                                    #kunci dibuat int karena string