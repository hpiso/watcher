from django.core.management.base import BaseCommand, CommandError
from myapp.models import Person
import nmap

class Command(BaseCommand):
    help = 'Scanning address'

    def handle(self, *args, **options):
        print "--- Init nmap ---"
        nm = nmap.PortScanner()

        hugo = '1C:5C:F2:88:09:57'
        alice = 'A0:39:F7:38:A1:97'
        stefan = '58:48:22:53:F4:0A'
        jessica = '98:F1:70:23:2A:DD'

        i = 1
        macAddress = []
        print "--- Scanning 10 times (to be sure we get the mac address) ---"
        while i < 10:

            nm.scan('192.168.0.0/24', arguments='-sn')
            for h in nm.all_hosts():
                if 'mac' in nm[h]['addresses']:
                    if nm[h]['addresses']['mac'] not in macAddress:
                        macAddress += [(nm[h]['addresses']['mac'])]
                        # print(nm[h]['vendor'])
            i += 1
        print "Final List : ", macAddress

        # if hugo in macAddress:
        p = Person.objects.get(name="Hugo")
        p.enabled = False
        p.save()
        print "hugo save "

        self.stdout.write(self.style.SUCCESS('OK'))