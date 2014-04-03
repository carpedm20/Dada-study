# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'School'
        db.create_table(u'school_school', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('logo_url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
        ))
        db.send_create_signal(u'school', ['School'])

        # Adding M2M table for field course_set on 'School'
        m2m_table_name = db.shorten_name(u'school_school_course_set')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('school', models.ForeignKey(orm[u'school.school'], null=False)),
            ('course', models.ForeignKey(orm[u'school.course'], null=False))
        ))
        db.create_unique(m2m_table_name, ['school_id', 'course_id'])

        # Adding model 'Course'
        db.create_table(u'school_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('course_id', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal(u'school', ['Course'])


    def backwards(self, orm):
        # Deleting model 'School'
        db.delete_table(u'school_school')

        # Removing M2M table for field course_set on 'School'
        db.delete_table(db.shorten_name(u'school_school_course_set'))

        # Deleting model 'Course'
        db.delete_table(u'school_course')


    models = {
        u'school.course': {
            'Meta': {'object_name': 'Course'},
            'course_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        u'school.school': {
            'Meta': {'object_name': 'School'},
            'course_set': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['school.Course']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo_url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['school']