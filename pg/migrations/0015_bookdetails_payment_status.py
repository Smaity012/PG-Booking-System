# Generated by Django 4.2.3 on 2023-08-25 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pg', '0014_bookdetails_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookdetails',
            name='payment_status',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]