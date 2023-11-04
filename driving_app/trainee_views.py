from django.shortcuts import render
from django.contrib import messages
from .models import Program_details,Trainee,Ride_log



def admission(request):
    if request.method=='GET':
        program_list=Program_details.objects.all()
        context={

            "program_key":program_list
        }
        return render (request,'driving_app/trainee/admission.html',context)
    if request.method=='POST':
        name=request.POST["name"] 
        email=request.POST["email"]
        phone=request.POST["phone"]
        address=request.POST["address"]
        programe_name_trainee=request.POST["programe_name"]
        transaction_no=request.POST["transaction"]
        #print(name,email,phone,address,programe_name,transaction_no)
        program_obj=Program_details.objects.get(program_name=programe_name_trainee)
        trainee_obj=Trainee(name=name,email=email,phone=phone,address=address,program=program_obj,transaction_no=transaction_no)
        trainee_obj.save()
        messages.success(request,"Congratulations! Your Admission Process  Has Been Successfully Completed.")

        program_list=Program_details.objects.all()
        context={

            "program_key":program_list
        }

        return render (request,'driving_app/trainee/admission.html',context)
    

def trainee_login(request):    
     if request.method=="GET":
         return render (request,'driving_app/trainee/login.html')
     if  request.method=="POST":
          id=request.POST["userid"]
          password=request.POST["userpass"]
          print(id,password)
          trainee_list=Trainee.objects.filter(trainee_id=id,password=password)
          x=len(trainee_list)
         # print("length is ", x)
          if x>0:
                trainee_object=Trainee.objects.get(trainee_id=id)
                request.session["session_key"]=id
                context={"trainee_data":trainee_object}
                
                return render (request,'driving_app/trainee/trainee_home.html',context)
          else:

               messages.error(request,"Invalid Credential")
               return render (request,'driving_app/trainee/login.html')




def trainee_home(request):
    logged_in_trainee=request.session["session_key"]
    trainee_logged_in_object=Trainee.objects.get(trainee_id=logged_in_trainee)
    context={"trainee_data": trainee_logged_in_object}
    return render(request,'driving_app/trainee/trainee_home.html')

def editprofile_trainee(request):
    if request.method=="GET":
       logged_in_trainee=request.session["session_key"]
       trainee_logged_in_object=Trainee.objects.get(trainee_id=logged_in_trainee)
       context={"trainee_data":trainee_logged_in_object}

       
       return render (request,'driving_app/trainee/editprofile_trainee.html',context)
    if request.method=="POST":
           edit_email=request.POST["email"]
           edit_phone=request.POST["phone"]
           edit_address=request.POST["address"]
           
           logged_in_trainee=request.session["session_key"]
           trainee_logged_in_object=Trainee.objects.get(trainerid=logged_in_trainee)
           trainee_logged_in_object.email=edit_email

           trainee_logged_in_object.phone= edit_phone
           trainee_logged_in_object.address=edit_address
           
           trainee_logged_in_object.save()
           context={"trainee_data": trainee_logged_in_object}
    return render(request,"driving_app/trainee/editprofile_trainee.html")


def trainee_logout(request):
      del request.session["session_key"]
      messages.success(request,"🤷‍♂️Successfully logout")

      return render (request,'driving_app/trainee/login.html')
  
def assigned_trainer(request):
    id=request.session["session_key"]
      
    trainee=Trainee.objects.get(trainee_id=id)
   
    context={"trainee_data":trainee}

    return render (request,'driving_app/trainee/assigned_trainer.html',context)



def previous_ride_details(request):
    id=request.session['session_key']
    trainee_logged_in_object=Ride_log.objects.filter(trainee=id)
    context={
        'trainee_data': trainee_logged_in_object
    }
    return render(request,'driving_app/trainee/previous_ride_details.html',context)
    