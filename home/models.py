from django.db import models

class Storage(models.Model):
    item = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.item


''' 
In this file, I used a very general way to store all the information with separate models since this is a 
simple application. Alternative way is create one model and an handle all information using that.
'''


# Models in Django are classes that represent data base tables.

# This Model represents all sixA information
class StorageSixA(models.Model):
    item = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        # verbose_name_plural is a human readable name you give to the objects
        verbose_name_plural = 'StorageSixA'

    # The __str__ method should be defined in a way that is easy to read and outputs all the members of the class
    def __str__(self):
        return self.item # On admin panel, where all the list of infomation is present. Title of the row will be 'item' name 

# This Model represents all sixB information
class StorageSixB(models.Model):
    item = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)


    class Meta:
        verbose_name_plural = 'StorageSixB'

    def __str__(self):
        return self.item

# This Model represents all sixC information
class StorageSixC(models.Model):
    item = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'StorageSixC'

    def __str__(self):
        return self.item
        

# This Model represents all sixE information
class StorageSixE(models.Model):
    item = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'StorageSixE'

    def __str__(self):
        return self.item
