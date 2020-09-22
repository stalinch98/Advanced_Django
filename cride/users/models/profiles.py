"""Profile model."""

# Django
from django.db import models

# Utilities
from cride.utils.models import CRideModel


class Profiel(CRideModel):
    """Profile model.
    A profile holds a user's public data like biography, picture,
    and statistics
    """

    users = models.OneToOneField('users.User', )
