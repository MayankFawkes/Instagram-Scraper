import socket,select,re,ssl,threading,sys,os
from urllib.parse import urlparse
from time import sleep
def hparsec(data):
  headers =  data.split(b'\r\n\r\n')[0]
  html = data[len(headers)+4:]
  headers=headers.decode().split("\r\n")
  out={}
  out["status"]=headers[0].split()[1]
  for n in headers[1:]:
    temp=n.split(":")
    value=""
    for n in temp[1:]:
      value+=n+":"
    out[temp[0].lower()]=value[1:len(value)-1]
  return out
def Download(urlinit="",location=""):
  if not urlinit:
    urlinit=input("Download Link -->")
    #urlinit="http://www.panacherock.com/downloads/mp3/01_Sayso.mp3"
  o=urlparse(urlinit)
  if o.query:
    url=(o.path+"?"+o.query)
  else:
    url=o.path
  filename=urlinit.split("?")[0].split("/")[-1]
  host=o.netloc
  send='GET {} HTTP/1.1\r\nHOST:{}\r\nConnection: close\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15\r\nAccept: */*\r\n\r\n'.format(url,host)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  if o.scheme=="https":
    s.connect((host, 443))
    s = ssl.create_default_context().wrap_socket(s, server_hostname=host)
  elif o.scheme=="http":
    s.connect((host, 80))
  else:
    print("we only support HTTP and HTTPS")
  s.sendall(send.encode("ascii"))
  data = s.recv(1024)
  headers =  data.split(b'\r\n\r\n')[0]
  image = data[len(headers)+4:]
  headers=hparsec(headers)
  #print((headers["status"]))
  if int(headers["status"]) is not 200:
    try:
      s.close()
      main(headers["location"])
    except:
      print("We cant download from this URL Contact Admin with URL")
      sys.exit(1)
  f = open(location+"/"+filename, 'wb')
  f.write(image)
  while True:
      data = s.recv(5120)
      if not data: break
      f.write(data)
  f.close()