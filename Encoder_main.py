from scapy.all import *

def message_encoder():
    data=input("Enter the message: ")
    asc=[]
    for ele in data:
        asc.extend(ord(num) for num in ele)
    n=len(asc)-1
    while n>=0:
        asc[n]=bin(asc[n])
        n=n-1
    for p in range(0,len(asc)):
        if len(asc[p])<10:
            diff=10-len(asc[p])
            m=0
            while m<diff:
                pos=asc[p].index('b')
                asc[p]=asc[p][:pos+1]+'0'+asc[p][pos+1:]
                m=m+1
    return asc



ip_src="192.168.0.67"
ip_dst="192.168.0.2"
ttl_rand=random.randrange(1,100)
pckt_list=[]
pckt1=IP(src=ip_src,dst=ip_dst,ttl=ttl_rand)/UDP()
pckt2=IP(src=ip_src,dst=ip_dst,ttl=(ttl_rand-1))/UDP()
begin=random.randint(0,100)
end=random.randint(0,100)
path="C:/Users/Szymon Mazurek/Desktop/pcap.pcap"
while begin>0:
    m=3
    n=random.randrange(1,3)
    if n==1:
        while m>0:
            c=wrpcap(path,pckt1,append=True)
            m=m-1

    else:
        while m>0:
            c=wrpcap(path,pckt2,append=True)
            m=m-1
    begin=begin-1

msg=message_encoder()
msg_length=len(msg)
dot_buffer='00101110'
for k in range(0,len(dot_buffer)):
    m=3
    if dot_buffer[k]=='1':
            while m>0:
                c=wrpcap(path,pckt1,append=True)
                m=m-1

    else:
            while m>0:
                c=wrpcap(path,pckt2,append=True)
                m=m-1



for i in range(0,msg_length):
        m=3
        msg[i]=msg[i][2:]
        for p in range(0,len(msg[i])):
            if msg[i][p]=='1':
                while m>0:
                    c=wrpcap(path,pckt1,append=True)
                    m=m-1


            else:
                while m>0:
                    c=wrpcap(path,pckt2,append=True)
                    m=m-1


for k in range(0,len(dot_buffer)):
            m=3
            if dot_buffer[k]=='1':
                while m>0:
                    c=wrpcap(path,pckt1,append=True)
                    m=m-1


            else:
                while m>0:
                    c=wrpcap(path,pckt2,append=True)
                    m=m-1



while end>0:
    m=3
    n=random.randrange(1,3)
    if n==1:
        while m>0:
            c=wrpcap(path,pckt1,append=True)
            m=m-1

    else:
        while m>0:
            c=wrpcap(path,pckt2,append=True)
            m=m-1

    end=end-1
