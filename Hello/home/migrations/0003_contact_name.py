# Generated by Django 4.0.5 on 2022-08-09 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_contacts_contact_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='name',
            field=models.CharField(default='000000', max_length=122),
        ),
    ]
