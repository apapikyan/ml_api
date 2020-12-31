# Generated by Django 3.1.4 on 2020-12-31 20:38

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.TextField(max_length=25)),
                ('description', models.TextField()),
                ('hyperparameters', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('configuration', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='configuration', to='api.config')),
            ],
        ),
    ]
