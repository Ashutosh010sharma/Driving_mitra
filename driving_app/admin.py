from django.contrib import admin
from .models import Contact,Feedback,Offer,Trainer,Program_details,Vehicle_model,Vehicle_details,Trainee,Ride_log
# Register your models here.

class Offer_Admin(admin.ModelAdmin):
    list_display=('contents', 'date' )
    search_fields=('date',)


class Trainer_Admin(admin.ModelAdmin):
    list_display=('name', 'trainerid','otherdetails' )
    search_fields=('cityname',)
    list_filter=['trainerid','cityname']


class Program_details_Admin(admin.ModelAdmin):
    list_display=('program_name', 'charges' )
    
    list_filter=['program_name']    


class Vehicle_details_Admin(admin.ModelAdmin):
    list_display=('vehicle_no', 'device_no','vehicle_model')
    
    list_filter=['vehicle_no']


class Trainee_Admin(admin.ModelAdmin):
    list_display=('name', 'trainee_id','program' ,'trainer')
    
    list_filter=['trainee_id']


class Ride_log_Admin(admin.ModelAdmin):
    list_display=('start_point', 'destination','trainer','date')


admin.site.register(Contact)
admin.site.register(Feedback)
admin.site.register(Offer,Offer_Admin)
admin.site.register(Trainer,Trainer_Admin)
admin.site.register(Program_details,Program_details_Admin)
admin.site.register(Vehicle_model)
admin.site.register(Vehicle_details,Vehicle_details_Admin)
admin.site.register(Trainee,Trainee_Admin)
admin.site.register(Ride_log,Ride_log_Admin)




admin.site.site_header="DrivingMitra School Portal Administration"
admin.site.site_title="Admin Dashboard"
admin.site.index_title=" Welcome To DrivingMitra"