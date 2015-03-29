# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ip_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='submission_date',
            field=models.DateField(default=datetime.datetime(2015, 3, 29, 16, 55, 48, 539993, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='first_name',
            field=models.CharField(default=datetime.datetime(2015, 3, 29, 16, 55, 55, 75752, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='last_name',
            field=models.CharField(default=datetime.datetime(2015, 3, 29, 16, 56, 0, 344328, tzinfo=utc), max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='idea',
            name='industry',
            field=models.CharField(max_length=50, choices=[(b'H', b'Health'), (b'T', b'Technology'), (b'E', b'Education'), (b'F', b'Finance'), (b'R', b'Travel')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=254),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userlike',
            name='like_dislike',
            field=models.IntegerField(default=0, choices=[(1, b'Like'), (0, b'Neutral')]),
            preserve_default=True,
        ),
    ]
