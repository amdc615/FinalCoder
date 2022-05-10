# Generated by Django 4.0.3 on 2022-04-12 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('familiares_coder', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
                ('animal', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='PeliculaFavorita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('genero', models.CharField(max_length=40)),
                ('estreno', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='familiar',
            name='edad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
