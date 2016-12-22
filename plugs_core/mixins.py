from django.db import models
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.exceptions import ValidationError

class Slugable(models.Model):

    slug = models.SlugField(max_length=75, null=False, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        """
        Overrides the save method
        """
        self.slug = self.create_slug()
        super(Slugable, self).save(*args, **kwargs)

    def create_slug(self):
        """
        Creates slug, checks if slug is unique, and loop if not
        """
        name = self.slug_source
        counter = 0
        # loops until slug is unique
        while True:
            if counter == 0:
                slug = slugify(name)
            else:
                # using the counter var to bump the slug name
                slug = slugify('{0} {1}'.format(name, str(counter)))
            try:
                # does the slug already exist, excluding the current object
                self.__class__.objects.exclude(pk=self.pk).get(slug=slug)
                # if slug exists increment counter and loop
                counter += 1
            except ObjectDoesNotExist:
                # the slug does not exist
                # we can break from the loop
                break
        return slug


class Timestampable(models.Model):
    """
    Adds created and updated fields
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
