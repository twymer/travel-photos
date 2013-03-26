# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Photo.title'
        db.add_column(u'photos_photo', 'title',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=50),
                      keep_default=False)


        # Changing field 'Photo.image'
        db.alter_column(u'photos_photo', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    def backwards(self, orm):
        # Deleting field 'Photo.title'
        db.delete_column(u'photos_photo', 'title')


        # Changing field 'Photo.image'
        db.alter_column(u'photos_photo', 'image', self.gf('django.db.models.fields.files.FileField')(max_length=100))

    models = {
        u'photos.photo': {
            'Meta': {'object_name': 'Photo'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['photos']