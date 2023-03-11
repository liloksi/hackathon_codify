# Generated by Django 4.1.7 on 2023-03-11 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('school', '0001_initial'),
        ('online_queue', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Olympiad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(verbose_name='оценки')),
                ('year', models.IntegerField(verbose_name='год')),
                ('school', models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='olympiad', to='school.school', verbose_name='школа')),
                ('student', models.ForeignKey(max_length=255, on_delete=django.db.models.deletion.CASCADE, to='online_queue.student', verbose_name='студент')),
            ],
            options={
                'verbose_name': 'Олимпиада',
                'verbose_name_plural': 'Олимпиады',
            },
        ),
        migrations.CreateModel(
            name='GoldenCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(verbose_name='оценки')),
                ('year', models.IntegerField(verbose_name='год')),
                ('school_fullname', models.ForeignKey(max_length=255, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='golden', to='school.school', verbose_name='название школы')),
                ('student_fullname', models.OneToOneField(max_length=50, null=True, on_delete=django.db.models.deletion.SET_NULL, to='online_queue.student', verbose_name='имя студента')),
            ],
            options={
                'verbose_name': 'Золотой сертификат',
                'verbose_name_plural': 'Золотые сертификаты',
            },
        ),
    ]
