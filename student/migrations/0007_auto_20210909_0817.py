# Generated by Django 3.2.4 on 2021-09-09 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0006_alter_student_nationality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('3', 'Prefer not to say')], max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='nationality',
            field=models.CharField(choices=[('Rwandan', 'Rwandan'), ('Kenyan', 'Kenyan'), ('Ugandan', 'Ugandan'), ('SouthSudanes', 'SouthSudanes'), ('Sudanes', 'Sudanes')], max_length=15, null=True),
        ),
    ]