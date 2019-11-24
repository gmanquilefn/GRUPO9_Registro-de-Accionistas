# Generated by Django 2.2.5 on 2019-09-14 23:46

from django.db import migrations, models
import django.db.models.manager
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accionista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(max_length=20, null=False)),
                ('nombres', models.CharField(default='', max_length=100)),
                ('apellidos', models.CharField(default='', max_length=100)),
                ('totalAcciones', models.IntegerField(default=0)),
                ('nacionalidad', models.CharField(default='', max_length=20)),
                ('direccion', models.CharField(default='', max_length=60)),
                ('telefono', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='example@correo.com', max_length=100)),
                ('fax', models.CharField(default='', max_length=20)),
                ('imagen', models.FileField(null=False, upload_to='accionistas')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            managers=[
                ('accionistas', django.db.models.manager.Manager()),
            ],
        ),
    ]