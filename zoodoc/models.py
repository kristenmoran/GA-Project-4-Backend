from django.db import models

<<<<<<< HEAD
<<<<<<< HEAD
# Create your models here.
=======
=======
>>>>>>> 4bbd0be2d2db4b4d1ca72ad44ddea8aecd540258
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User
# Create your models here.


class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=25)
    specialization = ArrayField(models.CharField(
        max_length=100), null=True, blank=True)
    languages = ArrayField(models.CharField(
        max_length=50), null=True, blank=True)
    about = models.TextField()
    practicing_from = models.CharField(max_length=50)
    image_url = models.TextField()

    def __str__(self):
        return self.first_name


class Qualification(models.Model):
    qualification_name = models.CharField(max_length=100)
    institute_name = models.CharField(max_length=100)
    procurement_year = models.CharField(max_length=100)
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='qualifications')

    def __str__(self):
        return self.qualification_name


class Office_Location(models.Model):
    office_name = models.CharField(max_length=250)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=25)

    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='office_location')

    def __str__(self):
        return self.office_name


class In_Network_Insurance(models.Model):
    insurance_name = ArrayField(models.CharField(
        max_length=100))
    office = models.ForeignKey(
        Office_Location, on_delete=models.CASCADE, related_name='insurance_name')

    def __str__(self):
        return ','.join(self.insurance_name)


class Review(models.Model):
    description = models.TextField()
    overall_rating = models.IntegerField()
    bed_side_rating = models.IntegerField()
    wait_time_rating = models.IntegerField()
    created_at = models.DateTimeField()
    doctor = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, related_name='reviews')
    owner = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name="reviews")

    def __int__(self):
        return self.overall_rating


class Profile(models.Model):
    pet_name = models.CharField(max_length=50)
    pet_age = models.IntegerField()
    pet_type = models.CharField(max_length=50)
    pet_gender = models.CharField(max_length=10)
    pet_service = models.CharField(max_length=50)
    owner_first_name = models.CharField(max_length=50)
    owner_last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    owner = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name="profile")

    def __str__(self):
        return self.owner_first_name


class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    reason_for_visiting = models.TextField(blank=True, null=True)
    office = models.ForeignKey(
        Office_Location, on_delete=models.CASCADE, related_name='appointment')
    owner = models.ForeignKey(
        'auth.User', on_delete=models.CASCADE, related_name="appointment")

    def __str__(self):
        return self.owner.username
<<<<<<< HEAD
>>>>>>> 1e5bb15153522aec51664c9fff011da3ebea3805
=======
>>>>>>> 4bbd0be2d2db4b4d1ca72ad44ddea8aecd540258
