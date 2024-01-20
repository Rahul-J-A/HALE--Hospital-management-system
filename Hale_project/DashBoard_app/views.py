from django.shortcuts import render,redirect
from django.db.models import Q
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from .models import*
from django.urls import reverse
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from datetime import date
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.http import JsonResponse
# Create your views here.
def bill(request):
    return render(request, 'bill.html')
def home(request):
    return render(request, 'home.html')
def main_appointment(request):
   
    appoint_detail=ADDSECTION.objects.all()
    # query=request.GET['search']
    query = request.POST.get('search')
    # print("query data")
    # print(query)
    if request.method=="POST":
        if query:
            print("hii query here")
            section_data2 = appoint_detail.filter(
                Q(sec_op_no__icontains=query) |   # Case-insensitive name search athu case ayaalum value get cheyyum
                Q(sec_doctor__icontains=query) |
                Q(sec_department__icontains=query) |
                Q(sec_date__icontains=query) |
                Q(sec_duration1__icontains=query)
            )
            print("Filtered Data Count:", section_data2.count())
            # context={
            #     'all_data': patients_all_data,
            #     'searched_data': patients_all_data2,
            # }
            context={
                "appoint_detail":appoint_detail,
                "searched_value":section_data2,
                
                }
            return render(request,"main_appointment.html",context)
        else:
            context={"msg":"No data  found", "appoint_detail":appoint_detail,}
            return render(request, 'main_appointment.html',context)
   
    else:
        appoint_detail=ADDSECTION.objects.all()
        context={
            "appoint_detail":appoint_detail,
            
            
        }
        return render(request, 'main_appointment.html',context)
     
    # return render(request, 'main_appointment.html',context)
# duplicate
def demo_appoint_save(request):
    context={
        'msg':"Appointment Saved",


    }

    return render(request, 'main_appointment.html',context)

def main_appointment2(request,msg):
    # msg=str(msg)
    passed_data = request.GET.get('msg', None)
    appoint_detail=ADDSECTION.objects.all()
    # query=request.GET['search']
    query = request.POST.get('search')
    # print("query data")
    # print(query)
    if request.method=="POST":
        if query:
            print("hii query here")
            section_data2 = appoint_detail.filter(
                Q(sec_op_no__icontains=query) |   # Case-insensitive name search athu case ayaalum value get cheyyum
                Q(sec_doctor__icontains=query) |
                Q(sec_department__icontains=query) |
                Q(sec_date__icontains=query) |
                Q(sec_duration1__icontains=query)
            )
            print("Filtered Data Count:", section_data2.count())
            # context={
            #     'all_data': patients_all_data,
            #     'searched_data': patients_all_data2,
            # }
            context={
                "appoint_detail":appoint_detail,
                "searched_value":section_data2,
                
                }
            return render(request,"main_appointment.html",context)
        else:
            context={"msg":"No data  found", "appoint_detail":appoint_detail,}
            return render(request, 'main_appointment.html',context)
   
    else:
        appoint_detail=ADDSECTION.objects.all()
        context={
            "appoint_detail":appoint_detail,
            
            
        }
        return render(request, 'main_appointment.html',context)
         

def delete_section(request,id_no):
    try:
        # Try to convert id_no to an integer
        id_no = int(id_no)
        update_value = ADDSECTION.objects.get(id=id_no)
        
    except ValueError:
        context={
            "msg":"id problem update_section"
        }
        return render(request,'doctor_section.html',context)
    showdata=ADDSECTION.objects.all()#to show the list of sections
    # context2={
    #     "saved_data":showdata
    # }
    update_value = ADDSECTION.objects.get(id=id_no)
    del_user=request.user.username
    if update_value.sec_doctor==del_user:
        delete_value=ADDSECTION.objects.get(id=id_no)
        print(delete_value)
        delete_value.delete()
        return redirect(addsection)
    
    else:
        context={"msg":"you don't have the permisiion to delete others data","up_val":update_value,
                        "saved_data":showdata,}
    
        return render(request,'doctor_section.html',context)#redirect for better use but no message
def appointsave(request,patient_id,doctor_id):
    print(patient_id,doctor_id)
    doctordetail = ADDSECTION.objects.get(id=doctor_id)
    patientdetail = PatientTable.objects.get(id=patient_id)
    if request.method=='POST':
        
        appointmentdetails=APPOINTMENTSAVED(app_id=patientdetail.id,app_Name=patientdetail.patient_name,app_age=patientdetail.patient_age,app_gender=patientdetail.patient_gender,app_Appointed_doctor=doctordetail.sec_doctor,app_discription=patientdetail.patient_discription,app_department=doctordetail.sec_department,app_op_no=doctordetail.sec_op_no,app_doctor_id=doctordetail.id,app_mark=False)
        appointmentdetails.save()
        # for attr, value in appointmentdetails.__dict__.items():
        #     print(f"{attr}: {value}")
    context={
        
             
        'msg':"Successfully appointment received"}
    # return redirect('main_appointment', msg=context.get('msg', ''))
    return render(request,"demo_appoint_save.html",context)




def add_appoint(request,id_no,):
    selected_option = request.POST.get('select_patient', 'none')  # Adjust the name as per your form
    selected_option_values = selected_option.split(',')
    
    selected_option_id = selected_option_values[0]
    if id_no:
        id_detail=ADDSECTION.objects.get(id=id_no)
    
    
    
    option=PatientTable.objects.all()
    doctorname=id_detail.sec_doctor
    # for i in id_detail:
    # print(id_detail.sec_doctor)
    # selected_patient=request.GET.get('select_patient', None)
    
    
    if request.method=='POST':
        selected_option = request.POST.get('select_patient', 'none')  # Adjust the name as per your form
        selected_option_values = selected_option.split(',')
        print(selected_option_values[0])
        selected_option_id = selected_option_values[0]
       

        if request.POST['search']:
            search_val = request.POST['search']
            print(search_val)
            section_data2 = option.filter(
                Q(patient_name__icontains=search_val) |   # Case-insensitive name search athu case ayaalum value get cheyyum
                Q(patient_age__icontains=search_val) |
                Q(patient_phone__icontains=search_val) |
                Q(patient_gender__icontains=search_val) 
               
            )
            context={
                "searched_data":section_data2,
                "appoint_detail":id_detail,
                "patient_data":option,
            }
            return render(request,"appointment_popup.html",context)
        else:
            
            if selected_option_id and selected_option_id.isdigit():
                appoint_box=PatientTable.objects.filter(id=selected_option_id)
                print("inside box")
                print(appoint_box)
                context={
                "appointed_patient":appoint_box,
                    "appoint_detail":id_detail,
                    "patient_data":option,
                }
                return render(request,"appointment_popup.html",context)
            else:
                    context={
                            
                            "appoint_detail":id_detail,
                            "patient_data":option,
                            
                        }
                    return render(request,"appointment_popup.html",context)
    print(id_detail)
    context={
                "appoint_detail":id_detail,
                "patient_data":option,
                
                
                
                }
    
   

    return render(request,"appointment_popup.html",context)








def update_section(request,id_no):
    print("update section")
    try:
        # Try to convert id_no to an integer
        id_no = int(id_no)
        update_value = ADDSECTION.objects.get(id=id_no)
        
    except ValueError:
        context={
            "msg":"id problem update_section"
        }
        return render(request,'doctor_section.html',context)
    showdata=ADDSECTION.objects.all()#to show the list of sections
    # context2={
    #     "saved_data":showdata
    # }
    update_value = ADDSECTION.objects.get(id=id_no)
    up_user=request.user.username
    # print("here1")
    if request.method=='POST':
        # print("posted")
        # print(up_user)
        # print(update_value.sec_doctor)
        if update_value.sec_doctor==up_user:#only if pazhaya user anengil mathram update cheyyan pattum

            update_value.sec_date=request.POST['date']
            update_value.sec_duration1=request.POST['duration1']
            update_value.sec_duration2=request.POST['duration2']
            update_value.sec_department=request.POST['departments']
            update_value.sec_op_no=request.POST['op_no']
            update_value.sec_break1=request.POST['break1']
            update_value.sec_break2=request.POST['break2']
            # update_value.sec_doctor=request.POST[up_user]
            update_value.save()
            print("here3")
            return redirect(addsection)
        else:
            context={"msg":"you dont have the permission to Update others data",
                     "up_val":update_value,
                        "saved_data":showdata,}
            return render(request,'doctor_section.html',context)
    context={
        "up_val":update_value,
        "saved_data":showdata,
        "checked":True
    }
    return render(request,'doctor_section.html',context)
def addsection(request):
    showdata=ADDSECTION.objects.all()
    verify_user1=request.user.username
    doctorname=User.objects.get(username=verify_user1)
    appointmentdetail=APPOINTMENTSAVED.objects.filter(app_Appointed_doctor=doctorname)


    
    context={
        "saved_data":showdata,
        "appointmentdetail":appointmentdetail
        
    }
    if request.method=='POST':
        date = request.POST['date']
        duration1=request.POST['duration1']
        duration2=request.POST['duration2']
        departments=request.POST['departments']
        op_no=request.POST['op_no']
        break1=request.POST['break1']
        break2=request.POST['break2']
        verify_user=request.user.username
       
        # print(verify_user)
        # if verify_user==User.objects.get(username=verify_user):
        try:
            user_instance=User.objects.get(username=verify_user)
        except User.DoesNotExist:
            context={
                'msg':"you are not a valid user"
            }
            return render(request,'doctor_section.html',context)
        print(user_instance)
        if user_instance is not None:  
            savesection=ADDSECTION(sec_date=date,sec_duration1=duration1,sec_duration2=duration2,sec_department=departments,sec_op_no=op_no,sec_break1=break1,sec_break2=break2,sec_doctor=user_instance)
            savesection.save()  
            date=""
            duration1=''
            duration2=''
            departments=''
            op_no=''
            break1=''
            break2=''
            print("correctuser")
            return redirect(addsection)    

        print(date,duration1,duration2,departments,op_no,break1,break2)
       
    # print(request.user.username)
    return render(request,'doctor_section.html',context)


# def recievedappointments(request,id_no):
#     verify_user1=request.user.username
#     doctorname=User.objects.get(username=verify_user1)
#     print(doctorname)
#     appointmentdetail=APPOINTMENTSAVED.objects.filter(app_Appointed_doctor=doctorname)
    
#     appointed_status = request.POST.get('appoint_status', 'false').lower() == 'true'
#     print(appointed_status)
   
        
#         # Your existing code...
#     markeddata = APPOINTMENTSAVED.objects.filter(id=id_no)
#     for i in markeddata:
#         if not i.app_mark:
#             print("data varum")
#             print(i.app_Name)
    
#     # marked data has the table of the marked appointment
#     # markeddata=APPOINTMENTSAVED.objects.filter(id=id_no)
#     if appointed_status:
#         markeddata.app_mark = True
#         print( markeddata.app_mark)
#         markeddata.update(app_mark=True)
#         # markeddata.save()

           
      
    
#     context={
        
#         "appointmentdetail":appointmentdetail
        
#     }
#     return render(request, 'doctor_received_appoint.html',context)
    
    
    
    # return redirect(recievedappointments_mark)
# def recievedappointments(request, id_no):
#     print(".........................")
#     print(id_no)
#     print(".........................")
#     verify_user1 = request.user.username
#     doctorname = User.objects.get(username=verify_user1)
#     print(doctorname)
#     appointmentdetail = APPOINTMENTSAVED.objects.filter(app_Appointed_doctor=doctorname)

#     if request.method == 'POST':
#         appointed_status = request.POST.get('appoint_status', 'false').lower() == 'true'
#         print(appointed_status)

#         # Get the specific appointment instance
#         markeddata = get_object_or_404(APPOINTMENTSAVED, id=id_no)
#         print(markeddata)
#         # Update the app_mark field
#         markeddata.app_mark = appointed_status
#         markeddata.save()

#         # Redirect to the same page or any other page you prefer after the update
#         return redirect('recievedappointments', id_no=id_no)

#     context = {
#         "appointmentdetail": appointmentdetail
#     }

#     return render(request, 'doctor_received_appoint.html', context)

def recievedappointments(request,id_no):
    doctorname = request.user.username
    
    make_this_appoint=APPOINTMENTSAVED.objects.get(id=id_no)
    # appointed_status = request.GET.get('appoint_status', 'false').lower() == 'true'
    # print(request.GET)
    if request.method == 'POST':
        appoint_value = request.POST.get('notappoint_false')
        print(appoint_value)
        print('value recieved')
        verify_status = request.POST.get('virify_val')
            
        print(verify_status)
        # if appoint_value=='deselect'
        make_this_appoint=APPOINTMENTSAVED.objects.get(id=id_no)
        print(make_this_appoint)
        print(make_this_appoint.app_mark)
        # if make_this_appoint.app_mark:#true in models
        if verify_status == 'marked':
            print("verified true")
            make_this_appoint.app_mark=False
            make_this_appoint.save()
            print(appoint_value)
    
        else:
            print("verified false")
            make_this_appoint.app_mark=True
            make_this_appoint.save()
    
            # verify_status = request.POST.get('virify_val')
            # print('................')
            # print(verify_status)
            # print('..............')
       
        # Do something when verify_status is 'marked'
        
            # if verify_status=='marked':
            # print("verifyed true")
            # make_this_appoint.app_mark=False
            # make_this_appoint.save()
            # else:
            
                

        
            
    doctor_appointments=APPOINTMENTSAVED.objects.filter(app_Appointed_doctor=doctorname)        
    context={
        "appointmentdetail" : doctor_appointments
    }
    return render(request, 'doctor_received_appoint.html', context)

def recievedappointments_mark(request):
    verify_user1=request.user.username
    doctorname=User.objects.get(username=verify_user1)
    appointmentdetail=APPOINTMENTSAVED.objects.filter(app_Appointed_doctor=doctorname)
    
    context={
        
        "appointmentdetail":appointmentdetail
        
    }
    return render(request,'doctor_received_appoint.html',context)

def login(request):
    if request.method == "POST":
        email = request.POST['log_email']
        password = request.POST['log_pass']
        print(email)
        if User.objects.filter(email=email).exists():
                
                
                #  Access the username
                username = User.objects.get(email=email)#get the usernameUser.objects.get(email=email).username
                print(User.objects.get(email=email))
                # print(username)
                auth_verified = auth.authenticate(username=username, password=password)
                print(auth_verified)
                if auth_verified is not None:
                    auth.login(request,auth_verified)#login=session or cookies
                    # return render(request, 'dashboard.html')
                    return redirect(dashboard)

                else:
                    context = {
                        'msg':'invalid email or password'
                    }
                    return render(request, 'login.html',context)
                    # context = {
                    #     'msg':'user already exists'
                    # }
                    # return render(request, 'index.html')
        else:
            context = {
                    'msg':'email doesnot  exists'
                }
            return render(request, 'login.html',context)
        
    return render(request,'login.html')
# def login_user(request):
#     # if request.user.is_authenticated:
#     #         # Access the username of the logged-in user
#     #     current_username = request.user.username
#     #     print(current_username)
#     #     print(request.user.email)
#     n=User.objects.get(username=request.user)
#     context = {
#         'val':n
#     }
#     return render(request, 'dashboard.html',context)
def dashboard(request):
    n=User.objects.get(username=request.user)
    context = {
        'val':n
    }
    return render(request, 'dashboard.html',context)
    
def register(request):
    if request.method=='POST':
        firstname = request.POST['reg_fname']
        lastname = request.POST['reg_lname']
        email = request.POST['reg_email']
        username=request.POST['uname']
        password = request.POST['reg_pass']
        c_password = request.POST['reg_cpas']
        if email==User.objects.filter(email=email).exists():
            context={
                'msg':"email already registered"
            }
            return render(request,'Register.html',context)
        else:
            if username==User.objects.filter(username=username).exists():
                context={
                    'msg':"Username already exist"
                }
                return render(request,'Register.html',context)
            else:
                if password==c_password:
                    newuser=User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password= password)
                    newuser.save()
                    return redirect(login)
    return render(request,'Register.html')
def about(request):
     return render(request,'about.html')
def contact(request):
     return render(request,'contact.html')
  #   send_mail(
    # "Subject here",
    # "Here is the message.",
    # "from@example.com",
    # ["to@example.com"],
    # fail_silently=False,)
def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        feedback_instance = Feeback(name=name, email=email, message=message)
        feedback_instance.save()

        
        send_mail(
                "feedback",
                feedback_instance.message,  
                "djangoemail0000@gmail.com",
                [feedback_instance.email],
                fail_silently=False,
            )

    return render(request,'feedback.html')
def patient(request):
   
       
    return render(request,'patient.html')

def updatepatient(request, id_no):
    print(id_no)
    patient = PatientTable.objects.filter(id=id_no) 

    if request.method == "POST":
        patient.patient_name = request.POST['hname']
        patient.patient_age = int(request.POST['hage'])
        patient.patient_gender = request.POST['hgender']
        patient.patient_phone = request.POST['hphone_no']
        patient.patient_address = request.POST['haddress']
        patient.patient_discription = request.POST['hdiscription']
        phonelength = len(request.POST['hphone_no'])
        if phonelength == 10:
            patient.save()
            return redirect('patient')  # Redirect to the 'patient' view
        else:
            context = {
                "msg": "enter a valid number",
                "patient_data": patient,
            }
            return render(request, "patient.html", context)

    context = {
        "patient_data": patient
    }
    return render(request, "patient.html", context)
def logout_view(request):
    auth.logout(request)
    # Redirect to a specific page after logout, such as the login page
    return redirect(login)

def reg_patient(request):
    if request.method=="POST":
        name=request.POST['name']
        age=int(request.POST["age"])
        gender=request.POST['gender']
        phone_number=request.POST['phone_no']
        address=request.POST['address']
        discription=request.POST['discription']
        phone_length=len(phone_number)
        if phone_length==10:
            if PatientTable.objects.filter(patient_phone=phone_number).exists():
                context={
                    "msg":"number already registered"
                }
                return render(request,"reg_patient.html",context)
            else:
                patient=PatientTable(patient_name=name,patient_age=age,patient_gender=gender,patient_phone=phone_number,patient_address=address,patient_discription=discription)
                patient.save()
                return redirect(reg_patient)
        else:
            context={
                "msg":"enter a valid number"
            }
            return render(request,"reg_patient.html",context)
                
    return render(request,"reg_patient.html")
def reg_view_patient(request):
    patients_all_data=PatientTable.objects.all()
    context={
        "all_data":patients_all_data
    }
    
    # query = request.POST.get('q', '')
    print("query_value:")
    # print(query)
    # print(query2)

    # query="patient1"
    if request.method=="POST":
        query=request.POST['search']
        # If there is a search query, filter the data based on it
        if query:
            print("hii query here")
            
            
            patients_all_data2 = patients_all_data.filter(
                Q(patient_name__icontains=query) |   # Case-insensitive name search athu case ayaalum value get cheyyum
                Q(patient_age__icontains=query) |
                Q(patient_gender__icontains=query) |
                Q(patient_address__icontains=query) |
                Q(patient_phone__icontains=query)
                
            )
            print("Filtered Data Count:", patients_all_data2.count())
            if not patients_all_data2:
                 context={
                    'msg':"No data found !!!!",
                    "all_data":patients_all_data
                }


            else:    
                context={
                    'all_data': patients_all_data,
                    'searched_data': patients_all_data2,
                }
                return render(request,"reg_view_patient.html",context)
        # else:
           

        #         context={
        #             'msg':"No data found !!!!",
        #             "all_data":patients_all_data
        #         }
        #     return render(request,"reg_view_patient.html",context)
    return render(request,"reg_view_patient.html",context)
def reg_update_patient(request,id_no):
    single_data=PatientTable.objects.get(id=id_no)
    context={
        "data":single_data
    }
    if request.method=="POST":
        single_data.patient_name=request.POST['hname']
        single_data.patient_age=int(request.POST["hage"])
        single_data.patient_gender=request.POST['hgender']
        single_data.patient_phone=request.POST['hphone_no']
        single_data.patient_address=request.POST['haddress']
        single_data.patient_discription=request.POST['hdiscription']
        phone_length=len(request.POST['hphone_no'])
        if phone_length==10:
           
            single_data.save()
            context={ 
                "msg":"Updated Successfully"
                     
                     }
            return render(request,'patient.html',context)
        else:
            context={ 
                "msg":"invalid number"
                     
                     }
            return render(request,'reg_update_patient.html',context)

    return render(request,"reg_update_patient.html",context)
def reg_update(request):
    patients_all_data=PatientTable.objects.all()
    context={
        "all_data":patients_all_data
    }
    
    return render(request,"reg_view_patient.html",context)

def medicine(request):
    return render(request,'medication.html')
def addmed(request):
    return render(request,'medicationadd.html')