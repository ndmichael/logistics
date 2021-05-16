from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class ItemSender(models.Model):

    """
    Model for item sender
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=150)
    address =  models.CharField(max_length=150)
    postal_code = models.CharField(max_length=150)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_sent = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date_sent',)

    def __str__(self):
        return f'{self.user}'


class ItemReciever(models.Model):  
    """
    Model for item receiver
    """
    sender = models.ForeignKey(ItemSender, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=250)
    email = models.EmailField(max_length=200)
    address =  models.CharField(max_length=150)
    postal_code = models.CharField(max_length=150)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    date_sent = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date_sent',)

    def __str__(self):
        return f'{self.fullname}'


class ItemDetail (models.Model):   
    '''
        Item details model
    '''

    STATUS= (
        ('sent', 'SENT'),
        ('pending', 'PENDING'),
    )

    item_sender = models.ForeignKey(ItemSender, on_delete=models.CASCADE)
    item_reciever = models.ForeignKey(ItemReciever, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    quantity = models.IntegerField()
    description = models.TextField(max_length= 1000)
    weight = models.CharField(max_length=10)
    paid = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS, default='PENDING')
    date_sent = models.DateTimeField(default=timezone.now)
    date_recieved = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ('-date_sent', '-date_recieved')

    def __str__(self):
        return f'{self.iname}'