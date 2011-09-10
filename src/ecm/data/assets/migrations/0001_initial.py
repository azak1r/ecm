# Copyright (c) 2010-2011 Robin Jarry
# 
# This file is part of EVE Corporation Management.
# 
# EVE Corporation Management is free software: you can redistribute it and/or 
# modify it under the terms of the GNU General Public License as published by 
# the Free Software Foundation, either version 3 of the License, or (at your 
# option) any later version.
# 
# EVE Corporation Management is distributed in the hope that it will be useful, 
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY 
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for 
# more details.
# 
# You should have received a copy of the GNU General Public License along with 
# EVE Corporation Management. If not, see <http://www.gnu.org/licenses/>.

#@PydevCodeAnalysisIgnore
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Asset'
        db.create_table('assets_asset', (
            ('itemID', self.gf('django.db.models.fields.BigIntegerField')(primary_key=True)),
            ('solarSystemID', self.gf('django.db.models.fields.BigIntegerField')()),
            ('stationID', self.gf('django.db.models.fields.BigIntegerField')()),
            ('hangarID', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('container1', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('container2', self.gf('django.db.models.fields.BigIntegerField')(null=True, blank=True)),
            ('typeID', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('quantity', self.gf('django.db.models.fields.BigIntegerField')(default=0)),
            ('flag', self.gf('django.db.models.fields.BigIntegerField')()),
            ('singleton', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('hasContents', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('assets', ['Asset'])

        # Adding model 'AssetDiff'
        db.create_table('assets_assetdiff', (
            ('id', self.gf('ecm.lib.bigintpatch.BigAutoField')(primary_key=True)),
            ('solarSystemID', self.gf('django.db.models.fields.BigIntegerField')()),
            ('stationID', self.gf('django.db.models.fields.BigIntegerField')()),
            ('hangarID', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('typeID', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('quantity', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 7, 31, 4, 47, 27, 970000), db_index=True)),
            ('new', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('flag', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal('assets', ['AssetDiff'])


    def backwards(self, orm):
        
        # Deleting model 'Asset'
        db.delete_table('assets_asset')

        # Deleting model 'AssetDiff'
        db.delete_table('assets_assetdiff')


    models = {
        'assets.asset': {
            'Meta': {'object_name': 'Asset'},
            'container1': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'container2': ('django.db.models.fields.BigIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'flag': ('django.db.models.fields.BigIntegerField', [], {}),
            'hangarID': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'hasContents': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'itemID': ('django.db.models.fields.BigIntegerField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.BigIntegerField', [], {'default': '0'}),
            'singleton': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'solarSystemID': ('django.db.models.fields.BigIntegerField', [], {}),
            'stationID': ('django.db.models.fields.BigIntegerField', [], {}),
            'typeID': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        },
        'assets.assetdiff': {
            'Meta': {'object_name': 'AssetDiff'},
            'date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 7, 31, 4, 47, 27, 970000)', 'db_index': 'True'}),
            'flag': ('django.db.models.fields.BigIntegerField', [], {}),
            'hangarID': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'id': ('ecm.lib.bigintpatch.BigAutoField', [], {'primary_key': 'True'}),
            'new': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'solarSystemID': ('django.db.models.fields.BigIntegerField', [], {}),
            'stationID': ('django.db.models.fields.BigIntegerField', [], {}),
            'typeID': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['assets']
