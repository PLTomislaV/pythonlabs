import os

from Crypto.Cipher import AES
import hashlib
import hmac
from scapy.all import rdpcap
import time
start_time = time.time()

def decode_packet(final_comb):

    incoming_length = int(len(final_comb))
    incoming_not_mac = final_comb[32:incoming_length - 32]

    mode = AES.MODE_CBC  # block mode
    IV = incoming_not_mac[0:16]
    cipher = AES.new(key, mode, IV)

    mask_encryption = cipher.decrypt(final_comb[0:16])
    mask_mac = cipher.decrypt(final_comb[16:32])
    mac = final_comb[incoming_length - 32:incoming_length]

    i2 = int(len(incoming_not_mac) / 16)
    extraction_for_mac = mask_encryption + mask_mac
    for x in range(i2):  # we start from 0
        if mask_mac[x % len(mask_mac)] < 127:
            extraction_for_mac = extraction_for_mac + incoming_not_mac[x * 16:(x + 1) * 16]

    our_mac1 = hmac.new(key_mac, extraction_for_mac, hashlib.sha256)
    our_mac1_di = our_mac1.digest()

    if our_mac1_di == mac:
        print("MAC correct!")

        b_pad_length = incoming_not_mac[len(incoming_not_mac) - 2:len(incoming_not_mac) - 1]
        pad_length = int.from_bytes(b_pad_length, "big")
        encrypted_packet = incoming_not_mac[
                           16:len(incoming_not_mac) - 2]

        i = int(len(encrypted_packet) / 16)
        encryption_block = b""
        for x in range(i):
            extracted_block = encrypted_packet[x * 16:(x + 1) * 16]
            if mask_encryption[x % len(mask_encryption)] < 127:
                encryption_block = encryption_block + extracted_block

        decrypted_block = cipher.decrypt(encryption_block)
        a = int(0)
        decrypted_padded_message = b''
        for x in range(i):  # we start from 0
            if mask_encryption[x % len(mask_encryption)] < 127:
                decrypted_padded_message = decrypted_padded_message + decrypted_block[a * 16:(a + 1) * 16]
                a = a + 1
            else:
                decrypted_padded_message = decrypted_padded_message + encrypted_packet[x * 16:(x + 1) * 16]

        decrypted_padded_message = decrypted_padded_message[0:len(decrypted_padded_message) - pad_length]
        return decrypted_padded_message

    else:
        print("MAC NOT CORRECT!")


pcap = rdpcap("E:\MyPcap2.pcap")
main_iterator = 0
password_mac = "my mac key yes".encode()
key_mac = hashlib.sha256(password_mac).digest()
password = "mypassword for en".encode()
key = hashlib.sha256(password).digest()
file_path = "E:\movie2.txt"
if (os.path.isfile(file_path)):
    os.remove(file_path)
    print("Old file removed")

print(len(pcap))

my_file_movie = open(file_path, "wb")
part = b''
while main_iterator in range(len(pcap)):
    part=decode_packet(pcap[main_iterator].load)
    my_file_movie.write(part)
    print(main_iterator)
    main_iterator = main_iterator+1

my_file_movie.close()

print("--- %s seconds ---" % (time.time() - start_time))



