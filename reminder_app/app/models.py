from django.db import models
from django.utils import timezone


class Person(models.Model):
    name = models.CharField(max_length=200)
    # login + password

    def __str__(self):
        return self.name


class Event(models.Model):
    # will delete events whenever a person is deleted (no flowers without owners)
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.author.name + ' - ' + self.title

    def add_event(self):
        pass

    def delete_event(self):
        pass

    def remind_about_event(self):
        pass

