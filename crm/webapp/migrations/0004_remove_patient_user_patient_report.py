# Generated by Django 4.2.6 on 2023-11-04 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_doctor_alter_userprofile_full_name_patient_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
        migrations.AddField(
            model_name='patient',
            name='report',
            field=models.FileField(default='patient_default_report.pdf', upload_to='Report/'),
        ),
    ]