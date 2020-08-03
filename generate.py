#!/usr/bin/env python
# Script by Mitch Bradford
# Dependencies - Python 3
# Instructions - run generate.py

# -----------------------------------------------------------------------
#Imports go here
from getpass import getpass
from base_config import template

# -----------------------------------------------------------------------
# Prompts
username = input('Enter the management username:')
password = getpass('Enter the management password')
secret = getpass('Enter the secret password')
hostname = input('Enter the hostname:')
domain = input('Enter the domain name:')
management_vlan = input('Enter the management VLAN:')
#look into using ipv4 module like the config audit script
management_ip = input('Enter the management VLAN IP address and subnet eg: 10.0.0.1 255.255.255.0:')
num_of_ports = input('Enter the number of ethernet ports:')
# -----------------------------------------------------------------------
# Generator Configs
def generate_configs():
	with open("config.txt", "w") as text_file:
		
		# Apply management credentials and enable password
		print('username ' + username + ' secret 0 ' + password, file=text_file)
		print('enable secret 0 ' + secret, file=text_file)
		
		print('hostname ' + hostname, file=text_file)
		print('ip domain name ' + domain, file=text_file)

		#management VLAN
		print('interface vlan ' + management_vlan, file=text_file)
		
		# Ip address
		print(' ip address ' + management_ip, file=text_file)
		print(' no shut', file=text_file)
		
		#ask for number of ports
		print('default interface range gi1/0/' + num_of_ports, file=text_file)
		print(' switchport mode access', file=text_file)
		#probably ask for user vlan here
		print(' switchport access vlan 1', file=text_file)
		print(' no shut', file=text_file)

		print('interface gi1/0/' + num_of_ports, file=text_file)
		print(' switchport mode access', file=text_file)
		print(' switchport access vlan 1', file=text_file)
		print(' no spanning-tree portfast', file=text_file)
		print(' spanning-tree portfast disable', file=text_file)
		print(' spanning-tree bpduguard disable', file=text_file)
		print(' storm-control broadcast level 10.00', file=text_file)
		print(' no shut', file=text_file)

		# Apply all other commands that don't require input
		for commands in template:
			print(commands, file=text_file)
		
# -----------------------------------------------------------------------
def main():
	"""
	Run Generator Configs function
	"""
	generate_configs()
	
if __name__ == "__main__":
	main()
