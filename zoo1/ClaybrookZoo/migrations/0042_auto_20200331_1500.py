# Generated by Django 2.2.4 on 2020-03-31 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ClaybrookZoo', '0041_auto_20200331_1500'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mammal',
            name='animal',
            field=models.ForeignKey(null=True, on_delete='CASCADE', related_name='mammal', to='ClaybrookZoo.Animal'),
        ),
    ]