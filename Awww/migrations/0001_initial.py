# Generated by Django 2.0.7 on 2022-07-31 16:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MusicPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.ManyToManyField(related_name='musicpost_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]