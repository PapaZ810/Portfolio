# Generated by Django 5.1.1 on 2024-09-12 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_alter_project_image_alter_project_short_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='bioText',
            new_name='bio_text',
        ),
    ]
