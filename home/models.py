from django.db import models

class Storage(models.Model):
    item = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.item


class StorageSixA(models.Model):
    item = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'StorageSixA'

    def __str__(self):
        return self.item

class StorageSixB(models.Model):
    item = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'StorageSixB'

    def __str__(self):
        return self.item

class StorageSixC(models.Model):
    item = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'StorageSixC'

    def __str__(self):
        return self.item
        

class StorageSixE(models.Model):
    item = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'StorageSixE'

    def __str__(self):
        return self.item
