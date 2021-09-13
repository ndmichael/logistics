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
    address =  models.CharField(max_length=150, blank=False, null=False)
    postal_code = models.CharField(max_length=150, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    country = models.CharField(max_length=100, blank=False, null=False)
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
    fullname = models.CharField(max_length=250, blank=False, null=False)
    email = models.EmailField(max_length=200, blank=False, null=False)
    address =  models.CharField(max_length=150, blank=False, null=False)
    postal_code = models.CharField(max_length=150, blank=False, null=False)
    city = models.CharField(max_length=100, blank=False, null=False)
    country = models.CharField(max_length=100, blank=False, null=False)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return f'{self.fullname}'


class ItemDetail (models.Model):   
    '''
        Item details model
    '''

    STATUS= (
        ('pending', 'PENDING'),
        ('sent', 'SENT'),
        ('delivered', 'DELIVERED'),       
    )

    PROBLEM = (
        ('paperwork', 'PAPERWORK_OVERLOAD'),
        ('custom clerance', 'CUSTOM CLEARANCE'),
        ('bad weather', 'BAD WEATHER'),
        ('holidays', 'HOLYDAYS'),
        ('no problem', 'No Problems'),
    )

    item_sender = models.ForeignKey(ItemSender, on_delete=models.CASCADE)
    item_reciever = models.ForeignKey(ItemReciever, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    slug = models.CharField(max_length=150)
    quantity = models.IntegerField()
    description = models.TextField(max_length= 1000)
    weight = models.CharField(max_length=10)
    image = models.ImageField(upload_to='food_photos', default='default.jpg')
    paid = models.BooleanField(default=False)
    status = models.CharField(choices=STATUS, default='PENDING', max_length=15)
    problem_type = models.CharField(choices=PROBLEM, default='NO PROBLEM', max_length=15)
    item_code = models.CharField(max_length=20)
    date_sent = models.DateTimeField(default=timezone.now)
    date_recieved = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ('-date_sent', '-date_recieved')

    def __str__(self):
        return f'{self.iname}'