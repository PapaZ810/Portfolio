# Generated by Django 5.1.1 on 2024-09-10 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_project_short_description_alter_project_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default='static/images/zoe.jpg', upload_to='static/images/'),
        ),
    ]
