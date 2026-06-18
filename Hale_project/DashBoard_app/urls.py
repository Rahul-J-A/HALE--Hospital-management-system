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
        path('pharmacy/',views.pharmacy,name='pharmacy'),
        path('appointment/',views.main_appointment,name='appointment'),
        path('payment/',views.payment,name='payment'),
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
        path('prints<int:id_no>/',views.prints,name='prints'),
        path('department/',views.department,name='department'),
      
        path('updatemed/<int:id_no>/', views.updatemed, name='updatemed'),

        path('updatemed2/<int:id_no>/', views.updatemed2, name='updatemed2'),
        path('add_department/', views.add_department, name='add_department'),
        path('detailed_department/<int:id_no>/', views.detailed_department, name='detailed_department'),

        

        path('med_delete/<int:id_no>/', views.med_delete, name='med_delete'),

        # path('medicine2/',views.medicine2,name='medicine2'),
        path('sellmed/<int:id_no>/', views.sellmed, name='sellmed'),
        path('medication_details/',views.medication_details,name='medication_details'),
        path('staffs/',views.staff,name='staffs'),
        path('staff_add/',views.staff_add,name='staff_add'),
        path('update_staff/<int:id_no>/',views.update_staff,name='update_staff'),
        path('bill/<int:id_no>/',views.bill,name='bill'),
        path('delete_staff/<int:id_no>/',views.delete_staff,name='delete_staff'),

        path('dept_update/<int:id_no>/',views.dept_update,name='dept_update'),

        path('dept_delete/<int:id_no>/',views.dept_delete,name='dept_delete'),
        path('med2/<int:id_no>/',views.med2,name='med2'),
        path('Accounting/', views.Accounting, name='Accounting'),
        path('med_profit/', views.med_profit, name='med_profit'),

        path('patient_profit/', views.patient_profit, name='patient_profit'),
        path('patient_card/<int:id_no>/', views.patient_card, name='patient_card'),




    ]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
    # every link is going to patient check

    # lo
    # ck