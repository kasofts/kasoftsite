# Generated by Django 4.2.1 on 2023-05-26 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kapp', '0003_alter_enquiry_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='file',
            field=models.FileField(default=None, upload_to='media/cv/'),
        ),
    ]
