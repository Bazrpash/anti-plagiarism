# Generated by Django 2.1.5 on 2020-08-08 14:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_and_last_name', models.CharField(max_length=100)),
                ('uni_major', models.CharField(blank=True, max_length=50, null=True)),
                ('uni_name', models.CharField(max_length=50)),
                ('uni_position', models.CharField(blank=True, choices=[('PROF', 'PROF'), ('researcher', 'researcher'), ('OTHER_POS', 'OTHER_POS')], max_length=20, null=True)),
                ('is_visible', models.BooleanField(default=False)),
                ('is_blocked', models.BooleanField(default=False)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_graduated', models.BooleanField(default=False)),
                ('is_professor', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('notes', models.TextField(blank=True, default='')),
            ],
        ),
    ]
