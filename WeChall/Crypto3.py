import sys

data='''6C 14 14 09 20 0F 14 07 51 20 1E 14 1A 20 18 14
11 1B 0A 09 20 14 13 0A 20 12 14 17 0A 20 08 0D
06 11 11 0A 13 0C 0A 20 0E 13 20 1E 14 1A 17 20
0F 14 1A 17 13 0A 1E 53 20 79 0D 0E 18 20 14 13
0A 20 1C 06 18 20 0B 06 0E 17 11 1E 20 0A 06 18
1E 20 19 14 20 08 17 06 08 10 53 20 7C 06 18 13
4C 19 20 0E 19 64 20 56 57 5D 20 10 0A 1E 18 20
0E 18 20 06 20 16 1A 0E 19 0A 20 18 12 06 11 11
20 10 0A 1E 18 15 06 08 0A 51 20 18 14 20 0E 19
20 18 0D 14 1A 11 09 13 4C 19 20 0D 06 1B 0A 20
19 06 10 0A 13 20 1E 14 1A 20 19 14 14 20 11 14
13 0C 20 19 14 20 09 0A 08 17 1E 15 19 20 19 0D
0E 18 20 12 0A 18 18 06 0C 0A 53 20 7C 0A 11 11
20 09 14 13 0A 51 20 1E 14 1A 17 20 18 14 11 1A
19 0E 14 13 20 0E 18 20 09 15 15 11 07 0B 0A 14
0D 12 06 0D 53'''

databytes=data.split()

print(chr(int(databytes[1],16)))

sys.stdout = open('/root/Documents/CTF_WECALL/results.py', mode = 'w',encoding='utf-8')
for i in range(128):
    mess="the %s results:      "%i
    print(mess)
    for d in databytes:
        print(chr((int(d,16)+i)%128),end='')
    print('\n\n\n\n\n')

