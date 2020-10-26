from urllib.request import *
from urllib.parse import *
import http.client

url='http://www.wechall.net/challenge/training/programming1/index.php?action=request'
cookie='WC=12612277-53612-GMFunhbdsc3QbIXh'
req = Request(url)
req.add_header('Cookie',cookie)
f=urlopen(req)
data= f.read().decode("utf-8")
print(data)


url_send=urlparse('http://www.wechall.net/challenge/training/programming1/index.php?answer=the_message')
print(url_send)
query_dict = parse_qs(url_send.query)  
query_dict['answer'] = data
new_parts = list(url_send)
new_parts[4] =urlencode(query_dict)
new_parts=urlunparse(new_parts)
print(new_parts)

req1=Request(new_parts)
req1.add_header('Cookie',cookie)
f1=urlopen(req1)





