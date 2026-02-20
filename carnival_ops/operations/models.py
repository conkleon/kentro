from django.db import models

class Team(models.Model):
    STATUS_CHOICES = [
        ('OFF', 'Standby / Εκτός'),
        ('GREEN', 'Πράσινο - Ελεύθερη'),
        ('YELLOW', 'Κίτρινο - Περιπολία'),
        ('RED', 'Κόκκινο - Περιστατικό'),
        ('PURPLE', 'Μωβ - Σταθερό Σημείο'),
    ]

    call_sign = models.CharField(max_length=10, unique=True, verbose_name="Κωδικός")
    leader_full_name = models.CharField(max_length=150, blank=True, verbose_name="Ονοματεπώνυμο Υπευθύνου")
    leader_phone = models.CharField(max_length=20, blank=True, verbose_name="Τηλέφωνο Υπευθύνου")
    members_list = models.TextField(blank=True, verbose_name="Μέλη Ομάδας") # Αποθήκευση ως κείμενο
    
    location = models.CharField(max_length=100, blank=True)
    incident_report = models.TextField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='OFF')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.call_sign} - {self.leader_full_name}"