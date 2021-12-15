from enum import auto
from django.db import models


class users(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department_name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=20)
    emailID = models.EmailField(max_length=100)
    USN = models.CharField(max_length=20)

    class Meta:
        db_table = "users"


class admins(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    location = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=15)
    emailID = models.EmailField(max_length=100)

    class Meta:
        db_table = "admins"


class committee(models.Model):
    committee_id = models.IntegerField(primary_key=True)
    committee_name = models.CharField(max_length=100)

    class Meta:
        db_table = "committee"


class committee_members(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    emailID = models.EmailField(max_length=100)
    committee_id = models.ForeignKey(committee, on_delete=models.CASCADE)

    class Meta:
        db_table = "committee_members"


class resources(models.Model):
    resource_id = models.IntegerField(primary_key=True)
    resource_name = models.CharField(max_length=250)
    OEM = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=50)
    department_name = models.CharField(max_length=100)
    unit_cost = models.IntegerField()
    location = models.CharField(max_length=250)
    purchase_date = models.DateField(null=True, blank=True)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to="hello/")
    about = models.CharField(max_length=400)
    # adminId = models.ForeignKey(admins, on_delete=models.CASCADE)

    class Meta:
        db_table = "resources"


class test(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to="hello/")

    class Meta:
        db_table = "test"


class resource_logbook(models.Model):
    log_id = models.IntegerField(primary_key=True)
    member_id = models.ForeignKey(users, on_delete=models.CASCADE)
    admin_id = models.ForeignKey(admins, on_delete=models.CASCADE)
    resource_id = models.ForeignKey(resources, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()

    class Meta:
        db_table = "resource_logbook"


class tender(models.Model):
    tender_id = models.IntegerField(primary_key=True)
    OEM = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=50)
    unit_cost = models.IntegerField()
    resource_name = models.CharField(max_length=250)
    tender_issue_date = models.DateField()
    quantity = models.IntegerField()
    about = models.CharField(max_length=400)
    admin_id = models.ForeignKey(admins, on_delete=models.CASCADE)
    committee_id = models.ForeignKey(committee, on_delete=models.CASCADE)
    approval_date = models.DateField()

    class Meta:
        db_table = "tender"
