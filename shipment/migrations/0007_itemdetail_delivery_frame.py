# Generated by Django 3.2 on 2021-11-27 18:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0006_alter_itemdetail_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemdetail',
            name='delivery_frame',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 4, 18, 12, 45, 779750, tzinfo=utc)),
        ),
    ]