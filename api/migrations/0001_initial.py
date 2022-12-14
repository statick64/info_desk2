# Generated by Django 4.0.7 on 2022-09-04 17:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemName',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('sys_name', models.CharField(max_length=250)),
                ('pc_boot_time', models.CharField(max_length=250)),
                ('total_size', models.CharField(max_length=250)),
                ('total_memory', models.CharField(max_length=250)),
                ('total_cores', models.CharField(max_length=250)),
                ('processor', models.CharField(max_length=250)),
                ('usage_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
