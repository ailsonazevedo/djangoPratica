# Generated by Django 4.0.1 on 2022-02-02 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lembretes', '0003_alter_lembrete_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='lembrete',
            name='data_lembrete',
            field=models.DateTimeField(null=True, verbose_name='Data do Lembrete'),
        ),
    ]
