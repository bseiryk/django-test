from django.db import models
from django.core import validators



class Override:
    def __str__(self):
        return self.name


class Rubric(Override, models.Model):
    name = models.CharField(max_length=20, db_index=True)


class Bd(models.Model):
    title = models.CharField(max_length=50, verbose_name='Name')
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT, null=True)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-published']


# many to many
class Technology(Override, models.Model):
    name = models.CharField(max_length=50)


# one to many
class Education(Override, models.Model):
    name = models.CharField(max_length=50)


# one to one
class Expertise(Override, models.Model):
    name = models.CharField(max_length=50)


class Profile(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    salary_min = models.IntegerField(
        null=True,
        validators=[validators.MinValueValidator(limit_value=3, message='adasdawd')],
    )
    email = models.EmailField(unique=True)
    is_hired = models.BooleanField(default=False)
    birth_date = models.DateTimeField(null=True)
    expertise = models.OneToOneField(
        'Expertise',
        on_delete=models.CASCADE,
    )
    education = models.ForeignKey(
        'Education',
        on_delete=models.PROTECT,
        related_query_name='entries'
    )
    technologies = models.ManyToManyField('Technology')

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
