# Generated by Django 4.0.5 on 2022-06-20 05:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HoodApp', '0006_rename_prof_photo_profile_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighbourhood',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='HoodApp.location'),
        ),
    ]