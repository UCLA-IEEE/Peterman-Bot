import subprocess
from sets import Set

class Scanner(object):

    def __init__(self):
        pass

    def scan_arp(self, mac_address_map):
        """
        Runs an arp-scan for the mac addresses on the network.
        Checks the arp output for any known mac addresses

        :param mac_address_map: map from officer names to their mac addresses
        :return: a set containing the names of the officers in the lab
        """

        try:
            arp_output = subprocess.check_output(["sudo", "arp-scan", "-l"])
        except CalledProcessError:
            print 'Error in running arp-scan for network output.'
            exit()

        officers_in_lab = Set()

        for key in mac_address_map:
            mac_address = mac_address_map[key]
            for line in arp_output.splitlines():
                if mac_address in line:
                    officers_in_lab.add(key)

        return officers_in_lab
