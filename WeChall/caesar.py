

data='WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ RI FDHVDU DQG BRXU XQLTXH VROXWLRQ LV ELQQDHPLOKHH'
datac=list(data)

for i in range(0,26):
    for j in datac:
        if j !=' ':
            print(chr((ord(j)-ord('A')+i)%26+ord('A')),end='')
        else:
            print(' ',end='')

    print()


