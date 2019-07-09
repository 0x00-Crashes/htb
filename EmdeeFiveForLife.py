import requests,re,hashlib,hexdump

url = 'http://docker.hackthebox.eu:41145'
p = {'http':'http://127.0.0.1:8080','https':'http://127.0.0.1:8080'}
r = requests.Session()

resp = r.get(url)
toEncrypt = re.findall(r"([a-zA-Z\d]{20})", resp.text)
print "String to encrypt: " + toEncrypt[0]

md5 = str(toEncrypt[0])
md5 = hashlib.md5(md5).hexdigest()
print "MD5: " + md5
md5_post = {'hash': md5}

r2 = r.post(url, data=md5_post)
flag = re.findall(r"HTB\{.*\}",r2.text)
print "Flag: " + flag[0]
