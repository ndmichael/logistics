# Generated by Django 3.2 on 2021-09-13 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipment', '0002_itemdetail_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdetail',
            name='problem_type',
            field=models.CharField(choices=[('paperwork', 'PAPERWORK_OVERLOAD'), ('custom clerance', 'CUSTOM CLEARANCE'), ('bad weather', 'BAD WEATHER'), ('holidays', 'HOLYDAYS'), ('no problem', 'No Problems')], default='NO PROBLEM', max_length=15),
        ),
    ]