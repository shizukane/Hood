from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch  import receiver
from django.http import Http404

class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=150)
    occupants = models.IntegerField()
    image = models.ImageField(default='hood.jpg', upload_to='hood/')
    datecreated = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hood')
    health_department_contact = models.IntegerField()
    police_authority_contact = models.IntegerField()

    def __str__(self):
        return f'{self.name} Neighborhood'

    class Meta:
        db_table ='Neighborhood'

    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

class Profile(models.Model):
    name = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=255)
    user= models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    neighborhood = models.ForeignKey(Neighborhood, null=True, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile/')

    def __str__(self):
        return f'{self.user.username} Profile'

    class Meta:
        db_table ='Profile'

    @receiver(post_save, sender=User)
    def update_create_profile(sender,instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender = User)
    def save_profile(sender,instance,**kwargs):
        instance.profile.save()


class Business(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.user} Business'

    class Meta:
        db_table ='Business'

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()


    @classmethod
    def search_by_name(cls,search_term):
        business = cls.objects.filter(name__icontains=search_term)
        return business




class Post(models.Model):
    title = models.CharField(max_length=100)
    story = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE)


    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def __str__(self):
        return f'{self.title} Post'
