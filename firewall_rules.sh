# Default policies: drop all incoming traffic but allow outgoing
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

# Allow all traffic on the loopback interface
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

# Allow established and related incoming connections
iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT


# Limit ICMP requests to prevent ICMP flood
iptables -A INPUT -p icmp -m limit --limit 1/s --limit-burst 10 -j ACCEPT
iptables -A INPUT -p icmp -j DROP


# Rate limit UDP to prevent UDP flood
iptables -A INPUT -p udp -m limit --limit 10/s -j ACCEPT
iptables -A INPUT -p udp -j DROP


# Implement SYN cookies and reduce SYN_RECEIVED timer
sysctl -w net.ipv4.tcp_syncookies=1
sysctl -w net.ipv4.tcp_synack_retries=2

# Drop excessive SYN packets to mitigate SYN flood
iptables -A INPUT -p tcp --syn -m limit --limit 1/s --limit-burst 3 -j ACCEPT
iptables -A INPUT -p tcp --syn -j DROP


# Rate limit HTTP(S) connections to mitigate HTTP flood
iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT
iptables -A INPUT -p tcp --dport 443 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT
iptables -A INPUT -p tcp --dport 80 -j DROP
iptables -A INPUT -p tcp --dport 443 -j DROP


# Drop packets that new incoming TCP connections should not be using
iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP
iptables -A INPUT -p tcp ! --syn -m state --state NEW -j DROP
iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP


# Limit SSH connections to prevent brute force attacks
iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -m recent --set
iptables -A INPUT -p tcp --dport 22 -m conntrack --ctstate NEW -m recent --update --seconds 60 --hitcount 10 -j DROP


# Prevent DoS attack by ensuring that only packets that match a known connection are allowed in
iptables -A INPUT -m state --state INVALID -j DROP

# Block packets pretending to be from your local network (spoofing)
iptables -A INPUT -s YOUR_LOCAL_NETWORK -j DROP
