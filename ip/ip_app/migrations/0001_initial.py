# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('idea_id', models.AutoField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('industry', models.CharField(max_length=50, choices=[(b'HEALTH', b'Health'), (b'TRAVEL', b'Technology'), (b'EDUCATION', b'Education'), (b'FINANCE', b'Finance'), (b'TRAVEL', b'Travel')])),
                ('description', models.TextField()),
                ('keywords', models.TextField()),
                ('rating', models.IntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserLike',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('like_dislike', models.IntegerField(default=0, choices=[(1, b'Like'), (0, b'Neutral'), (-1, b'Dislike')])),
                ('idea_id', models.ForeignKey(to='ip_app.Idea')),
                ('user_id', models.ForeignKey(to='ip_app.User')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='idea',
            name='submittor_id',
            field=models.ForeignKey(to='ip_app.User'),
            preserve_default=True,
        ),
    ]
