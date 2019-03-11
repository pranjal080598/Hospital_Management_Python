from django.db import models
from django.urls import reverse
import uuid 
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


class Patient(models.Model):
    u_id=models.OneToOneField(User,on_delete=models.CASCADE)
    First_Name=models.CharField(max_length=40)
    Last_Name=models.CharField(max_length=40)
    Middle_Name=models.CharField(max_length=40)
    Address=models.CharField(max_length=200)
    Date_Of_Birth=models.DateField()
    Blood_Grp=models.CharField(max_length=8)
    Profile_pic= models.FileField(upload_to="profilepics/")

    def __str__(self):
        full_name=self.First_Name+self.Middle_Name+self.Last_Name
        # return self.First_Name
        return '{0} {1} {2} {3} {4} {5} {6}'.format(self.u_id,self.First_Name,self.Last_Name,self.Middle_Name,self.Address,self.Date_Of_Birth,self.Profile_pic)

    # def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        # return reverse('patient-detail', args=[str(self.id)])


class Doctor(models.Model):
    u_id=models.OneToOneField(User,on_delete=models.CASCADE)
    First_Name=models.CharField(max_length=40)
    Last_Name=models.CharField(max_length=40)
    Middle_Name=models.CharField(max_length=40)
    Address=models.CharField(max_length=200)
    Date_Of_Birth=models.DateField()
    Blood_Grp=models.CharField(max_length=8)
    Degree=models.CharField(max_length=100)
    Description=models.CharField(max_length=200)
    Profile_pic= models.FileField(upload_to="profilepics/")

    def __str__(self):
        full_name=self.First_Name+self.Middle_Name+self.Last_Name
        return self.First_Name

class Staff(models.Model):
    u_id=models.OneToOneField(User,on_delete=models.CASCADE)
    First_Name=models.CharField(max_length=40)
    Last_Name=models.CharField(max_length=40)
    Middle_Name=models.CharField(max_length=40)
    Address=models.CharField(max_length=200)
    Date_Of_Birth=models.DateField()
    Blood_Grp=models.CharField(max_length=8)
    Date_of_joining=models.DateField()
    Profile_pic= models.FileField(upload_to="profilepics/")

    def __str__(self):
        full_name=self.First_Name+self.Middle_Name+self.Last_Name
        # return self.First_Name
        return '{0} {1} {2} {3} {4} {5} {6}'.format(self.u_id,self.First_Name,self.Last_Name,self.Middle_Name,self.Address,self.Date_Of_Birth,self.Profile_pic)



class Timings(models.Model):
    Doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Contact_Time = models.TimeField()
    def __str__(self):
        return str(self.Contact_Time)


class Slots(models.Model):
    Doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Slot_Time = models.CharField(max_length=15)
    def __str__(self):
        return str(self.Slot_Time)


class Appointment(models.Model):
    u_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    Slot_Time=models.ForeignKey(Slots,on_delete=models.CASCADE)
    Date=models.DateField()
    Taken_time=models.TimeField()
    def __str__(self):
        tp=str(self.Date)
        ta=str(self.Slot_Time)
        return '{0} {1}'.format(tp,ta)
        return (tp,ta)


class CancelAppointments(models.Model):
    u_id=models.ForeignKey(User,on_delete=models.CASCADE)
    Doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    #Slot_Time=models.ForeignKey(Slots,on_delete=models.CASCADE)
    Date=models.DateField()
    # Taken_time=models.TimeField()
    def __str__(self):
        return '{0} {1} {2}'.format(self.u_id,self.Doctor_id,self.Date)

class medicine(models.Model):
    medicine_name=models.CharField(max_length=250)
    description=models.CharField(max_length=250)
    def __str__(self):
        return '{0}'.format(self.medicine_name)


class historydata(models.Model):
    u_id=models.CharField(max_length=100)
    Doctor_id=models.CharField(max_length=100,default="")
    date=models.DateField()
    Med_1=models.CharField(max_length=120)
    m1_days=models.CharField(max_length=100)
    m1_times_a_day=models.CharField(max_length=100)
    '''Med_2=models.ForeignKey(medicine,on_delete=models.CASCADE,related_name='m2')
    m2_days=models.CharField(max_length=100)
    m2_times_a_day=models.CharField(max_length=100)
    Med_3=models.ForeignKey(medicine,on_delete=models.CASCADE,related_name='m3')
    m3_days=models.CharField(max_length=100)
    m3_times_a_day=models.CharField(max_length=100)
    Med_4=models.ForeignKey(medicine,on_delete=models.CASCADE,related_name='m4')
    m4_days=models.CharField(max_length=100)
    m4_times_a_day=models.CharField(max_length=100)
    Med_5=models.ForeignKey(medicine,on_delete=models.CASCADE,related_name='m5')
    m5_days=models.CharField(max_length=100)
    m5_times_a_day=models.CharField(max_length=100)'''
    description=models.CharField(max_length=300)

    def __str__(self):
             return '{0} {1}'.format(self.date,self.Doctor_id)

    
        

# Create your models here.
'''class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


class Book(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because book can only have one author, but authors can have multiple books
    # Author as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')
    book_pic = models.FileField(upload_to="profilepics/")
    # ManyToManyField used because genre can contain many books. Books can cover many genres.
    # Genre class has already been defined so we can specify the object above.
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('book-detail', args=[str(self.id)])

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])


class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='a', help_text='Book availability')

    class Meta:
        ordering = ["due_back"]
        

    def __str__(self):
        """
        String for representing the Model object
        """
        return '{0} ({1})'.format(self.id,self.book.title)


class Author(models.Model):
    """
    Model representing an author.
    """
    id=models.CharField(max_length=12,primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        ordering = ["last_name","first_name"]
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('author-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        #return '{0}, {1}'.format(self.last_name,self.first_name)
        return '{0} {1} {2}'.format(self.last_name,self.first_name,str(self.id))
        #return (str(self.id))

    def __repr__(self):
    	return (str(self.id))
'''