from django.shortcuts import render,redirect,get_object_or_404
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Patient,Slots,Doctor,Appointment,Staff,medicine,historydata
from django.contrib.auth.decorators import login_required
from .form import RegistrationForm,RegistrationForm2,apointForm, cancelForm,Appoint_med
from django.contrib.auth.models import User as User
import datetime
import time
from django.contrib import messages
import operator



def tests(request):
    return render(
            request,
            'test.html',
        )


@login_required
def givemed(request):
    # List=['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']
    List=[]
    username=request.user
    print(username.id)
    doctor=Doctor.objects.filter(u_id=username.id)
    u=Patient.objects.filter(u_id=username.id)
    print(doctor)
    print(u)
    print(username.id)
    current_date=datetime.datetime.now().date()
    print(current_date)
    Doctor_logged_in=Doctor.objects.none()
    Patient_logged_in=Patient.objects.none()
    if u:
        return redirect('/home/')
        Patient_logged_in=u
        print("Logged In user is Patient")
    if doctor:
        Doctor_logged_in=doctor
        print("Logged In User Is Doctor")
        print(Doctor_logged_in)
    print(Patient_logged_in)
    apoint_form=Appoint_med()
    print(apoint_form)
    d=medicine.objects.none()
    a=Appointment.objects.all()
    us=User.objects.all()
    # print("Doctors Id",doctor[0].id)
    today_apoint=Appointment.objects.filter(Date=current_date).filter(Doctor_id=doctor[0].id)
    print("Todays Apoint",today_apoint)
    i=0
    for tds in today_apoint:
        print(tds.u_id)
        u=User.objects.filter(id=tds.u_id.id)
        List.append(u)
        i=i+1
    print("List Is",List)
    print(List[0])
    if request.method == 'POST':
        apoint_form1 =Appoint_med(request.POST)
        # print(apoint_form1)
        # print(apoint_form1)
        uid=request.POST['u_id']
        m=request.POST['Med_1']
        print(m)
        print(uid)
        # user1.Doctor_id_id=Doctor.objects.filter(First_Name=value).values('id')[0]['id']
        print(apoint_form1)
        # print(apoint_form)
        if apoint_form1.is_valid():
            u=apoint_form1.save(commit=False)
            uuid=User.objects.filter(username=uid)
            print(uuid)
            # print(apoint_form1.Med_1)
            # user1.Doctor_id_id=Doctor.objects.filter(First_Name=value).values('id')[0]['id'] 
            print(request.user.id)
            u.Doctor_id=request.user
            u.date=current_date
            print(u.Doctor_id)
            # apoint_form1.description=" "
            print("Registered")
            u.save()
        else:
            print(" Not Registered Invalid")
    d=medicine.objects.all()
    return render(
        request,
        'givemedicine.html',
        context={'user':today_apoint,'Appoint_med':apoint_form,'medicine':d,'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in}
    )


def history(request):
    username=request.user
    print(username.id)
    d=Doctor.objects.filter(u_id=username.id)
    u=Patient.objects.filter(u_id=username.id)
    print(d)
    print(u)
    print(username.id)
    Doctor_logged_in=Doctor.objects.none()
    Patient_logged_in=Patient.objects.none()
    if u:
        Patient_logged_in=u
        print("Logged In user is Patient")
    if d:
        return redirect('/home/')
        Doctor_logged_in=d
        print("Logged In User Is Doctor")
    print(Patient_logged_in)
    logu=request.user
    App=historydata.objects.filter(u_id=logu).order_by('-date')
    print(App)
    if request.method=='POST':
                value=request.POST['date']
                value2=request.POST['doctor_name']
                print(value2)
                print(value)
                if value and request.POST['doctor_name']==" ":
                    print("Inside Date")
                    value=request.POST['date']
                    print(value)
                    App=historydata.objects.filter(u_id=logu).filter(date=value).distinct()
                elif not value and request.POST['doctor_name']!= " ":
                    print("Inside Doctors")
                    value2=request.POST['doctor_name']
                    App=historydata.objects.filter(u_id=logu).filter(Doctor_id=value2).distinct().order_by('-date')
                elif request.POST['doctor_name']!=" " and value:
                    print("Inside BOth")
                    App=historydata.objects.filter(u_id=logu).filter(Doctor_id=value2).filter(date=value)
    # App=sorted(auths,key=operator.attrgetter('date'))
    print(App)
    doctors=Doctor.objects.all()
    return render(
            request,
            'history.html',
            context={'App':App,'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in,'doctors':doctors}
        )



def myappoint(request):
    username=request.user
    print(username.id)
    d=Doctor.objects.filter(u_id=username.id)
    u=Patient.objects.filter(u_id=username.id)
    print(d)
    print(u)
    print(username.id)
    Doctor_logged_in=Doctor.objects.none()
    Patient_logged_in=Patient.objects.none()
    if u:
        Patient_logged_in=u
        print("Logged In user is Patient")
    if d:
        return redirect('/home/')
        Doctor_logged_in=d
        print("Logged In User Is Doctor")
    print(Patient_logged_in)
    logu=request.user
    doctors=Doctor.objects.all()
    App=Appointment.objects.filter(u_id=logu).order_by('-Date')
    print(App)
    if request.method=='POST':
                value=request.POST['date']
                value2=request.POST['doctor_name']
                print(value2)
                print(value)
                if value and request.POST['doctor_name']==" ":
                    print("Inside Date")
                    value=request.POST['date']
                    print(value)
                    App=Appointment.objects.filter(u_id=logu).filter(Date=value).distinct()
                    return render(
                                        request,
                                        'myappoint.html',
                                        context={'App':App,'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in,'doctors':doctors}
                                    )
                elif not value and request.POST['doctor_name']!= " ":
                    print("Inside Doctors")
                    value2=request.POST['doctor_name']
                    us=User.objects.filter(username=value2)
                    App=Appointment.objects.filter(u_id=logu).filter(Doctor_id=us[0].id).distinct().order_by('-date')
                    return render(
                                    request,
                                    'myappoint.html',
                                    context={'App':App,'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in,'doctors':doctors}
                                )
                elif request.POST['doctor_name']!=" " and value:
                    print("Inside BOth")
                    value2=request.POST['doctor_name']
                    us=User.objects.filter(username=value2)
                    App=Appointment.objects.filter(u_id=logu).filter(Doctor_id=us[0].id).filter(Date=value)
                    return render(
                                    request,
                                    'myappoint.html',
                                    context={'App':App,'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in,'doctors':doctors}
                                )
    # App=sorted(auths,key=operator.attrgetter('date'))
    print(App)
    doctors=Doctor.objects.all()
    return render(
            request,
            'myappoint.html',
            context={'App':App,'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in,'doctors':doctors}
        )



def main_home(request):
    return render(
            request,
            'indexnew.html',
        )

@login_required
def home(request):
    username=request.user
    print(username.id)
    d=Doctor.objects.filter(u_id=username.id)
    u=Patient.objects.filter(u_id=username.id)
    print(d)
    print(u)
    print(username.id)
    Doctor_logged_in=Doctor.objects.none()
    Patient_logged_in=Patient.objects.none()
    if u:
        Patient_logged_in=u
        print("Logged In user is Patient")
    if d:
        Doctor_logged_in=d
        print("Logged In User Is Doctor")
    print(Patient_logged_in)
    return render(
            request,
            'home.html',
            context={'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in}
        )

@login_required
def service(request):
    username=request.user
    print(username.id)
    d=Doctor.objects.filter(u_id=username.id)
    u=Patient.objects.filter(u_id=username.id)
    print(d)
    print(u)
    print(username.id)
    Doctor_logged_in=Doctor.objects.none()
    Patient_logged_in=Patient.objects.none()
    if u:
        Patient_logged_in=u
        print("Logged In user is Patient")
    if d:
        Doctor_logged_in=d
        print("Logged In User Is Doctor")
    return render(
            request,
            'services.html',
            context={'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in}
        )

@login_required
def contactus(request):
    username=request.user
    print(username.id)
    d=Doctor.objects.filter(u_id=username.id)
    u=Patient.objects.filter(u_id=username.id)
    print(d)
    print(u)
    print(username.id)
    Doctor_logged_in=Doctor.objects.none()
    Patient_logged_in=Patient.objects.none()
    if u:
        Patient_logged_in=u
        print("Logged In user is Patient")
    if d:
        Doctor_logged_in=d
        print("Logged In User Is Doctor")
    return render(
            request,
            'contactus.html',
            context={'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in}
        )

@login_required
def team(request):
    username=request.user
    print(username.id)
    d=Doctor.objects.filter(u_id=username.id)
    u=Patient.objects.filter(u_id=username.id)
    print(d)
    print(u)
    print(username.id)
    Doctor_logged_in=Doctor.objects.none()
    Patient_logged_in=Patient.objects.none()
    if u:
        Patient_logged_in=u
        print("Logged In user is Patient")
    if d:
        Doctor_logged_in=d
        print("Logged In User Is Doctor")
    return render(
            request,
            'team.html',
            context={'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in}
        )

@login_required
def aboutus(request):
    username=request.user
    print(username.id)
    d=Doctor.objects.filter(u_id=username.id)
    u=Patient.objects.filter(u_id=username.id)
    print(d)
    print(u)
    print(username.id)
    Doctor_logged_in=Doctor.objects.none()
    Patient_logged_in=Patient.objects.none()
    if u:
        Patient_logged_in=u
        print("Logged In user is Patient")
    if d:
        Doctor_logged_in=d
        print("Logged In User Is Doctor")
    return render(
            request,
            'aboutus.html',
            context={'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in}
        )

def index(request):
    a=15
    username=request.user
    print(username.id)
    d=Doctor.objects.filter(u_id=username.id)
    u=Patient.objects.filter(u_id=username.id)
    print(d)
    print(u)
    print(username.id)
    Doctor_logged_in=Doctor.objects.none()
    Patient_logged_in=Patient.objects.none()
    if u:
        Patient_logged_in=u
        print("Logged In user is Patient")
    if d:
        Doctor_logged_in=d
        print("Logged In User Is Doctor")
    return render(
            request,
            'base_new.html',
            context={'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in}
        )

@login_required
def patientdetail(request,pk):
    username=request.user
    print(username.id)
    d=Doctor.objects.filter(u_id=username.id)
    u=Patient.objects.filter(u_id=username.id)
    s=Staff.objects.filter(u_id=username.id)
    print(d)
    print(u)
    print(username.id)
    Doctor_logged_in=Doctor.objects.none()
    Patient_logged_in=Patient.objects.none()
    if u:
        return redirect('/home/')
        Patient_logged_in=u
        print("Logged In user is Patient")
    if d:
        Doctor_logged_in=d
        print("Logged In User Is Doctor")
    detail=Patient.objects.all()
    for dt in detail:
        print("In temp",dt.u_id.id)
        print("In Name",dt.u_id)
        print("Normal D",dt.id)
    # post = get_object_or_404(Patient, pk=pk)
    # print("Post Id IS ",post.id)
    a=str(pk)
    print(a)
    Patient_list = Patient.objects.filter(u_id=pk)
    return render(request,'patientdetail.html',context={'Patient_logged_in':Patient_logged_in,'Doctor_logged_in':Doctor_logged_in,'Patient_dict':Patient_list})

@login_required
def viewapoint(request):
    a=0
    # value=request.POST['doctor_name']
    MiddleName=[]
    LastName=[]
    FirstName=[]
    allpatientdetail=Patient.objects.none()
    username=request.user
    print(username.id)
    d=Doctor.objects.filter(u_id=username.id)
    u=Patient.objects.filter(u_id=username.id)
    s=Staff.objects.filter(u_id=username.id)
    print(d)
    print(u)
    print(username.id)
    Doctor_logged_in=Doctor.objects.none()
    Patient_logged_in=Patient.objects.none()
    if u:
        return redirect('/home/')
        print("Logged In user is Patient")
    if d:
        Doctor_logged_in=d
        print("Logged In User Is Doctor")
        current_date=datetime.datetime.now().date()
        print(current_date)
        allapoint=Appointment.objects.filter(Date=current_date).filter(Doctor_id=Doctor_logged_in[0])
        print(allapoint)
        print(current_date)
        for apoint in allapoint:
            patientdetail=Patient.objects.filter(u_id=apoint.u_id)
            # allpatientdetail.append(patientdetail)
            # stories = django_stories | vitor_stories  # merge querysets
            allpatientdetail=allpatientdetail | patientdetail
            print("At 0",patientdetail[0].Middle_Name)
            FirstName.append(patientdetail[0].First_Name)
            MiddleName.append(patientdetail[0].Middle_Name)
            LastName.append(patientdetail[0].Last_Name)
            print("At allpatientdetail 0",allpatientdetail[0].Middle_Name)
            print(apoint.u_id)
        print(allpatientdetail)
        print(allapoint)
        if request.method=='POST':
            value=request.POST['date']
            print(value)
            allapoint=Appointment.objects.filter(Date=value).filter(Doctor_id=Doctor_logged_in[0])
            for apoint in allapoint:
                patientdetail=Patient.objects.filter(u_id=apoint.u_id)
                # allpatientdetail.append(patientdetail)
                # stories = django_stories | vitor_stories  # merge querysets
                allpatientdetail=allpatientdetail | patientdetail
                print("At 0",patientdetail[0].Middle_Name)
                FirstName.append(patientdetail[0].First_Name)
                MiddleName.append(patientdetail[0].Middle_Name)
                LastName.append(patientdetail[0].Last_Name)
                print("At allpatientdetail 0",allpatientdetail[0].Middle_Name)
                print(apoint.u_id)
            print(allpatientdetail)
            print(allapoint)
        doctors=Doctor.objects.all()
        return render(
                    request,
                    'viewapoint.html',
                    context={'doctors':doctors,'FirstName':FirstName,'MiddleName':MiddleName,'LastName':LastName,'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in,'allapoint':allapoint,'allpatientdetail':allpatientdetail}
                )
    if s:
            Staff_logged_in=d
            current_date=datetime.datetime.now().date()
            print(current_date)
            allapoint=Appointment.objects.filter(Date=current_date)
            for apoint in allapoint:
                patientdetail=Patient.objects.filter(u_id=apoint.u_id)
                # allpatientdetail.append(patientdetail)
                # stories = django_stories | vitor_stories  # merge querysets
                allpatientdetail=allpatientdetail | patientdetail
                print("At 0",patientdetail[0].Middle_Name)
                FirstName.append(patientdetail[0].First_Name)
                MiddleName.append(patientdetail[0].Middle_Name)
                LastName.append(patientdetail[0].Last_Name)
                print("At allpatientdetail 0",allpatientdetail[0].Middle_Name)
                print(apoint.u_id)
            print(allpatientdetail)
            print(allapoint)
            if request.method=='POST':
                value=request.POST['date']
                print(value)
                if request.POST['doctor_name']==" ":
                    value=request.POST['date']
                    print(value)
                    allapoint=Appointment.objects.filter(Date=value)
                    for apoint in allapoint:
                        patientdetail=Patient.objects.filter(u_id=apoint.u_id)
                        # allpatientdetail.append(patientdetail)
                        # stories = django_stories | vitor_stories  # merge querysets
                        allpatientdetail=allpatientdetail | patientdetail
                        print("At 0",patientdetail[0].Middle_Name)
                        FirstName.append(patientdetail[0].First_Name)
                        MiddleName.append(patientdetail[0].Middle_Name)
                        LastName.append(patientdetail[0].Last_Name)
                        print("At allpatientdetail 0",allpatientdetail[0].Middle_Name)
                        print(apoint.u_id)
                elif not value and request.POST['doctor_name']!= " ":
                    pass
                elif request.POST['doctor_name']!=" " and value:
                    value=request.POST['date']
                    print(value)
                    value2=request.POST['doctor_name']
                    print(value2)
                    doctor=Doctor.objects.filter(First_Name=value2)
                    allapoint=Appointment.objects.filter(Date=value).filter(Doctor_id=doctor[0].id)
                    print(current_date)
                    for apoint in allapoint:
                        patientdetail=Patient.objects.filter(u_id=apoint.u_id)
                        # allpatientdetail.append(patientdetail)
                        # stories = django_stories | vitor_stories  # merge querysets
                        allpatientdetail=allpatientdetail | patientdetail
                        print("At 0",patientdetail[0].Middle_Name)
                        FirstName.append(patientdetail[0].First_Name)
                        MiddleName.append(patientdetail[0].Middle_Name)
                        LastName.append(patientdetail[0].Last_Name)
                        print("At allpatientdetail 0",allpatientdetail[0].Middle_Name)
                        print(apoint.u_id)
                print(allpatientdetail)
                print(allapoint)
            doctors=Doctor.objects.all()
            return render(
                    request,
                    'viewapoint.html',
                    context={'doctors':doctors,'FirstName':FirstName,'MiddleName':MiddleName,'LastName':LastName,'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in,'allapoint':allapoint,'allpatientdetail':allpatientdetail}
                )

@login_required
def takeapoint(request):
    username=request.user
    print(username.id)
    d=Doctor.objects.filter(u_id=username.id)
    u=Patient.objects.filter(u_id=username.id)
    s=Staff.objects.filter(u_id=username.id)
    print(d)
    print(u)
    print(username.id)
    Doctor_logged_in=Doctor.objects.none()
    Patient_logged_in=Patient.objects.none()
    Staff_logged_in=Staff.objects.none()
    if s:
        Staff_logged_in=d
    if u:
        Patient_logged_in=u
        print("Logged In user is Patient")
    if d:
        return redirect('/home/')
        Doctor_logged_in=d
        print("Logged In User Is Doctor")
    registered=False
    apoint=apointForm()
    slots=Slots.objects.none()
    doctors=Doctor.objects.all()
    slots_time=Slots.objects.none()
    if request.method == 'POST':
        apoint_form =apointForm(request.POST)
        print(apoint_form)
        print("Before Validaion")
        dt=(request.POST['slot'])
        print("Value Taken=",dt)
        # apoint_form.Slot_Time_id=Slots.objects.filter(Slot_Time=dt).values('id')[0]['id'] 
        if (apoint_form.is_valid()):
            print("Validated")
            #return HttpResponse("HELOOOOOOOOOOOOO")
            user1=apoint_form.save(commit=False)
            value=request.POST['doctor_name']
            value2=(request.POST['slot'])
            value3=request.POST['date']
            current_date=datetime.datetime.now().date()
            if value3<(str)(current_date) and value3:
                messages.warning(request, 'Invalid Date. Please Select Appropraite Date!!!!!!!')
                return render(
                            request,
                            'apoint.html',
                            context={'Staff_logged_in':Staff_logged_in,'slots_time':slots_time,'apoint':apoint,'doctors':doctors,'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in}
                             )     
            doc=Doctor.objects.filter(First_Name=value).values('id')[0]['id'] 
            uid=request.user 
            app=Appointment.objects.filter(Doctor_id=doc).filter(Date=value3).filter(u_id=uid.id)
            if(app):
                messages.warning(request, 'You Already Have An Appointment For That Date Please Cancel That Appointment To Take Another!!!!!!!')
                return render(
                            request,
                            'apoint.html',
                            context={'Staff_logged_in':Staff_logged_in,'slots_time':slots_time,'apoint':apoint,'doctors':doctors,'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in}
                             )  
            print(app)  
            user1.Date=value3
            user1.Doctor_id_id=Doctor.objects.filter(First_Name=value).values('id')[0]['id'] 
            user1.Slot_Time_id=Slots.objects.filter(Slot_Time=dt).values('id')[0]['id'] 
            user1.u_id=User.objects.get(username=request.user.get_username())
            user1.Taken_time=datetime.datetime.now().time()
            #user_form.set_password(user.password)
            print("HELOOOOOOOOOOOOO")
            user1.save()
            registered = True
            messages.success(request, 'Your Appointment Has Been Taken Successfully!!!!!!!')
        else:   
             print(" NOt Validated")

    else:
        print("Not Validated")
        apoint=apointForm()
        slots=Slots.objects.none()
        doctors=Doctor.objects.all()
        slots_time=Slots.objects.none()
        # user_form = RegistrationForm()
    if registered:
         return redirect ('/takeapoint/')
         #return reverse ('home:base')
    else:
        return render(
            request,
            'apoint.html',
            context={'Staff_logged_in':Staff_logged_in,'slots_time':slots_time,'apoint':apoint,'doctors':doctors,'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in}
    )


@login_required
def cancelapoint(request):
    # messages=" "
    username=request.user
    print(username.id)
    d=Doctor.objects.filter(u_id=username.id)
    u=Patient.objects.filter(u_id=username.id)
    print(d)
    print(u)
    print(username.id)
    Doctor_logged_in=Doctor.objects.none()
    Patient_logged_in=Patient.objects.none()
    if u:
        Patient_logged_in=u
        print("Logged In user is Patient")
    if d:
        return redirect('/home/')
        Doctor_logged_in=d
        print("Logged In User Is Doctor")
    

    registered=False
    print(cancelForm)
    cancelapoint=cancelForm()
    doctors=Doctor.objects.all()
    if request.method == 'POST':
        cancel_form =cancelForm(request.POST)
        print("Cancel Form Data",cancel_form)
        print("Before Validaion")
        if (cancel_form.is_valid()):
            print("Validated")
            #return HttpResponse("HELOOOOOOOOOOOOO")
            user1=cancel_form.save(commit=False)
            value=request.POST['doctor_name']
            value3=request.POST['date']
            current_date=datetime.datetime.now().date()
            if value3<(str)(current_date):
                messages.warning(request, 'Invalid Date. Please Select Appropraite Date!!!!!!!')
                return render(
                            request,
                            'cancelapoint.html',
                            context={'apoint':cancelapoint,'doctors':doctors,'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in}
    )                       
            user1.Date=value3
            user1.Doctor_id_id=Doctor.objects.filter(First_Name=value).values('id')[0]['id'] 
            user1.u_id=User.objects.get(username=request.user.get_username())
            Cancel_apoint_d=Appointment.objects.filter(u_id=user1.u_id,Doctor_id=user1.Doctor_id_id,Date=user1.Date)
            if not Cancel_apoint_d:
                print("Not Deleted")
                messages.warning(request, 'Sorry!!!!! You Dont Have Any Appointment Please Enter Proper Details')
            else:
                print("Cancel Apooint Entry",Cancel_apoint_d)
                Cancel_apoint_d.delete()
                messages.success(request, 'Your Appointment Has Been Cancelled')
                # messages.info(request, 'Your Appointment Has Been Cancelled')
                print("Delete Successfully")
            # user1.Taken_time=datetime.datetime.now().time()
            #user1.Taken_time=datetime.datetime.now().time()
            #user_form.set_password(user.password)
            print("HELOOOOOOOOOOOOO")
            user1.save()
            registered = True
           
        else:
             print(" NOt Validated")
    else:
        print("Not Validated")
        cancelapoint=cancelForm()
        print(cancelapoint)
        doctors=Doctor.objects.all()
    if registered:
         return redirect ('/cancelapoint/')
    else:
        return render(
            request,
            'cancelapoint.html',
            context={'apoint':cancelapoint,'doctors':doctors,'Doctor_logged_in':Doctor_logged_in,'Patient_logged_in':Patient_logged_in}
    )

def book(request,pk):
    post = get_object_or_404(Book, pk=pk)
    print(post.id)
    ans_list = Book.objects.filter(id=post.id)
    return render(request,'bookdetial.html',context={'ans_dict':ans_list})

def author(request,pk):
    post = get_object_or_404(Author, first_name=pk)
    print(post)
    ans_list = Author.objects.filter(first_name=post.first_name)
    return render(request,'author.html',context={'ans_dict':ans_list})


def register(request):
    p=Patient.objects.all()
    # print(p[0].u_id)
    registered = False
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        user_form2 = RegistrationForm2(request.POST,request.FILES)
        print(user_form2)
        print("Before Validaion")
        if (user_form.is_valid() and user_form2.is_valid()):
            print("Validated")
            #return HttpResponse("HELOOOOOOOOOOOOO")
            user=user_form.save()
            print(user)
            print(user.id)
            print(user.username)
            user2=user_form2.save(commit =False)
            user2.u_id=user
            #user_form.set_password(user.password)
            print("HELOOOOOOOOOOOOO")
            '''username = user_form.get('username')
            raw_password = user_form.get('password')
            print(username)
            user.first_name=user_form.get('first_name')
            user.last_name=user_form.get('last_name')
            user.email=user_form.get('email')'''
            '''user.first_name=request.POST.get('first_name')
            user.last_name=request.POST.get('last_name')
            user.email=request.POST.get('email')'''
            user.save()
            user2.save()
            #login(request, authenticate(username=username, password=raw_password))
            registered = True
            print(user_form['username'])

    else:
        print("Not Validated")
        user_form = RegistrationForm()
        user_form2 = RegistrationForm2()
    if registered:
        #return HttpResponse("Logged In")
         #redirect_to = settings.LOGIN_REDIRECT_URL
         messages.success(request, 'Your Appointment Has Been Registered Successfully!!!!!!!')
         return redirect ('/login/')
         #return reverse ('home:base')
    else:
        return render(request, 'register.html', {'user_form': user_form,'user_form2':user_form2})



@login_required
def load_slots(request):
    i=0
    doctor_id = request.GET.get('doctor_name')
    date = request.GET.get('date')
    print(date)
    print(doctor_id)
    if(doctor_id!=' 'and date!=' '):
        slot=[]
        slot1=[]
        print("Slots Found")
        doctor=Doctor.objects.filter(First_Name=doctor_id).values('id')[0]['id']    
        slots=Slots.objects.filter(Doctor_id=doctor)
        print(slots)
        for s1 in slots:
            # print(s1)
            slot_id=Slots.objects.filter(Doctor_id=doctor).values('id')[i]['id']
            i=i+1
            print("i=",i)
            print("SLots Id",slot_id)
            appoint=Appointment.objects.filter(Doctor_id=doctor,Slot_Time=slot_id,Date=date)
            print("Appointment",appoint)
            if len(appoint) == 0:
                slot.append(s1)
                print("IN if ",slot)
            else:
                continue
        print("SLots",slot)
        print("Doctor Id",doctor_id)
       
    else:
        print("Slots Not Found")
        slots=Slots.objects.none()
    return render(request, 'slots_dropdown_list_option.html', {'slots': slot})



@login_required
def load_finalslots(request):
    i=0
    doctor_id = request.GET.get('doctor_name')
    date = request.GET.get('date')
    print(date)
    print(doctor_id)
    if(doctor_id!=' 'and date!=' '):
        slot=[]
        slot1=[]
        print("Slots Found")
        doctor=Doctor.objects.filter(First_Name=doctor_id).values('id')[0]['id']    
        slots=Slots.objects.filter(Doctor_id=doctor)
        print(slots)
        for s1 in slots:
            # print(s1)
            slot_id=Slots.objects.filter(Doctor_id=doctor).values('id')[i]['id']
            i=i+1
            print("i=",i)
            print("SLots Id",slot_id)
            appoint=Appointment.objects.filter(Doctor_id=doctor,Slot_Time=slot_id,Date=date)
            print("Appointment",appoint)
            if len(appoint) == 0:
                slot.append(s1)
                print("IN if ",slot)
            else:
                continue
        print("SLots",slot)
        print("Doctor Id",doctor_id)
       
    else:
        print("Slots Not Found")
        slots=Slots.objects.none()
    return render(request, 'slots_dropdown_list_option.html', {'slots': slot})




'''
Error Time 
# value2.datetime.strptimestrftime('%H:%M:%S')
            # datetime.datetime.strptime(value2, '%H:%M p.m.').time()
            # dt = time.strptime(value2, "%H:%M p.m.")
            # print("DT++",dt)
            # ft=dt.tm_hour+dt.tm_min
            # print(ft)
            # value2.strftime('%H:%M:%S')
            # value2.time()


def bookdetail(request,pk):
    return HttpResponse("HELLO WORLD")
    post = get_object_or_404(Author, pk=pk)
    print(post.id)
    ans_list = Author.objects.filter(id=post.id)
    return render(request,'bookdetial.html',context={'ans_dict':ans_list})

 # Create your views here.
def show(request):
    return HttpResponse('HELLO')
'''