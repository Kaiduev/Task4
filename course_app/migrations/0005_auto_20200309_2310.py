# Generated by Django 3.0.3 on 2020-03-09 23:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0004_auto_20200309_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course_app.Course', unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='course_app.Course', unique=True),
        ),
    ]
