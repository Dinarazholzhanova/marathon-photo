# Generated by Django 3.0.7 on 2020-06-06 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('runners', '0001_initial'),
        ('competitions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competition', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competitions.Competition')),
                ('runner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='runners.Runner')),
            ],
        ),
    ]
