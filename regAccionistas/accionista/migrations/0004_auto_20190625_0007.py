# Generated by Django 2.2.1 on 2019-06-25 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accionista', '0003_auto_20190624_2327'),
    ]

    operations = [
        migrations.AddField(
            model_name='accionista',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accionista',
            name='run',
            field=models.CharField(max_length=20),
        ),
    ]
