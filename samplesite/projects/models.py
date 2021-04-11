from django.db import models
from finder.models import Items


class Override:
    def __str__(self):
        return self.name


class Projects(Override, models.Model):
    name = models.CharField(max_length=256)
    root_folder = models.OneToOneField(
        Items,
        on_delete=models.DO_NOTHING,
    )
    is_deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Projects'
        verbose_name_plural = 'Projects'
