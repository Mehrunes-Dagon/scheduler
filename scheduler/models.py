from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User


class Employer(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    companyName = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class Employee(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class Event(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid4, editable=False)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
