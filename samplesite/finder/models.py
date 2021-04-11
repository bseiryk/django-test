from django.db import models
from .constants import types


class Override:
    def __str__(self):
        return self.name


class Items(Override, models.Model):
    name = models.CharField(max_length=256)
    # make delete via post delete
    parent = models.ForeignKey(
        'self',
        related_name="parent_entity",
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    is_root = models.BooleanField(default=False)
    file = models.FileField(blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    type = models.CharField(choices=types, max_length=50)
    content_items = models.ManyToManyField('self', symmetrical=False, blank=True)

    class Meta:
        verbose_name = 'Files and Folders'
        verbose_name_plural = 'Files and Folders'
