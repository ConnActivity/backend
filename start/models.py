from django.db import models


# Create your models here.

class Tag(models.Model):
    value = models.CharField(max_length=30)


class User(models.Model):
    class Gender(models.TextChoices):
        maennlich = 'm', ('männlich')
        weiblich = 'w', ('weiblich')
        divers = 'd', ('divers')
        nicht_angeben = 'x', ('nicht angeben')

    user_id = models.CharField(max_length=30, primary_key=True, unique=True, editable=False)
    username = models.CharField(max_length=20, unique=True)
    gender = models.CharField(choices=Gender.choices, max_length=1, default=Gender.nicht_angeben)
    user_email = models.CharField(max_length=50, unique=True)
    user_age = models.IntegerField(default=0, blank=False)
    university = models.CharField(max_length=100)
    user_bio = models.CharField(max_length=500)
    user_tags = models.ManyToManyField(Tag, blank=True)


class Event(models.Model):
    title = models.CharField(max_length=200)
    date_published = models.DateTimeField('date published')
    date = models.DateTimeField('date of event')
    location = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, null=False, blank=True)
    member_limit = models.IntegerField(default=4)
    image = models.FileField(upload_to='images/', null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)
    member_list = models.ManyToManyField(User, related_name='member_list_user', blank=True)
    is_private = models.BooleanField(default=False)
    member_wait_list = models.ManyToManyField(User, blank=True, related_name='wait_list_user')
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=42)  # required for django
