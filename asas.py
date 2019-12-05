import random 
import os
import smtplib

a=input('please enter your gmail id: ')
    
if a[-9:]!='gmail.com':
    print('invalid email')
    quit()
    
confirm0=input('confirm gmail id:')
m=3
while a!=confirm0:
    if m!=0:
        a=input('please enter your gmail id: ')
        comfirm0=input('confirm gmail id:')
    else:
        print('invalid email')
        quit()
    m-=1

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login('masterkey42069@gmail.com', 'Rishi@1234')
subject='Please verify OTP'
message = str(random.randrange(1000,10000))
msg=f'Subject: {subject}\n\n{message}'
s.sendmail('masterkey42069@gmail.com', a, msg)
OTP=input('Please enter OTP: ')
a+='.txt'
n=3
while OTP!=message:
    if n!=0:
        print('OTP invalid ,A new otp has been sent to your gmail account')
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login('masterkey42069@gmail.com', 'Rishi@1234')
        subject='invalid OTP'
        message = str(random.randrange(1000,10000))
        msg=f'Subject: {subject}\n\n{message}'
        s.sendmail('masterkey42069@gmail.com', a[:-4], msg)
        OTP=input('Please enter new OTP: ')
        n-=1
    else:
        print('exceeded number of trials')
        quit()
else:

    n=0
    while n!=4:
        b=open(a,'a')
        n=int(input('Press 1 to add your data\nPress 2 to delete your data\nPress 3to send email\nPress 4 to quit\n'))
        if n==1:
            email=input('Enter account name: ')
            confirm=input('Are u sure this is the account you want?(Y/N): ')
            while confirm.upper()!='Y':
                email = input('Enter account name: ')
                confirm = input('are u sure this is the account you want?(Y/N): ')
            username=input('Enter the username: ')
            confirm1=input('Are you sure this is your username for the given account?(Y/N)')
            while confirm1.upper()!='Y':
                username = input('Enter account name: ')
                confirm1 = input('are u sure this is the account you want?(Y/N): ')
            password=input('enter corresponding password: ')
            confirm2=input('confirm password: ')
            while confirm2!=password:
                password = input('enter corresponding password: ')
                confirm2 = input('confirm password: ')


            l1,l2,l3=[],[],[]
            l1.append(email)
            l2.append(username)
            l3.append(password)
            data = list(zip(l1, l2, l3))
            for dat in data:
               print(dat, file=b)
            b.close()
        elif n==2:
            b.close()
            os.remove(a)
            

        elif n==3:
            b=open(a,'r')
            x=input('do you want to view everything(Y/N)')
            if x.upper()=='Y':
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login('masterkey42069@gmail.com', 'Rishi@1234')
                subject='Full Data'
                message = b.read()
                msg=f'Subject: {subject}\n\n{message}'
                s.sendmail('masterkey42069@gmail.com', a[:-4], msg)
            else:
                
                y=input('which account do u want to view:')
                for i in b:
                    if i.split(',')[0][2:-1]==y:
                        s = smtplib.SMTP('smtp.gmail.com', 587)
                        s.starttls()
                        s.login('masterkey42069@gmail.com', 'Rishi@1234')
                        subject='Password for corresponding account'
                        message = i
                        msg=f'Subject: {subject}\n\n{message}'
                        s.sendmail('masterkey42069@gmail.com', a[:-4], msg)
                        break
    else:
        print('thank you for using master key')
        b.close()
        quit()
                
        
