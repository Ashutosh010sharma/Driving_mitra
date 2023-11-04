
from django.urls import path,include
from.import views,trainee_views,trainer_views
urlpatterns = [
    
    path("",views.home,name="home" ),
    path("aboutus/",views.aboutus,name="aboutus" ),
    path("feedback/",views.user_feedback,name="feedback" ),
    path("contactus/",views.contactus,name="contactus" ),
    path("login/",views.login,name="login"),
    path("admission/",trainee_views.admission,name="admission"),
    path("trainee_login/",trainee_views.trainee_login,name="trainee_login"),
    path("trainer_login/",trainer_views.trainer_login,name="trainer_login"),
    path("editprofile_trainer/",trainer_views.editprofile_trainer,name="editprofile_trainer"),
    path("trainer_home/",trainer_views.trainer_home,name="trainer_home"),
    path("trainer_logout/",trainer_views.trainer_logout,name="trainer_logout"),
    path("all_trainers/",views.all_trainers,name="all_trainers"),
    path("trainee_home/",trainee_views.trainee_home,name="trainee_home"),
    path("editprofile_trainee/",trainee_views.editprofile_trainee,name="editprofile_trainee"),
    path("trainee_logout/",trainee_views.trainee_logout,name="trainee_logout"),
    path("all_trainee/",trainer_views.all_trainee,name="all_trainee"),
    path("assigned_trainer/",trainee_views.assigned_trainer,name="assigned_trainer"),
    path("ride_log/",trainer_views.ride_log,name="ride_log"),
    path("previous_ride_details/",trainee_views.previous_ride_details,name="previous_ride_details"),
    path("trainee_performance/",trainer_views.trainee_performance,name="trainee_performance"),
    path("our_programs/",views.our_programs,name="our_programs" ),    
]