from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking
import smtplib
import getpass


HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "icoutsourcerouter@outlook.com"
TO_EMAIL = "iulianmatei00@gmail.com"
PASSWORD = "weprofessionalsIC"
sendingto = ["iulianmatei00@gmail.com","19768gaency@gmail.com"]
TO_EMAIL2="19768gaency@gmail.com"


SUBJECT = "test dupa eroare"
nume=''
nr_tel=''
email=''
date=''
time=''
state=''
city=''
age=''
insta_handler=''
how_much_per_month=''
how_much_wish=''
obstacle=''
how_much_invest=''

def testmain(request):
    return render(request, 'main2.html')

def home(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'main.html')

def log_in(request):
    if request.method == 'POST':
        username= request.POST.get('username')
        password= request.POST.get('pass')
        
        validade_user = authenticate(request, username=username, password=password)
        if validade_user is not None:
            login(request, validade_user)
            return redirect('main-home') 
        else:
            messages.error(request, 'Incorect date, or the account does not exist')
            #return redirect('gradi-inscriere2')
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        Username= request.POST.get('username')
        email= request.POST.get('email')
        password= request.POST.get('pass')
        password2= request.POST.get('pass2')

        if(password!=password2):
            messages.error(request,'Passwords do not match up')
            return redirect('gradi-register')

        get_all_users_by_username = User.objects.filter(username=Username)
        if get_all_users_by_username:
            messages.error(request, 'The Username is already in use')
            return redirect('main-signup')

        new_user = User.objects.create_user(username=Username, email=email, password=password)
        new_user.first_name = Username
        new_user.save()
        #messages.success(request,'Cont creat!')
        return render(request, 'main.html')
    return render(request, 'signup.html')


def booking(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    global nume,nr_tel,email,date,time,state,city,age,insta_handler,how_much_per_month,how_much_wish,obstacle,how_much_invest
    if request.method == 'POST':

        nume = request. POST['name']
        nr_tel = request. POST['phone']
        email = request. POST['email']
        date = request. POST['date']
        time = request. POST['time']
        state = request. POST['state']
        city = request. POST['city']
        age = request. POST['age']
        insta_handler = request. POST['insta_handler']
        how_much_per_month = request. POST['how_much_per_month']
        how_much_wish =request. POST['how_much_wish']
        obstacle =request. POST['obstacle']
        how_much_invest =request. POST['how_much_invest']

        new_book = Booking (nume=nume,numar_tel=nr_tel,email=email ,date=date,
                            time=time,country=state,city=city,
                               age=age, insta_handler=insta_handler,how_much_per_month=how_much_per_month,
                               how_much_wish=how_much_wish, obstacle=obstacle, how_much_invest=how_much_invest)
        new_book.save()

    TEXT_AUXILIAR=f"\n Instagram ID: {insta_handler} \n How much does he make per month: {how_much_per_month} \n How much he whishes to make: {how_much_wish}\n Obstacle: {obstacle} \n How much is he willing to invest: {how_much_invest}"  
    TEXT=f" Nume: {nume} \n Numar de telefon: {nr_tel} \n E-mail: {email} \n Data: {date} \n Time: {time} \n Tara: {state} \n Oras: {city} " + TEXT_AUXILIAR
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

    smtp = smtplib.SMTP(HOST, PORT)

    status_code, response = smtp.ehlo()
    print(f"[*] Echoing the server: {status_code} {response}")

    status_code, response = smtp.starttls()
    print(f"[*] Starting TLS connection: {status_code} {response}")

    status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
    print(f"[*] Logging in: {status_code} {response}")

    if (len(nume)>0):
        
        smtp.sendmail(FROM_EMAIL, TO_EMAIL, message.encode('utf_8'))
        smtp.sendmail(FROM_EMAIL, TO_EMAIL2, message.encode('utf_8'))
        smtp.quit()

    return render(request, 'booking.html',{})


def see_more_basic(request):
    #return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'see_more_basic.html')


def logoutuser(request):
    logout(request)
    return render(request, 'main.html')