from django.contrib import admin
# Importing all the models from Models.py file
from .models import Storage, StorageSixA, StorageSixB, StorageSixC, StorageSixE

admin.site.register(Storage)

'''
The register [admin.site.register()] function is used to add models to the Django admin so that data for those models 
can be created, deleted, updated and queried through the user interface.
'''

admin.site.register(StorageSixA)
admin.site.register(StorageSixB)
admin.site.register(StorageSixC)
admin.site.register(StorageSixE)