#!/usr/bin/env python
from sqlite3 import connect
import pwn

def main():
    p = pwn.connect("127.0.0.1", 1337)
    x = 0
    while x < 999:
        y = p.sendlineafter(b'Give p:', bytes(x))
        if y != 'Conditions not satisfied!':
            p.interactive()
        x +=1

main()
