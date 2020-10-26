data="oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:we hgrppnhshs.p"
dataBytes=list(data)
lenth=len(dataBytes)

for i in range(0,148,2):
    tmp=dataBytes[i]
    dataBytes[i]=dataBytes[i+1]
    dataBytes[i+1]=tmp

dataRE=""
for e in dataBytes:
    dataRE+=e


print (dataRE)