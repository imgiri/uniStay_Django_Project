# Generated by Django 5.0.3 on 2024-03-13 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unistay', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accommodation',
            old_name='accommodation_type',
            new_name='type',
        ),
        migrations.AddField(
            model_name='accommodation',
            name='bathroom_type',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='bedrooms',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='accommodation',
            name='budget',
            field=models.IntegerField(default=200),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user_type',
            field=models.CharField(choices=[('individual', 'Individual'), ('business', 'Business')], default='individual', max_length=20),
        ),
    ]
