from django.shortcuts import render
from .models import Contact,Feedback,Offer,Trainer,Program_details
from django.contrib import messages

# Create your views here.
def home(request):
    offer_list=Offer.objects.all()    # select * from offer just like a SQL query
    
    # send this(offer_list) list  to template so  do it  with following method
    context={
      
       "offer_key":offer_list              # here offer_key is a dictionary and it contain list which is offer_list and in offer_list  objects are saved 

    } 
    return render (request,'driving_app/html/index.html',context)



def aboutus(request):
    return render (request,'driving_app/html/aboutus.html')






def user_feedback(request):

    if request.method=='GET':
       return render (request,'driving_app/html/feedback.html')
    if request.method=='POST':
        print("in if")
        name=request.POST["name"] 
        email=request.POST["email"]
        designation=request.POST["designation"]
        feedback=request.POST["feedback"]
        #print(name,email,designation,feedback)

        feedback_f=Feedback(name=name,email=email,designation=designation,feedback=feedback)
        feedback_f.save()#ORM Framework

        messages.success(request,"We love hearing from you! Thank you for leaving feedback for us.")
        return render (request,'driving_app/html/feedback.html')
    

def contactus(request):

    if request.method=='GET':
          return render (request,'driving_app/html/contactus.html')


    if request.method=='POST':

        # code for data insertion and then send back on the same page with message
          user_name=request.POST["name"] #fetching the values from input field  using these name
          user_email=request.POST["email"]
          user_phone=request.POST["phone"]
          user_query=request.POST["query"]
          #print(user_name,user_email,user_phone,user_query)

          contact=Contact(name=user_name,email=user_email,phone=user_phone,question=user_query)
          contact.save()#ORM Framework
          messages.success(request,"Thank you For Contacting Us We Will Reach You Soon.")
          return render (request,'driving_app/html/contactus.html')
          





def login(request):
    return render (request,'driving_app/html/login.html')


def all_trainers(request):
    trainer_list=Trainer.objects.all()
    context={
            'trainer_data':trainer_list
        }
    return render(request,'driving_app/html/all_trainers.html',context)

def our_programs(request):
    program_info_list=Program_details.objects.all()
    context={
        "program_data":program_info_list
    }
    return render (request,'driving_app/html/our_programs.html',context)


