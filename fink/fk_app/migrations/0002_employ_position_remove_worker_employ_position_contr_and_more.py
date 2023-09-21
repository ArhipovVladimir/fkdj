# Generated by Django 4.2.5 on 2023-09-20 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fk_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employ_position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='worker',
            name='employ_position_contr',
        ),
        migrations.RemoveField(
            model_name='worker',
            name='surname',
        ),
        migrations.AddField(
            model_name='worker',
            name='employ_position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fk_app.employ_position'),
            preserve_default=False,
        ),
    ]
