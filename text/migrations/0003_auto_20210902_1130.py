# Generated by Django 3.2.6 on 2021-09-02 06:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('text', '0002_auto_20210901_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sendemail',
            old_name='subject',
            new_name='email',
        ),
        migrations.RemoveField(
            model_name='sendemail',
            name='img',
        ),
    ]