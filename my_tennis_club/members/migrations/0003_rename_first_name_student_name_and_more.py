# Generated by Django 4.1.7 on 2023-03-27 13:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='last_name',
            new_name='surname',
        ),
    ]
