from asyncio.base_futures import _future_repr_info
from operator import mod
# import z3
import re
import string

data="(12433, 149, 197, 104), (8147, 131, 167, 6633), (10687, 211, 197, 35594), (19681, 131, 211, 15710), (33577, 251, 211, 38798), (30241, 157, 251, 35973), (293, 211, 157, 31548), (26459, 179, 149, 4778), (27479, 149, 223, 32728), (9029, 223, 137, 20696), (4649, 149, 151, 13418), (11783, 223, 251, 14239), (13537, 179, 137, 11702), (3835, 167, 139, 20051), (30983, 149, 227, 23928), (17581, 157, 131, 5855), (35381, 223, 179, 37774), (2357, 151, 223, 1849), (22649, 211, 229, 7348), (1151, 179, 223, 17982), (8431, 251, 163, 30226), (38501, 193, 211, 30559), (14549, 211, 151, 21143), (24781, 239, 241, 45604), (8051, 179, 131, 7994), (863, 181, 131, 11493), (1117, 239, 157, 12579), (7561, 149, 199, 8960), (19813, 239, 229, 53463), (4943, 131, 157, 14606), (29077, 191, 181, 33446), (18583, 211, 163, 31800), (30643, 173, 191, 27293), (11617, 223, 251, 13448), (19051, 191, 151, 21676), (18367, 179, 157, 14139), (18861, 149, 191, 5139), (9581, 211, 193, 25595)"

mylist=data.split("), ")
result="falg:"
for i in mylist:
    # re.sub(r'\(\)','',i)
    i=i.replace(' ','')
    i=i.lstrip('(')
    i=i.rstrip(')')
    tr=i.split(',')
    # print(tr)

    # e, p, q, pow(ord(c), e, p * q)
    # mod(pow(x,tr[0]),tr[1]*tr[2])==tr[3]
    # flag=mod(pow(int(tr[3]),1.0/int(tr[0])),int(tr[1])*int(tr[2]))
    # print(flag)
    # print(chr(int(flag)))

    for asc in range(32,127):
        if mod(pow(asc,int(tr[0])),int(tr[1])*int(tr[2]))==int(tr[3]):
             print(chr(asc),end='')