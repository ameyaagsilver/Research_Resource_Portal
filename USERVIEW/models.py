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

    # def __str__(self):
    #     return self.name


class committee(models.Model):
    committee_id = models.AutoField(primary_key=True, default=None)
    committee_name = models.CharField(max_length=100)

    class Meta:
        db_table = "committee"

    # def __str__(self):
    #     return self.name


class committee_members(models.Model):
    user_id = models.CharField(max_length=100, primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    emailID = models.EmailField(max_length=100)
    committee_id = models.ForeignKey(
        committee, on_delete=models.CASCADE, db_column="committee_id")

    # class Meta:
    #     db_table = "committee_members"


class resources(models.Model):
    resource_id = models.AutoField(primary_key=True, default=None)
    resource_name = models.CharField(max_length=250)
    OEM = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=50)
    department_name = models.CharField(max_length=100)
    unit_cost = models.IntegerField()
    location = models.CharField(max_length=250)
    purchase_date = models.DateField(null=True, blank=True)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to="hello/")
    about = models.CharField(max_length=1000)
    admin_id = models.ForeignKey(
        admins, on_delete=models.CASCADE, default="r0Fi0ITEUSMcLPxf2JXUxL3VNK03", db_column="admin_id")

    class Meta:
        db_table = "resources"

    # def __str__(self):
    #     return self.name


class test(models.Model):
    test_id = models.AutoField(primary_key=True, default=None)
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to="hello/")

    class Meta:
        db_table = "test"


class resource_logbook(models.Model):
    log_id = models.AutoField(primary_key=True, default=None)
    member_id = models.ForeignKey(
        users, on_delete=models.CASCADE, db_column="member_id")
    admin_id = models.ForeignKey(
        admins, on_delete=models.CASCADE, db_column="admin_id")
    resource_id = models.ForeignKey(
        resources, on_delete=models.CASCADE, db_column="resource_id")
    issue_date = models.DateField()
    return_date = models.DateField(null=True)

    class Meta:
        db_table = "resource_logbook"

    # def __str__(self):
    #     return self.name


class tender(models.Model):
    tender_id = models.AutoField(primary_key=True, default=None)
    OEM = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=50)
    unit_cost = models.IntegerField()
    resource_name = models.CharField(max_length=250)
    tender_issue_date = models.DateField()
    quantity = models.IntegerField()
    about = models.CharField(max_length=1000)
    admin_id = models.ForeignKey(
        admins, on_delete=models.CASCADE, db_column="admin_id")
    committee_id = models.ForeignKey(
        committee, on_delete=models.CASCADE, db_column="committee_id")
    approval_date = models.DateField()

    class Meta:
        db_table = "tender"

    # def __str__(self):
    #     return self.name
