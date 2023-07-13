from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm


class LeadershipMember(models.Model):
    """
    Model representing a leadership member.
    """
    # One-to-One relationship with the built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Fields for name, designation, and bio
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    bio = models.TextField()
    
    def __str__(self):
        return self.name
    
class PartyRegistration(models.Model):
    """
    Model representing a party registration.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    guests = models.PositiveIntegerField()

    def __str__(self):
        return self.user.username
    
class PartyRegistrationForm(ModelForm):
    """
    Form for party registration.
    """
    class Meta:
        model = PartyRegistration
        fields = ['name', 'email', 'phone', 'guests']
