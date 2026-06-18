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
    
    context={
        
             
        'msg':"Successfully appointment received"}
 
    return render(request,"demo_appoint_save.html",context)




def add_appoint(request,id_no,):
    selected_option = request.POST.get('select_patient', 'none')  # Adjust the name as per your form
    selected_option_values = selected_option.split(',')
    
    selected_option_id = selected_option_values[0]
    if id_no:
        id_detail=ADDSECTION.objects.get(id=id_no)
    
    option=PatientTable.objects.all()
    doctorname=id_detail.sec_doctor
    if request.method=='POST':
        selected_option = request.POST.get('select_patient', 'none')  # Adjust the name as per your form
        selected_option_values = selected_option.split(',')
        print(selected_option_values[0])
        selected_option_id = selected_option_values[0]
       

        if request.POST['search']:
            search_val = request.POST['search']
           
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
    depts=Department.objects.all()

    
    context={
        "saved_data":showdata,
        "appointmentdetail":appointmentdetail
        ,"departs":depts
        
    }
    if request.method=='POST':
        departments=request.POST['departments']
        op_no=int(request.POST['op_no'])
        dept=Department.objects.get(dept_name=departments)

        if op_no <= dept.dept_op_nos:
        # Allow the doctor to add an operation
           
            date = request.POST['date']
            duration1=request.POST['duration1']
            duration2=request.POST['duration2']
            departments=request.POST['departments']
            op_no=request.POST['op_no']
            break1=request.POST['break1']
            break2=request.POST['break2']
            verify_user=request.user.username
        else:
            context={'msg':"no of op exceded",
                     'total':dept.dept_op_nos,"departs":depts,"saved_data":showdata,
        "appointmentdetail":appointmentdetail}
            return render(request,'doctor_section.html',context)    
        
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



def recievedappointments(request,id_no):
    doctorname = request.user.username
    
    make_this_appoint=APPOINTMENTSAVED.objects.get(id=id_no)
    # appointed_status = request.GET.get('appoint_status', 'false').lower() == 'true'
    # print(request.GET)
    
    if request.method == 'POST':
        priscription=request.POST.get('priscription',None)
        print("priscirption")
        print(priscription)
        if priscription:
            make_this_appoint.app_doctor_priscription = priscription
            make_this_appoint.save()
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

        message = "THANKS FOR THE FEEDBACK"
        send_mail(
                "feedback",
                message,  
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

def addmed(request):
    if request.method=="POST":
        medicine_id=request.POST.get("medicine_id",None)
        generic_name=request.POST.get("generic_name",None)
        category=request.POST.get("category",None)
        desc1=request.POST.get("desc1",None)
        desc2=request.POST.get("desc2",None)
        expiry_date=request.POST.get("expiry_date",None)
        price=request.POST.get("price",None)
        use=request.POST.get("use",None)
        Quantity=request.POST.get("Quantity",None)
       
        medsave=MedicineList(medicine_id=medicine_id,generic_name=generic_name,category=category,desc1=desc1,desc2=desc2,exp_date=expiry_date,price=price,use=use,Quantity=Quantity)
        medsave.save()
    medsaved=MedicineList.objects.all()
    context={
        'meddetails':medsaved
    }
    return render(request,'medicationadd.html',context)
def prints(request,id_no):
    return render(request,"print.html")
def medicine(request):
    appoint_patients=APPOINTMENTSAVED.objects.filter(app_mark=True)
   
    pharmacy_detail=MedicineList.objects.all()
    patientlists=request.POST.get("patientlist",None)
       
    
    if request.method=="POST":
        patientlists=request.POST.get("patientlist",None)
       
       
        try:
            med_info = APPOINTMENTSAVED.objects.get(id=patientlists)
        except APPOINTMENTSAVED.DoesNotExist:
            print("errorfound")
    
        print(patientlists)
        
        
        print(patientlists)
        context={
           'appointsaved':appoint_patients,
           'meddetails':pharmacy_detail,'selected':med_info
        }
        return render(request,'medication.html',context)
    context={'appointsaved':appoint_patients,'meddetails':pharmacy_detail}

    return render(request,'medication.html',context)


def med2(request,id_no):
        print(id_no)
        appoint_patients=APPOINTMENTSAVED.objects.filter(app_mark=True)

        med_info = APPOINTMENTSAVED.objects.get(id=id_no)
        if request.method=='GET':
            print("getting")
            print(request.GET.get("generic_name",'None'))
            save_values=APPOINTMENTSAVED.objects.get(id=id_no)
            if request.GET.get("generic_name",None)!=None:
                print("nonenenennen")
                save_values.app_medicine=request.GET.get("generic_name",'None')
            if request.GET.get("frequency",None)!=None:
                save_values.app_frequency=request.GET.get("frequency",'')
            if request.GET.get("dosage",None)!=None:
                save_values.app_dosage=request.GET.get("dosage",'')
            if request.GET.get("route",None)!=None:    
                save_values.app_Route_0f_administration=request.GET.get("route",'')

            start_date= request.GET.get("start_date")

            if request.GET.get("start_date") is not None:
                save_values.app_enddate = start_date

            end_date=request.GET.get("end_date")
            if end_date is not None and end_date != "":
                save_values.app_enddate = end_date
            if request.GET.get("Priscription",None)!=None:    
                save_values.app_doctor_priscription=request.GET.get("Priscription")
            if request.GET.get("refills_remainging",None)!=None:    
                print("nonenenennen")
                save_values.app_refills_remaining=request.GET.get("refills_remainging",'None')
            
            save_values.save()
            return redirect('medicine')

        context={'selected':med_info,'appointsaved':appoint_patients,}
        return render(request,'medication.html',context)


# def medicine2(request):
#     appoint_patients=APPOINTMENTSAVED.objects.all()
   
#     pharmacy_detail=MedicineList.objects.all()
#     global patientlists
#     if request.method=="POST":
        
#         patientlists=request.POST.get("patientlist",None)
        
#         med_info=APPOINTMENTSAVED.objects.get(id=patientlists)
#         print(patientlists)
#         context={
#            'appointsaved':appoint_patients,
#            'selected':med_info,'meddetails':pharmacy_detail
#         }
#         return render(request,'medication.html',context)
#     context={'appointsaved':appoint_patients,'meddetails':pharmacy_detail}

#     return render(request,'medication.html',context)



def updatemed(request,id_no):
    global med_id
    med_single_data = MedicineList.objects.get(medicine_id=id_no)
    med_id=med_single_data.medicine_id
    medsaved=MedicineList.objects.all()
    print(id_no)
    if request.method=='POST':
        
            context={
        
            'meddetails':medsaved,
            "med_single_data":med_single_data,
            }
            med_single_data.save()
            return redirect(updatemed,id_no)
       
    context={
    
        'meddetails':medsaved,
        "med_single_data":med_single_data,
    }
    return render(request,'medicationadd.html',context)
def updatemed2(request,id_no):
    global med_id
    print("medid=",id_no)
    med_single_data = MedicineList.objects.get(medicine_id=med_id)
   
    
    print(request.GET.get("medicine_id",None))

    med_single_data.medicine_id=request.GET.get("medicine_id",None)
    print(request.POST.get("medicine_id",None))
    med_single_data.generic_name=request.GET.get("generic_name",None)
    med_single_data.category=request.GET.get("category",None)
    med_single_data.desc1=request.GET.get("desc1",None)
    med_single_data.desc2=request.GET.get("desc2",None)
    med_single_data.exp_date=request.GET.get("expiry_date",None)
    med_single_data.price=request.GET.get("price",None)
    med_single_data.use=request.GET.get("use",None)
    med_single_data.Quantity=request.GET.get("Quantity",None)
    med_single_data.save()
    context={"msg":"successfully updated"}
    # return render(request,'medicationadd.html',context)
    return render(request,'demo_updatemed.html',context)
    
def add_department(request):
    dept_head=Staffs.objects.filter(staff_role='DepartmentHead')
    if request.method=="POST":
        DeptName=request.POST.get('deptname',None)
        if Department.objects.filter(dept_name__iexact=DeptName).exists():
            context={'msg':'Department already exists'}
            return render(request,'add_department.html',context)
        else:    
            DeptName=request.POST.get('deptname',None)
            op_no=request.POST.get('op',None)
            head_of_dept=request.POST.get('head_of_dept',None)
            contact=request.POST.get('contact',None)
            discription=request.POST.get('discription',None)
            department=Department(dept_name=DeptName,dept_op_nos=op_no,dept_head_of_dept=head_of_dept,dept_contact=contact,dept_discription=discription)
            department.save()
       
       
        return redirect('department/')
    context={"dept_head":dept_head}
    return render(request,'add_department.html',context)
def department(request):
    
    alldata=Department.objects.all()
    context={'alldata':alldata}
   
    return render(request,'department.html',context)
def detailed_department(request,id_no):
    dept=Department.objects.get(id=id_no)
    dept_doc=dept.dept_name
    doctor=ADDSECTION.objects.filter(sec_department=dept_doc)

    context={'dept':dept,
             "doctor":doctor
             }
    return render(request,'detailed_department.html',context)

def pharmacy(request):
    meddetails=MedicineList.objects.all()
    pharmacy_detail=MedicineList.objects.all()
    if request.method=="POST":
        query=request.POST.get("search",None)
        pharmacy_detail2 = pharmacy_detail.filter(
                    Q(medicine_id__icontains=query) |   # Case-insensitive name search athu case ayaalum value get cheyyum
                    Q(generic_name__icontains=query) |
                    Q(category__icontains=query) |
                    Q(desc1__icontains=query) |
                    Q(desc2__icontains=query) |
                    Q(use__icontains=query)|
                    Q(price__icontains=query)|
                    Q(exp_date__icontains=query)
                    
                )
        context={"meddetails":meddetails,"searched":pharmacy_detail2}

        return render( request,'pharmacy.html',context)
    context={"meddetails":meddetails}
    return render( request,'pharmacy.html',context)

def med_delete(request,id_no):
    dele_val=MedicineList.objects.get(medicine_id=id_no)
    dele_val.delete()


    return redirect(pharmacy)
def sellmed(request,id_no):
    sell=MedicineList.objects.get(medicine_id=id_no)
    if sell.Quantity !=0:
        medprofit=profit(med_profit=sell.Quantity)
        sell.Quantity=sell.Quantity-1
        sell.save()
        medprofit.save()
        return redirect(pharmacy)
    else:
        context={"msg":"Medicine balance is 0"}
        return render(request,'demo_no_medicine.html',context)
    

def medication_details(request):
    alldetails=APPOINTMENTSAVED.objects.filter(app_mark=True)
    context={"alldetails":alldetails}



    return render(request,"medication_details.html",context)    


def staff(request):
    staff_details=Staffs.objects.all()
    context={"alldata":staff_details}
    return render(request,"staff.html",context)


def staff_add(request):
    if request.method=="POST":
        name = request.POST['name']
        age=request.POST['age']
        gender=request.POST['gender']
        role=request.POST['role']
        phone=request.POST['phone_no']
        address=request.POST['address']
        if len(phone)==10:

            if Staffs.objects.filter(staff_phone_no=phone).exists():
                context={"msg":"number already registered"}
                return render(request,"staff_add.html",context)
            else:
                save_data=Staffs(staff_name=name,staff_age=age,staff_gender=gender,staff_phone_no=phone,staff_role=role,staff_address=address)
                save_data.save()

        else:        
            context={"msg":"enter valid number"}
            return render(request,"staff_add.html",context)
    
    return render(request,"staff_add.html")

def update_staff(request,id_no):
    staff_data=Staffs.objects.get(id=id_no)
    if request.method=="POST":
        phone=request.POST['phone_no']
        staff_data.staff_name = request.POST['name']
        staff_data.staff_age=request.POST['age']
        staff_data.staff_gender=request.POST['gender']
        staff_data.staff_role=request.POST['role']
        staff_data.staff_phone_no=request.POST['phone_no']
        staff_data.staff_address=request.POST['address']
        if len(phone)==10:
            
            
                staff_data.save()
                return redirect(staff)
        else:        
                context={"msg":"enter valid number"}
                return render(request,"staff_Update.html",context)
    context={"data":staff_data}
    return render(request,"staff_Update.html",context)

def payment(request):
  
   
    alldetails=APPOINTMENTSAVED.objects.filter(app_mark=True)
    
    if request.method=="POST":
        query=request.POST.get("search",None)
        pharmacy_detail2 = alldetails.filter(
                    Q(app_id__icontains=query) |
                       Q(id__icontains=query) |   # Case-insensitive name search athu case ayaalum value get cheyyum
                    Q(app_Name__icontains=query) |
                    Q(app_Appointed_doctor__icontains=query) |
                    Q(app_medicine__icontains=query) |
                    Q(app_department__icontains=query) |
                    Q(app_Route_0f_administration__icontains=query)|
                    Q(app_age__icontains=query)|
                    Q(app_gender__icontains=query)|
                    Q(app_discription__icontains=query)
                    
                )
        context={"alldetails":alldetails,"searched":pharmacy_detail2}

        return render( request,'payment.html',context)
    context={"alldetails":alldetails}
    return render(request,"payment.html",context)    


def bill(request,id_no):
    
    data=APPOINTMENTSAVED.objects.get(id=id_no)
    
    patient_detail=PatientTable.objects.get(id=data.app_id)
    if request.method=="POST":
        medicine_priscribed=request.POST['medicine_priscribed']
        medicine_dosage=request.POST['medicine_dosage']
        medicine_duration=request.POST['medicine_duration']
        appoint_given = request.POST.get('advice_given', '')
        fees =request.POST.get('fees', 0)
        print(appoint_given)
        data.app_medicine_priscribed=medicine_priscribed
        data.app_medicine_dosage=medicine_dosage
        data.app_medicine_duration=medicine_duration
        data.app_advice_given=appoint_given
        data.app_fee=fees

        data.save()
    context={"data":data,"patient_detail":patient_detail}
    return render( request,'prescription.html',context)


def delete_staff(request,id_no):
    staff_data=Staffs.objects.get(id=id_no)
    staff_data.delete()

    return render(request,"staff.html")

def dept_update(request,id_no):
  
    dept_head=Staffs.objects.filter(staff_role='DepartmentHead')
     
    dept_info=Department.objects.get(id=id_no)
    if request.method=='POST':
        contact=request.POST.get('contact',None)

    
        if len(contact)==10:
            dept_info.dept_name=request.POST.get('deptname',None)
            dept_info.dept_op_nos=request.POST.get('op',None)
            dept_info.dept_head_of_dept=request.POST.get('head_of_dept',None)
            dept_info.dept_contact=request.POST.get('contact',None)
            dept_info.dept_discription=request.POST.get('discription',None)
            dept_info.save()
            context1={
                "msg":"successfully Updated"
            }
            return render(request,"depart_update_re.html",context1)
        else:
            context={
                "msg":"enter valid number",
                 "dept_head":dept_head,
                "dept_info":dept_info,
            }
            return render(request,"update_department.html",context)

    context={
            "dept_head":dept_head,
            "dept_info":dept_info
                }
    return render(request,"update_department.html",context)

def dept_delete(request,id_no):
    dept_info=Department.objects.get(id=id_no)
    dept_info.delete()
    return redirect(department)

def Accounting(request):
    return render(request,"accounting.html")

def med_profit(request):
    med_detail=MedicineList.objects.all()
    # sum_result = MedicineList.objects.aggregate(total_sum=models.Sum('Quantity'))
    # sum=sum_result['total_sum']
    total_sum=profit.objects.aggregate(total_sum=models.Sum('med_profit'))
    total = total_sum['total_sum']
    total_price_list = [med_item.calculate_total_price() for med_item in med_detail] 
    sum_medicine=sum(total_price_list)
   
    context={"med_detail":med_detail,"sum_result":sum_medicine,"total_sum":total}
    return render(request,"med_profit.html",context)


def patient_profit(request):
    patient=APPOINTMENTSAVED.objects.all()
    total_sum=APPOINTMENTSAVED.objects.aggregate(total_sum=models.Sum('app_fee'))
    total = total_sum['total_sum']

    context={"patient":patient,"total":total}


    return render(request,"patient_profit.html",context)

def patient_card(request,id_no):
    appoint_box=PatientTable.objects.filter(id=id_no)

   
       
    context={
        'appointed_patient': appoint_box,
        
    }
    return render(request,"patient_card.html",context)

