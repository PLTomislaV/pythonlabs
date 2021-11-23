from Crypto.Cipher import AES
import hashlib
import hmac
import secrets
from scapy.layers.inet import Ether
from scapy.layers.inet import UDP
from scapy.layers.inet6 import IPv6
from scapy.all import *

import time
start_time = time.time()

def pad_message(mess):  # passing in in bytes
    iterations = int(0)
    while len(mess) % 16 != 0:  # length of mess modulo 16 not equal to 0
        mess = mess + " ".encode()  # padding with bytes
        iterations = iterations + 1
    return mess, iterations  # we must inform about the length of padding

def forge_packet(message, key, key_mac, ip_src, ip_dst, file_path, source_port, dest_port):
    mode = AES.MODE_CBC  # block chaining mode
    IV = secrets.token_bytes(16)  # LENGTH 16 bytes
    cipher = AES.new(key, mode, IV)
    padded_message = pad_message(message)
    pad_length = padded_message[1]
    padded_message = padded_message[0]

    mask_encryption = secrets.token_bytes(16)
    enc_mask_encryption = cipher.encrypt(mask_encryption)

    mask_mac = secrets.token_bytes(16)
    enc_mask_mac = cipher.encrypt(mask_mac)

    # here we extract using mask
    i = int(len(padded_message) / 16)  # how many chunks of 16 bytes lenth do we have ?
    encryption_block = b""
    for x in range(i):
        extracted_block = padded_message[x * 16:(x + 1) * 16]  # extract data
        if mask_encryption[x % len(mask_encryption)] < 127: # save for later encryption
            encryption_block = encryption_block + extracted_block

    encrypted_block = cipher.encrypt(encryption_block) #encrypt chosen blocks

    a = int(0)
    encrypted_packet = b""
    for x in range(i):  # we asseble our packet with encrypted parts
        if mask_encryption[x % len(mask_encryption)] < 127:
            # should we use an encrypted part of data ?
            encrypted_packet = encrypted_packet + encrypted_block[a * 16:(a + 1) * 16]
            a = a + 1
        else:
            #or original ?
            encrypted_packet = encrypted_packet + padded_message[x * 16:(x + 1) * 16]

    b_pad_length = pad_length.to_bytes(1, 'big')  # pad lentgh conversion
    b_next_header = bytes.fromhex("FD")  # 'experimental value for IPv6'
    final_payload_trailer = IV + encrypted_packet + b_pad_length + b_next_header #assembly of the payload


    #  padded_final_payload_trailer = pad_message(final_payload_trailer) WHAT ABOUT THIS PADDING ?
    padded_final_payload_trailer = final_payload_trailer
    i2 = int(len(padded_final_payload_trailer) / 16)

    extraction_for_mac = mask_encryption + mask_mac
    for x in range(i2):  # we start from 0
        if mask_mac[x % len(mask_mac)] < 127:
            extraction_for_mac = extraction_for_mac + padded_final_payload_trailer[x * 16:(x + 1) * 16]

    our_mac1 = hmac.new(key_mac, extraction_for_mac, hashlib.sha256)
    digested_mac1 = our_mac1.digest()

    final_comb = enc_mask_encryption + enc_mask_mac + padded_final_payload_trailer + digested_mac1

    pckt = Ether() / IPv6(src=ip_src, dst=ip_dst) / UDP(sport=source_port, dport=dest_port) / Raw(load=final_comb)
    c = wrpcap(file_path, pckt, append=True)



TU=9000-82 # transmnission declaration unit in bytes
password_mac = "my mac key yes".encode()
password = "mypassword for en".encode()
ip_src = "2001:db8:3333:4444:5555:6666:7777:8888"
ip_dst = "2001:db8:3333:4444:CCCC:DDDD:EEEE:FFFF"
sport = 2150
dport = 2155
file_path = "E:\MyPcap2.pcap" #path of the packet capture file to be created
if (os.path.isfile(file_path)):
    os.remove(file_path)
    print("Old file removed")

key_mac = hashlib.sha256(password_mac).digest()
key_aes = hashlib.sha256(password).digest()


my_file_movie = open("E:\lol.txt","rb") #input file
my_content = my_file_movie.read(TU) # read chunk of data
x=1
while len(my_content) > 0:
    forge_packet(my_content, key_aes, key_mac, ip_src, ip_dst, file_path, sport, dport)
    print(x)
    x=x+1
    my_content = my_file_movie.read(TU)# read chunk of data

my_file_movie.close()

print("--- %s seconds ---" % (time.time() - start_time))


#if(os.path.isfile(file_path)):
#    os.remove(file_path)
#    print("File removed")

#file1 = open(file_path, "wb")
#file1.write(final_comb)
#print("Written into file")
#file1.close()

#file1 = open(file_path, "r")
#print("File content:")
#print(file1.read())
#file1.close()

# MTU =
# maximum transmission unit, variable size, influences final_payload_trailer_mac size,
# for IPv6 it is a min of 1280 bytes up to 65536 kilo bytes, with regards to WIKI
# packet =  #some binary data of variable size,
# padded_packet = pad_packet(packet) # here we must create a padding function working on binary data
# mask_encryption =
# here we must create a mask to extract data blocks for encryption, it must somehow adapt to size of padded packet
# mask_MAC = #mask for MAC, MAC includes EAMDSP trailer

# final_payload_trailer_mac = IV + padded_encrypted_packet + padding length + next_header + MAC
