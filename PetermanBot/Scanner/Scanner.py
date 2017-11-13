import subprocess

class Scanner(object):

    def __init__(self):
        pass

    def scan_arp(self, mac_address_map):
        arp_output = subprocess.check_output(["sudo", "arp-scan", "-l"])

        officers_in_lab = []

        for key in mac_address_map:
            mac_address = mac_address_map[key]
            for line in arp_output.splitlines():
                if mac_address in line:
                    officers_in_lab.append(key)

        return officers_in_lab
