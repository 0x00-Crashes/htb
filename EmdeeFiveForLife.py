import requests,re,hashlib,hexdump

p = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}
r = requests.Session()
resp = r.get('http://docker.hackthebox.eu:40022/', proxies=p)

#rint "R1: " + str(r.status_code)
#print format_text('r.headers is: ',r.headers)
#print format_text('r.cookies is: ',r.cookies)
#print r.text
toEncrypt = re.findall(r"([a-zA-Z\d]{20})", resp.text)
print "String to encrypt: " + toEncrypt[0]
md5 = str(toEncrypt[0])
md5 = hashlib.md5(md5).hexdigest()
print "MD5: " + md5
md5_post = {'hash': md5}

r2 = r.post('http://docker.hackthebox.eu:40022/', data=md5_post, proxies=p)
#print "\nR2: " + str(r2.status_code)
#print "\nResponse: \n" + r2.text
flag = re.findall(r"HTB\{.*\}",r2.text)
print "Flag: " + flag[0]


