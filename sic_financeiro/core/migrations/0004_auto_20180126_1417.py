# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-01-26 17:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_auto_20180115_0857'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoDespesa',
            fields=[
                ('id', models.AutoField(db_column='pk_tipo_despesa', primary_key=True, serialize=False)),
                ('nome', models.CharField(db_column='nome_tipo_despesa', max_length=100, unique=True)),
                ('cor_layout', models.CharField(db_column='cor_layout_tipo_despesa', max_length=10)),
                ('data_modificacao', models.DateTimeField(auto_now=True, db_column='data_modificacao_tipo_despesa', null=True)),
                ('usuario', models.ForeignKey(db_column='fk_user_tipo_despesa', on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tb_tipo_despesa',
            },
        ),
        migrations.AlterField(
            model_name='conta',
            name='cor_layout',
            field=models.CharField(choices=[('primary', 'Azul'), ('success', 'Verde'), ('warning', 'Laranja'), ('danger', 'Vermelho'), ('pink', 'Rosa'), ('default', 'Cinza'), ('purple', 'Roxo'), ('info', 'info')], db_column='cor_layout_conta', max_length=10),
        ),
    ]
