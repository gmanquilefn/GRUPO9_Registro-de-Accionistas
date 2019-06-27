from django.db import migrations, models
import django.db.models.manager

class Migration(migrations.Migration):
  initial = True
  
  dependencies = [
  ]

  operations = [
    migrations.CreateModel(
      name='Accionista',

      fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('run', models.CharField(max_length=20)),
        ('nombres', models.CharField(default='', max_length=100)),
        ('apellidos', models.CharField(default='', max_length=100)),
        ('totalAcciones', models.IntegerField(default=0)),
        ('nacionalidad', models.CharField(default='', max_length=20)),
        ('direccion', models.CharField(default='', max_length=60)),
        ('telefono', models.CharField(default='', max_length=20)),
        ('email', models.CharField(default='example@correo.com', max_length=100)),
        ('fax', models.CharField(default='', max_length=20)),
      ],

      managers=[
        ('accionistas', django.db.models.manager.Manager()),
      ],
    ),
  ]
