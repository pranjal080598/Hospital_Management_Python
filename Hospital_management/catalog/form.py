from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import User
from .models import Patient, Appointment,Slots,CancelAppointments
from django.contrib.auth.forms import UserCreationForm
from .models import historydata,medicine


class Appoint_med(forms.ModelForm):
    error_css_class='error'
    required_css_class='required'
    # Med_1 = forms.ModelChoiceField(medicine, required=True)
    # Med_1=forms.ModelChoiceField(queryset=medicine.objects.all())
    # Med_1=forms.CharField(required=True, widget=forms.Select(choices=[]))
    '''Med_2=forms.CharField(required=False, widget=forms.Select(choices=[]))
    Med_3=forms.CharField(required=False, widget=forms.Select(choices=[]))
    Med_4=forms.CharField(required=False, widget=forms.Select(choices=[]))
    Med_5=forms.CharField(required=False, widget=forms.Select(choices=[]))
    m1_days=forms.CharField(required=True, widget=forms.Select(choices=[]))
    m2_days=forms.CharField(required=False, widget=forms.Select(choices=[]))
    m3_days=forms.CharField(required=False, widget=forms.Select(choices=[]))
    m4_days=forms.CharField(required=False, widget=forms.Select(choices=[]))
    m5_days=forms.CharField(required=False, widget=forms.Select(choices=[]))
    m1_times_a_day=forms.CharField(required=True, widget=forms.Select(choices=[]))
    m2_times_a_day=forms.CharField(required=False, widget=forms.Select(choices=[]))
    m3_times_a_day=forms.CharField(required=False, widget=forms.Select(choices=[]))
    m4_times_a_day=forms.CharField(required=False, widget=forms.Select(choices=[]))
    m5_times_a_day=forms.CharField(required=False, widget=forms.Select(choices=[]))
    '''
    u_id=forms.CharField(required=True, widget=forms.Select(choices=[]))
    Med_1=forms.CharField(required=True, widget=forms.Select(choices=[]))
    class Meta:
        model=historydata
        fields = (
            'u_id',
            'Med_1',
            'm1_days',
            'm1_times_a_day',
            'description'
            )
    '''def __init__(self,*args,**kwargs):
        super(Appoint_med,self).__init__(*args,**kwargs)'''
        # Med_1=medicine.objects.all()

'''Med_2',
            'm2_days',
            'm2_times_a_day',
            'Med_3',
            'm3_days',
            'm3_times_a_day',
            'Med_4',
            'm4_days',
            'm4_times_a_day',
            'Med_5',
            'm5_days',
            'm5_times_a_day'''
class RegistrationForm(UserCreationForm,forms.ModelForm):
    error_css_class='error'
    required_css_class='required'
    '''First_Name=forms.CharField(max_length=40)
    Last_Name=forms.CharField(max_length=40)
    Middle_Name=forms.CharField(max_length=40)
    Address=forms.CharField(max_length=200)
    Date_Of_Birth=forms.DateField()
    Blood_Grp=forms.CharField(max_length=8)
    '''

    class Meta:
        model = User
        fields = ('username',
            'password1',
            'password2'
            )


class apointForm(forms.ModelForm):
    # doctor_name=forms.ChoiceField()
    doctor_name=forms.CharField(required=True, widget=forms.Select(choices=[]))
    slot=forms.CharField(required=True, widget=forms.Select(choices=[]))
    # slot=forms.ChoiceField()
    date =forms.DateField(required=False)

    class Meta:
        model=Appointment
        fields={'doctor_name','slot','date'}
            
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['slot'].queryset = Slots.objects.none()

        if 'slot' in self.data:
            try:
                slot_id = int(self.data.get('slot'))
                self.fields['slot'].queryset = Slots.objects.filter(id=slot_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['slot'].queryset = self.instance.doctor_name.slot_set.order_by('name')


class cancelForm(forms.ModelForm):
    # doctor_name=forms.ChoiceField()
    doctor_name=forms.CharField(required=True, widget=forms.Select(choices=[]))
    # slot=forms.ChoiceField()
    date=forms.DateField(required=False)

    class Meta:
        model=CancelAppointments
        fields={'doctor_name','date'}
            
    
class RegistrationForm2(forms.ModelForm):
    # u_id=RegistrationForm()
    First_Name=forms.CharField(max_length=40)
    Last_Name=forms.CharField(max_length=40)
    Middle_Name=forms.CharField(max_length=40)
    Address=forms.CharField(max_length=200)
    Date_Of_Birth=forms.DateField()
    Blood_Grp=forms.CharField(max_length=8)
    Profile_pic=forms.FileField()

    class Meta:
        model = Patient
        fields = ('First_Name','Last_Name','Middle_Name','Address','Date_Of_Birth','Blood_Grp','Profile_pic')    
