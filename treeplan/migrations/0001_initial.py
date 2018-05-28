# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('milestone', models.DecimalField(max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('x', models.DecimalField(max_digits=10, decimal_places=2)),
                ('y', models.DecimalField(max_digits=10, decimal_places=2)),
                ('name', models.CharField(max_length=100)),
                ('sciName', models.CharField(max_length=100)),
                ('diameter', models.DecimalField(max_digits=10, decimal_places=2)),
                ('height', models.DecimalField(max_digits=10, decimal_places=2)),
                ('heightToCrown', models.DecimalField(max_digits=10, decimal_places=2)),
                ('crownSpread', models.DecimalField(max_digits=10, decimal_places=2)),
                ('age', models.DecimalField(max_digits=10, decimal_places=2)),
                ('ontogenetic', models.CharField(max_length=100)),
                ('health', models.CharField(max_length=100)),
                ('note', models.CharField(max_length=100)),
                ('plan', models.ForeignKey(verbose_name=b'plan', to='treeplan.Plan')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
