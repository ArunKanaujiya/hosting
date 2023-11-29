# Generated by Django 4.2.5 on 2023-11-27 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0007_customer_address_customer_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('price', models.PositiveIntegerField()),
                ('category', models.CharField(choices=[('COMIX', 'comix'), ('LANGUAGE', 'language'), ('NOWEL', 'nowel'), ('REFRENCE', 'refrence'), ('HISTORICAL', 'historical')], default='nowel', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Receipe',
        ),
        migrations.AlterField(
            model_name='customer',
            name='age',
            field=models.IntegerField(default=18),
        ),
    ]