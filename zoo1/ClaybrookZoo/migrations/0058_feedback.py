# Generated by Django 2.2.4 on 2020-04-08 11:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClaybrookZoo', '0057_booking_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('highlight', models.BooleanField(default=False)),
                ('sender', models.ForeignKey(on_delete='CASCADE', related_name='feedback_sender', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date',),
            },
        ),
    ]