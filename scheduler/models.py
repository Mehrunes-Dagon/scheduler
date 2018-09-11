from django.db import models
from uuid import uuid4


class Employer(models.Model):
    id = models.models.UUIDField(
        primary_field=True, default=uuid4, editable=False)
    companyName = models.charField(max_length=100)
