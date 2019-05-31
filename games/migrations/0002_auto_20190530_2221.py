# Generated by Django 2.0.13 on 2019-05-30 20:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='skills',
            new_name='skill',
        ),
        migrations.AddField(
            model_name='game',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to=''),
            preserve_default=False,
        ),
    ]
