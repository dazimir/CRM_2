# Generated by Django 4.0.5 on 2022-06-06 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_organization_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.EmailField(blank=True, max_length=255, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.EmailField(blank=True, max_length=255, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Фамилия'),
        ),
    ]
