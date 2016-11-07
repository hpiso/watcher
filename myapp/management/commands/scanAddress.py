from django.core.management.base import BaseCommand, CommandError
from myapp.models import Object
import nmap
import datetime

class Command(BaseCommand):
    help = 'Scanning address'

    def handle(self, *args, **options):
        print "--- Init nmap ---"
        nm = nmap.PortScanner()

        i = 1
        macAddress = []
        print "--- Scanning 10 times (to be sure we get the mac address) ---"
        while i < 10:
            nm.scan('192.168.0.0/24', arguments='-sn')
            for h in nm.all_hosts():
                if 'mac' in nm[h]['addresses']:
                    if nm[h]['addresses']['mac'] not in macAddress:
                        macAddress += [(nm[h]['addresses']['mac'])]
                        print(nm[h]['vendor'])
            i += 1
        print "Final List : ", macAddress

        for address in macAddress:
            o = Object(mac_address=address, date_time=datetime.datetime.now())
            o.save()