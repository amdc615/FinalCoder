# Generated by Django 4.0.4 on 2022-05-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares_coder', '0003_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email_address', models.EmailField(max_length=150)),
                ('message', models.CharField(max_length=2000)),
            ],
        ),
    ]