from django.urls import path
from DashBoard_app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
if settings.DEBUG:
    urlpatterns=[
        # path('admin/', admin.site.urls,name='admin'),
        path('',views.home),
        path('logout/',views.logout_view,name='logout'),
        path('home/',views.home,name='home'),
        
        path('login/',views.login,name='login'),
        path('register/',views.register,name='register'),
     
        path('about/',views.about,name='about'),
        path('contact/',views.contact,name='contact'),
        path('feedback/',views.feedback,name='feedback'),
        path('dashboard/', views.dashboard, name='dashboard'),
        path('doctor/',views.addsection,name='doctor'),
        path('patient/',views.patient,name='patient'),
        path('nurse/',views.patient,name='nurse'),
        path('laboratorist/',views.patient,name='laboratorist'),
        path('appointment/',views.main_appointment,name='appointment'),
        path('accountant/',views.patient,name='accountant'),
        path('payment/',views.patient,name='payment'),
        path('bedstatus/',views.patient,name='bedstatus'),
        path('bloodbank/',views.patient,name='bloodbank'),
        path('medicine/',views.medicine,name='medicine'),
        path('reg_patient/',views.reg_patient,name='reg_patient'),
        path('reg_view_patient/',views.reg_view_patient,name='reg_view_patient'),
        path('update<str:id_no>/',views.update_section, name='update'),
        path('delete<str:id_no>/',views.delete_section, name='delete'),
        path('add_appoint<str:id_no>/',views.add_appoint, name='add_appoint'),
        path('updatepatient<str:id_no>/', views.updatepatient, name='updatepatient'),
        path('reg_update_patient<str:id_no>/',views.reg_update_patient,name='reg_update_patient'),
        path('reg_update/',views.reg_update,name='reg_update'),
        path('appointsave/<int:patient_id>/<str:doctor_id>/',views.appointsave,name='appointsave'),
        path('demo_appoint_save/',views.demo_appoint_save,name='demo_appoint_save'),
       

        path('recievedappointments<int:id_no>/',views.recievedappointments,name='recievedappointments'),
        path('recievedappointmentsmark/',views.recievedappointments_mark,name='recievedappointmentsmark'),
        path('addmed/',views.addmed,name='addmed'),




    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
    # every link is going to patient check

    # lo
    # ck