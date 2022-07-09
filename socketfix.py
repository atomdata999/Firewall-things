import os
import sys
import time
#something simple
#blocks all socket methods
#https://unix.stackexchange.com/questions/139285/limit-max-connections-per-ip-address-and-new-connections-per-second-with-iptable this can help you
#https://serverfault.com/questions/353130/iptables-and-multiple-ports this can help you
#reverse proxy https://stackoverflow.com/questions/35863265/reverse-proxy-iptables
#this is good to https://www.cyberciti.biz/faq/linux-kernel-etcsysctl-conf-security-hardening/
# this is only if you can't whitelist a certain application or is to much of a hastle to do so
while True:
	print("BLOCKING IPS")
	os.system("netstat -n -p | grep SYN_REC | awk '{print $5}' | awk -F: '{print $1}' | sort | uniq >> black.txt")
	ips = open("black.txt", "r").readlines()
	for ip in ips:
		if ip == "":
			print("NOT BEING ATTACKED!!!")
		elif ip == "your ip":
			print("NOT BEING ATTACKED!!!")
		else:
			print("Has been attacked!!!")
			os.system(f"iptables -A INPUT -s {ip} -j DROP")
