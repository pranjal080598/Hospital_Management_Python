from django.contrib import admin
from .models import Patient,Doctor,Slots,Timings,Appointment,Staff,CancelAppointments,medicine,historydata
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here
# accounts.admin.py
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
	list_display=('u_id','Last_Name', 'First_Name', 'Middle_Name')


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
	list_display=('Last_Name', 'First_Name','Middle_Name','Degree')


@admin.register(Timings)
class TimingsAdmin(admin.ModelAdmin):
	list_display = ('Doctor_id','Contact_Time')

@admin.register(Slots)
class SlotsAdmin(admin.ModelAdmin):
	list_display = ('Doctor_id','Slot_Time')


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
	list_display = ('u_id','Doctor_id','Date','Slot_Time')

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
	list_display=('u_id','Last_Name', 'First_Name', 'Middle_Name','Date_of_joining')

@admin.register(CancelAppointments)
class CancelAppointmentAdmin(admin.ModelAdmin):
	list_display=('u_id','Doctor_id','Date')

@admin.register(medicine)
class medicineAdmin(admin.ModelAdmin):
	list_display=('medicine_name','description')
		

@admin.register(historydata)
class historydataAdmin(admin.ModelAdmin):
	list_display=('u_id','description')
# admin.site.register(Slots)
# admin.site.register(Timings)
# admin.site.register(Doctor)
# admin.site.register(Appointment)



'''@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')


@admin.register(BookInstance) 
class BookInstanceAdmin(admin.ModelAdmin):
    pass
'''