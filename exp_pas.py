import subprocess
import re
import time


def get_ssid_names():
	cmd_out = subprocess.getoutput('netsh wlan show profiles')  
	return re.findall(r':\s(.*)', cmd_out)[1:]  # Extract profile names


def get_ssid_passwords(ssid: str):
	pattern = re.search(r'Key Content.*', subprocess.getoutput \
					   ('netsh wlan show profile name={} key=clear'.format(ssid)))

	if pattern:
		return pattern.group().split(':')[1].strip()	# extract password from the output.


if __name__ == '__main__':

	ssids = get_ssid_names() 

	for ssids, passkeys in zip(ssids, list(map(get_ssid_passwords, ssids))):
		print(ssids, (15-len(ssids)) * ' ', passkeys)

