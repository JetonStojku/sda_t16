# Generated by Django 4.2 on 2023-10-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0005_movie_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='color',
            field=models.CharField(choices=[('badge-primary', 'Primary'), ('badge-secondary', 'Secondary'), ('badge-success', 'Success'), ('badge-danger', 'Danger'), ('badge-warning', 'Warning'), ('badge-info', 'Info'), ('badge-light', 'Light'), ('badge-dark', 'Dark')], default='badge-primary', max_length=40),
        ),
        migrations.AlterField(
            model_name='movie',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='movie_cover'),
        ),
    ]
