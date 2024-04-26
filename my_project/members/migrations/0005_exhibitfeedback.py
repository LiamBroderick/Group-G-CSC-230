# Generated by Django 5.0.1 on 2024-04-20 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_section_exhibit_playtypecognitive_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExhibitFeedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exhibit_name', models.CharField(max_length=100)),
                ('rating', models.CharField(max_length=10)),
                ('feedback_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]