# Generated by Django 4.2.5 on 2023-11-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0006_customer_age_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
