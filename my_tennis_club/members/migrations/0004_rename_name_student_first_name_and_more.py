# Generated by Django 4.1.7 on 2023-03-27 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_rename_first_name_student_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='surname',
            new_name='last_name',
        ),
    ]
