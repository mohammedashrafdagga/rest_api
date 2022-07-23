import datetime
import uuid

from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.fields import AutoSlugField


class Collage(models.Model):
    name = models.CharField(max_length=255)
    year_of_collage = models.IntegerField()
    date_of_created = models.DateField(auto_now_add=True)
    manger_of_collage = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.name


class Major(models.Model):
    collage = models.ForeignKey(Collage, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = AutoSlugField(null=True, default=None,
                         unique=True, populate_from='name')
    number_of_hour = models.IntegerField()
    date_of_created = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Semester(models.Model):
    semester = (('First Semester', 'First Semester'),
                ('Second Semester', 'Second Semester'))
    name = models.CharField(choices=semester, max_length=100)
    date_of_start = models.DateField()
    date_of_end = models.DateField()

    def __str__(self) -> str:
        return self.name


class Courses(models.Model):
    collage = models.ForeignKey(Collage, on_delete=models.CASCADE)
    major = models.ManyToManyField(Major)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    year = models.CharField(
        choices=(('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')), max_length=10)
    slug = AutoSlugField(default=None,
                         unique=True, populate_from='name')
    id_course = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return f'{self.name} {self.id_course}'


class Staff(models.Model):
    gender_c = (('Male', 'Male'),
                ('Female', 'Female'))

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    staff_image = models.ImageField(upload_to='staff_image/')
    collage = models.ForeignKey(
        Collage, on_delete=models.CASCADE)
    fields = models.CharField(max_length=155)
    dob = models.DateField()
    gender = models.CharField(choices=gender_c, max_length=6)
    date_of_started = models.DateField(auto_now_add=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name}_{self.user.last_name}_{self.fields}'


class Student(models.Model):
    gender_c = (('Male', 'Male'),
                ('Female', 'Female'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    std_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    std_image = models.ImageField(upload_to='images/', null=True, blank=True)
    collage = models.ForeignKey(
        Collage, on_delete=models.CASCADE, null=True, blank=True)
    major = models.ForeignKey(
        Major, on_delete=models.CASCADE, null=True, blank=True)
    address = models.CharField(max_length=155, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    gender = models.CharField(
        choices=gender_c, null=True, blank=True, max_length=10)
    phone_number = models.CharField(max_length=15, null=True, blank=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


# @receiver(post_save, sender=User)
# def create_student(sender, instance, created, ** kwargs):
#     if created:
#         Student.objects.create(
#             user=instance
#         )


class NoSemster(models.Model):

    YEAR_CHOICES = [(r, r) for r in range(2001, datetime.date.today().year+1)]
    # semster
    semster = models.ForeignKey(Semester, on_delete=models.CASCADE)
    # year
    year = models.IntegerField(
        ('year'), choices=YEAR_CHOICES, default=datetime.date.today().year)
    # slug from year and semster
    slug = AutoSlugField(default=None,
                         unique=True, populate_from=['semster', 'year'])

    def __str__(self) -> str:
        return str(self.slug)


class SemsterCourses(models.Model):
    # current semster
    no_semster = models.ForeignKey(NoSemster, on_delete=models.CASCADE)
    # semster
    semster = models.ForeignKey(Semester, on_delete=models.CASCADE)
    # instructor
    instructor = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True)
    # courses
    coures = models.ForeignKey(Courses, on_delete=models.CASCADE)

    slug = AutoSlugField(default=None,
                         unique=True, populate_from=['no_semster', 'coures'])

    def __str__(self) -> str:
        return str(self.slug)


# POST what the some can create new instance from this.
