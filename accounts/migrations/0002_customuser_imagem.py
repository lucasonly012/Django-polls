# Generated by Django 4.2.6 on 2023-10-10 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='imagem',
            field=models.FileField(default=None, null=True, upload_to='images'),
        ),
    ]
