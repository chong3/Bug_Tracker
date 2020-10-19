# Generated by Django 3.1.2 on 2020-10-19 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_summary', models.CharField(max_length=100)),
                ('issue_description', models.TextField()),
                ('date_submitted', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('target_resolution', models.DateTimeField(default=django.utils.timezone.now)),
                ('priority', models.CharField(max_length=30)),
                ('issue_status', models.CharField(max_length=30)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]