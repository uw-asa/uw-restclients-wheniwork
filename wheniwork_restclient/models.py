from django.db import models
from datetime import time


class Account(models.Model):
    account_id = models.PositiveIntegerField(null=True)
    master_id = models.PositiveIntegerField(null=True)
    company = models.CharField(max_length=500)

    def __str__(self):
        return self.company


class User(models.Model):
    user_id = models.PositiveIntegerField(null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    employee_code = models.CharField(max_length=100, null=True)

    def __str__(self):
        return "%s %s" % self.employee_code


class Location(models.Model):
    location_id = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Position(models.Model):
    position_id = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name


class Site(models.Model):
    site_id = models.PositiveIntegerField(null=True)
    name = models.CharField(max_length=100, null=True)
    location_id = models.PositiveIntegerField(null=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Shift(models.Model):
    shift_id = models.PositiveIntegerField(null=True)
    account_id = models.PositiveIntegerField(null=True)
    user_id = models.PositiveIntegerField(null=True)
    location_id = models.PositiveIntegerField(null=True)
    position_id = models.PositiveIntegerField(null=True)
    site_id = models.PositiveIntegerField(null=True)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    notes = models.CharField(max_length=350)


class Request(models.Model):
    STATUS_PENDING = 0
    STATUS_CANCELED = 1
    STATUS_ACCEPTED = 2
    STATUS_EXPIRED = 3

    TYPE_UNPAIDTIMEOFF = 0
    TYPE_PAIDTIMEOFF = 1
    TYPE_SICKLEAVE = 2
    TYPE_HOLIDAY = 3

    request_id = models.PositiveIntegerField(null=True)
    account_id = models.PositiveIntegerField(null=True)
    user_id = models.PositiveIntegerField(null=True)
    creator_id = models.PositiveIntegerField(null=True)
    status = models.PositiveSmallIntegerField(choices=(
        (STATUS_PENDING, 'Pending'),
        (STATUS_CANCELED, 'Canceled'),
        (STATUS_ACCEPTED, 'Accepted'),
        (STATUS_EXPIRED, 'Expired')))
    type = models.PositiveSmallIntegerField(choices=(
        (TYPE_UNPAIDTIMEOFF, 'Unpaid Time Off'),
        (TYPE_PAIDTIMEOFF, 'Paid Time Off'),
        (TYPE_SICKLEAVE, 'Sick Leave'),
        (TYPE_HOLIDAY, 'Holiday')))
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    canceled_by = models.ForeignKey(User, related_name='+')
    hours = models.DecimalField(max_digits=5, decimal_places=2)

    def is_allday(self):
        if self.start_time.time() == time(0, 0, 0) \
                and self.end_time.time() == time(23, 59, 59):
            return True
        return False


class Message(models.Model):
    message_id = models.PositiveIntegerField(null=True)
    account_id = models.PositiveIntegerField(null=True)
    user_id = models.PositiveIntegerField(null=True)
    request_id = models.PositiveIntegerField(null=True)
    swap_id = models.PositiveIntegerField(null=True)
    conversation_id = models.PositiveIntegerField(null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    type = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title
