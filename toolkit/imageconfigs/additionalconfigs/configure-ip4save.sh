sed -i '/^COMMIT$/i -A INPUT -p icmp --icmp-type 8 -j ACCEPT' /etc/systemd/scripts/ip4save
