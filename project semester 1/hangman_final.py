import random #modul random
import testkata
from tampilan_hangman import gambar_hangman
import string #modul

#MENU AWAL
print("selamat datang di game HANGMAN",'\n')
print('membeli tahu di jalan raya')
nama=input("kalo boleh tau, siapa namanya?: ")
print('\n')
print("halo",nama,'sebelum bermain, mohon perhatikan instruksi di bawah:','\n')

#TATA CARA BERMAIN
def ulang():    
    print('{:>38}'.format("instruksi permainan".upper()))
    print('1. pemain hanya diperbolehkan mengisi 1 huruf di setiap sesi'.upper())
    print('2. apabila jawaban salah, maka nyawa akan berkurang 1'.upper())
    print('3. apabila jawaban benar, maka pemain akan mendapatkan poin'.upper())
    paham=input("apakah anda sudah siap untuk bermain? (Y/N):".upper())
    if paham == "N" or paham == 'n':
        print("\nniat main gak sih ente!!!".upper())
        exit()
    else:
        print("baik, mari kita coba".upper())
ulang()
print('\n')  

#PILIHAN LEVEL
def gamestart():
    level=input(("silahkan pilih level [mudah,sedang,susah]:"))
    if level == "mudah":
        def kata_valid(kata):
            kata = random.choice(testkata.mudah)  # memilih sesuatu dari list secara acak
            return kata.upper()

    elif level == "sedang":
        def kata_valid(kata):
            kata = random.choice(testkata.sedang)  # memilih sesuatu dari list secara acak
            return kata.upper()

    elif level == "susah":
        def kata_valid(kata):
            kata = random.choice(testkata.susah)  # memilih sesuatu dari list secara acak
            return kata.upper()

    else:
        print("input salah")

#PERMAINAN HANGMAN
    def hangman():
        kata = kata_valid(testkata)
        huruf_kata = set(kata)  # huruf di dalam kata
        abjad = set(string.ascii_uppercase)
        huruf_terpakai = set()  # untuk huruf yang udah ditebak

        nyawa = 7

        # JAWABAN DARI PEMAIN
        while len(huruf_kata) > 0 and nyawa > 0:
            # huruf terpakai
            # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
            print('kamu punya', nyawa, 'nyawa tersisa dan huruf yang telah kamu gunakan: ', ' '.join(huruf_terpakai))

            # kata saat ini (contohnya K - T A)
            list_kata = [huruf if huruf in huruf_terpakai else '-' for huruf in kata]
            print(gambar_hangman[nyawa])
            print('kata saat ini: ', ' '.join(list_kata))

            huruf_pemain = input('tebak huruf: ').upper()
            if huruf_pemain in abjad - huruf_terpakai:
                huruf_terpakai.add(huruf_pemain)
                if huruf_pemain in huruf_kata:
                    huruf_kata.remove(huruf_pemain)
                    print('')

                else:
                    nyawa = nyawa - 1  # nyawa berkurang jika jawaban salah
                    print('\nhuruf ini,', huruf_pemain, 'tidak ada di dalam kata.')

            elif huruf_pemain in huruf_terpakai:
                print('\nanda telah menggunakan huruf ini. coba tebak huruf lain.')

            else:
                print('\nhuruf ini tidak valid.')

        # bagian ini saat len(huruf_kata) == 0 atau saat nyawa == 0
        if nyawa == 0:
            print(gambar_hangman[nyawa])
            print('game over, kata yang dimaksud adalah:', kata)
        else:
            print('SELAMAT!!! kamu telah menebak kata:', kata, '!!')


    if __name__ == '__main__':
        hangman()

    gameover=input("ingin coba lagi?(y/n) ")
    if gameover == "Y" or gameover == "y":
        gamestart()
    else:
        print("baik, see you to the next journey!!".upper())
        exit()
gamestart()
