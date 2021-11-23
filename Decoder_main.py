from scapy.layers.inet import IP
from scapy.all import *
import binascii


pcap = rdpcap("C:/Users/tomas/Downloads/pcap (15).pcap")  #read packet capture file
pcap.show()# display the packet capture file
main_iterator = 0 # this is our value of packets "sniffed", main iterator to go through the file.


def int2bytes(i): #funcion helpig me to convert binary to ASCII
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

def alterElements(a,n): #function taking in every third element in respect to start, we can search for exact bit change
    return a[n::3]

def packet_sniffer(n,b): #reading the packets from file n=number of packets to sniff, b=main iterator,
    packets=[]
    ttl_list=[]

    fin=b +n
    while b < fin:
        packets.append(pcap[b]) #read packet from file
        ttl_list.append(pcap[b][0][IP].ttl) #read this packet ttl value
        b = b+1 #iterate
    src_ip=packets[0][0].src #read source ip
    dst_ip=packets[0][0].dst #read destination ip
    return src_ip,dst_ip, ttl_list, fin #output

print('min_max: Listening.....')
mm_conf=packet_sniffer(15,main_iterator)#here we sniff 15 packets to determine the low and high TTL values

main_iterator=mm_conf[3] #note main iterator

max_ttl=max(mm_conf[2])#max ttl value
min_ttl=min(mm_conf[2])#min ttl value
if max_ttl-min_ttl ==1:#checking the amplitude
    print("min_max Established:" ,min_ttl,max_ttl)
    L_H=[0,0]#saving the values
    L_H[0]=min_ttl
    L_H[1]=max_ttl
else:
    print("min_max Error, start again") #if min max not found, print error

t_f2=0#used as boolean for second loop(decoding)
t_f = 1#used as boolean for first loop(key searching)
a_bin = []
full_mess = ''
while t_f == 1:
    search_buff = packet_sniffer(1, main_iterator)# sniff 1 packet
    main_iterator = search_buff[3]#note iteration

    if main_iterator > 150: #if looking for a key is unsuccesful, timeout after 150 packets
        print("Timeout: Key NOT found")
        t_f = 0 #abandon
        n = len(new_a)#abandon
        t_f2=1#abandon
        break#abandon

    if search_buff[2][0] == L_H[0]:#if our sniffed value of ttl is equal with our established ttl_low
        a_bin.append(0) #note we recive 0


    elif search_buff[2][0] == L_H[1]:
        a_bin.append(1) #note we recive 1


    else:
         print("Ack: Different TTL than low or high")

    for x in range(3): #for each x we alter elements recived during key searching,

        new_a = alterElements(a_bin, x)#from all main dataflow we crate 3 new subsets, in which we search for a key
        b = [0,0,1,0,1,1,1,0] #this is our key

        for n in range(0,len(new_a)):#in each subset
            new_var=[]
            var=new_a[n:n+8]# search only for 8 bits
            if var == b: # if the byte found corresponds to a key
                print("Key found")
                t_f=0#abandon
                n=len(new_a)#abandon


main_iterator = main_iterator +3 #skip two packets


while t_f2 ==0: #decoding starting

    asc_bin = ''

    for x in range(0,8):#read 8 TTL values, each separated by 2 packets

        asc = packet_sniffer(1,main_iterator) #sniff 1 packet

        if asc[2][0] == L_H[0]:
            asc_bin=asc_bin+'0' #note if 0

        elif asc[2][0] == L_H[1]:
            asc_bin=asc_bin+'1' #note if 1

        main_iterator = main_iterator +3 #skip 2 packets
        print(asc_bin) #print on the fly what we are creating
        b = '00101110'
        if asc_bin == b: #checking if we find a key
            t_f2 = 0

            print("Full Message:\n")
            print(full_mess)
            print()
            print("END OF TRANSMISSION !!!!!!")
            t_f2=1
            break


    n=int(asc_bin,2)#from a byte to decimal

    letter=int2bytes(n).decode('utf-8','surrogatepass')#decimaal to ASCII and save that letter
    full_mess=full_mess+letter#put the letter into full message buffer
    print(full_mess)#print out full message

