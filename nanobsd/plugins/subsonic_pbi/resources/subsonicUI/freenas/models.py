from django.db import models


class Subsonic(models.Model):
    """
    Django model describing every tunable setting for subsonic
    """

    enable = models.BooleanField(default=False)
