# Generated by Django 3.0.3 on 2020-03-09 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0002_auto_20200309_2121'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['content_type']},
        ),
    ]
