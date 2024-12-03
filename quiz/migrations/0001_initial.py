# Generated by Django 5.1.3 on 2024-12-02 11:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=256)),
                ('option_1', models.CharField(max_length=256)),
                ('option_2', models.CharField(max_length=256)),
                ('option_3', models.CharField(max_length=256)),
                ('option_4', models.CharField(max_length=256)),
                ('correct_option', models.PositiveSmallIntegerField(choices=[(1, 'Option1'), (2, 'Option2'), (3, 'Option3'), (4, 'Option4')])),
            ],
        ),
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField()),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='quiz.question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]