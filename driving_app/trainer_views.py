from django.shortcuts import render
from django.contrib import messages
from .models import Trainer ,Trainee,Ride_log,Vehicle_details

def trainer_login(request): 
     if request.method=="GET":
         return render (request,'driving_app/trainer/login.html')
     if  request.method=="POST":
          id=request.POST["userid"]
          password=request.POST["userpass"]
          #print(id,password)
          trainer_list=Trainer.objects.filter(trainerid=id,password=password)
          x=len(trainer_list)
         # print("length is ", x)
          if x>0:
                trainer_object=Trainer.objects.get(trainerid=id)
                request.session["session_key"]=id
                context={"trainer_data":trainer_object}
                
                return render (request,'driving_app/trainer/trainer_home.html',context)
          else:

               messages.error(request,"Invalid Credential")
               return render (request,'driving_app/trainer/login.html')



def editprofile_trainer(request): 
      if request.method=="GET":
       logged_in_trainer=request.session["session_key"]
       trainer_logged_in_object=Trainer.objects.get(trainerid=logged_in_trainer)
       context={"trainer_data":trainer_logged_in_object}

       
       return render (request,'driving_app/trainer/editprofile_trainer.html',context)
      if request.method=="POST":
           edit_email=request.POST["email"]
           edit_phone=request.POST["phone"]
           edit_address=request.POST["address"]
           edit_city=request.POST["city"]
           logged_in_trainer=request.session["session_key"]
           trainer_logged_in_object=Trainer.objects.get(trainerid=logged_in_trainer)
           trainer_logged_in_object.email=edit_email

           trainer_logged_in_object.phone= edit_phone
           trainer_logged_in_object.address=edit_address
           trainer_logged_in_object.cityname=edit_city
           trainer_logged_in_object.save()
           context={"trainer_data": trainer_logged_in_object}
      return render (request,'driving_app/trainer/trainer_home.html',context)

def  trainer_home(request):
      logged_in_trainer=request.session["session_key"]
      trainer_logged_in_object=Trainer.objects.get(trainerid=logged_in_trainer)
      context={"trainer_data": trainer_logged_in_object}
      return render (request,'driving_app/trainer/trainer_home.html',context)

def trainer_logout(request):
      del request.session["session_key"]
      messages.success(request,"🤷‍♂️Successfully logout")

      return render (request,'driving_app/trainer/login.html')


def all_trainee(request):
      id= request.session['session_key']
      trainer_obj=Trainer.objects.get(trainerid=id)
      trainee_info_list=Trainee.objects.filter(trainer=trainer_obj)
      context={
            'trainee_data':trainee_info_list
      }
      return render (request,'driving_app/trainer/all_trainee.html',context)


def ride_log(request):
      if request.method=='GET':
            id= request.session['session_key']
            trainer_obj=Trainer.objects.get(trainerid=id)
            trainee_list=Trainee.objects.filter(trainer=trainer_obj)
            context={
            'trainee_id_key':trainee_list
                  }
            return render (request,'driving_app/trainer/ride_log.html',context)

      if request.method=='POST':
            id=request.session['session_key']
            vechile_no=request.POST['Vechile Number']
            vechile_obj=Vehicle_details.objects.get(vehicle_no=vechile_no)
            start_point=request.POST['start_point']
            destination=request.POST['destination']
            time=request.POST['time']
            date=request.POST['date']
            trainee_id=request.POST['name']
            ride_log_obj=Ride_log(vehicle_details=vechile_obj,start_point=start_point,destination=destination,trainer=id,trainee=trainee_id,start_time=time,date=date)
            ride_log_obj.save()
            
            id=request.session['session_key']
            trainer_obj=Trainer.objects.get(trainerid=id)
            trainee_list=Trainee.objects.filter(trainer=trainer_obj)
            context={
                  'trainee_id_key':trainee_list
            }
            
            return render(request,'driving_app/trainer/ride_log.html',context)
      
      
      
      
def trainee_performance(request):
      
      if request.method=='GET':
    
            id=request.session["session_key"]
            trainer_obj=Trainer.objects.get(trainerid=id)
            trainee_list=Trainee.objects.filter(trainer=trainer_obj)

            ride_details_list=Ride_log.objects.filter(trainer=id)

            context={

                    "ride_details":ride_details_list
                }  



            return render (request,'driving_app/trainer/trainee_performance.html',context)  
      if request.method=="POST": 
             ride_id=request.POST["rideid"]
             tp=request.POST["tp"]
             ride_obj=Ride_log.objects.get(id=ride_id)
             ride_obj.performance=tp
             ride_obj.save()
              
             id=request.session["session_key"]
             trainer_obj=Trainer.objects.get(trainerid=id)
             trainee_list=Trainee.objects.filter(trainer=trainer_obj)

             ride_details_list=Ride_log.objects.filter(trainer=id)
            #  trainee_name_list=[]
            #  for rd in ride_details_list:
                  
            #      trainee_obj=   Trainee.objects.filter(trainee_id=rd.trainee)
            #      name=trainee_obj[0].name
            #      print(name)
            #      trainee_name_list.append(name)

             context={

                "ride_details":ride_details_list,
                # "namelist":trainee_name_list
                    }  


            
      return render (request,'driving_app/trainer/trainee_performance.html',context) 
       
      
                  
