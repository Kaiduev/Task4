# Generated by Django 3.0.3 on 2020-03-09 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0005_auto_20200309_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='branch',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='course_app.Course'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='course',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='course_app.Course'),
        ),
    ]
