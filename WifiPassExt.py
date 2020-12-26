import subprocess

results = []

ssids = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
ssids = [line.split(':')[1][1:-1] for line in ssids if 'All User Profile' in line]

for id in ssids:
    passwords = subprocess.check_output(['netsh','wlan','show','profile',id,'key=clear']).decode('utf-8').split('\n')
    passwords = [line.split(':')[1][1:-1] for line in passwords if 'Key Content' in line]
    try:
        #print(f'Wifi Name : {id}\nPassword : {passwords[0]}\n')
        results.append(f'Wifi Name : {id}\nPassword : {passwords[0]}\n\n')
    except IndexError:
        #print(f'\nWifi Name : {id}\nOpen Network\n')
        results.append(f'Wifi Name : {id}\nOpen Network\n\n')

with open("wifi's.txt",'a') as f:
    f.writelines(results)
    

    