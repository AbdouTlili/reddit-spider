import urllib.request , urllib.parse, urllib.error
import ssl

url ='https://miro.medium.com/max/1200/1*mk1-6aYaf_Bes1E3Imhc0A.jpeg'
# ignoring the ssl certificate 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
# Ignore SSL certificate errors

req = urllib.request.Request(headers=headers, url=url)

image = urllib.request.urlopen(req).read()

with open('img.png','wb') as f:
    f.write(image)