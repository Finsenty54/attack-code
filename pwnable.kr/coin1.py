#!/usr/bin/python2
# coding=utf-8
# __author__:TaQini

from pwn import *

local_file = './passcode'
local_libc = '/lib/x86_64-linux-gnu/libc.so.6'
remote_libc = local_libc  # '../libc.so.6'

is_local = False
is_remote = False

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
        p = sh.process(local_file)
        #elf = ELF(local_file)
    elif sys.argv[1] == 'nc':
        conn = remote(sys.argv[2], sys.argv[3])
    else:
        # len(sys.argv) == 3:
        host = sys.argv[1]
        port = sys.argv[2]
        p = remote(host, port)
        libc = ELF(remote_libc)

    '''else:
        host, port = sys.argv[1].split(':')'''


#elf = ELF(local_file)

#context.log_level = 'debug'
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


# rop1s
trash = conn.recvline_contains('N=')

fake = 0
while (fake < 100):
    useful = conn.recvline_contains('N=')

    num, fake_tmp = str(useful).split(' ')
    print 'n=',num.strip("b'N=")
    num = int(num.strip("b'N="))
    fake_num= int(fake_tmp.strip('C=').strip("'"))
    fake +=fake_num
    #fake+=int(fake_tmp.strip("'"))
    print 'fake=',fake

    #保存值
    #双指针注意
    left_f=0
    right_f=num
    left=0
    right=int(num/2)
    #fake_num之后要发送的结果值
    final_send=0
    for j in range(fake_num):
        data=''
        for i in range(left, right):
            data+=str(i)+' '

        conn.sendline(data)
        rcv=int(str(conn.recvline()).strip("b'").strip("\\n'"))
        #print("rcv="+str(rcv)+"     send_count="+str(j))
        if (right-left)==1 and rcv==9:
            final_send=left
        elif (right-left)==1 and rcv==10:
            final_send=right

        if rcv<(right-left)*10:
            right_f=right
            right=left_f+int((right_f-left_f)/2)
            #print("left_f=%d, right_f=%d" %(left_f,right_f))
        else:
            left_f=right
            left=right
            right=left_f+int((right_f-left_f)/2)
            #print("left_f=%d, right_f=%d" %(left_f,right_f))

    conn.sendline(str(final_send))

        

print conn.recvlines()

# debug()


# system()地址 + 命令字符串地址
