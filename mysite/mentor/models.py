from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=123, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Why_Choose_Mentor(models.Model):
    title = models.CharField(max_length=123, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Courses(models.Model):
    title = models.CharField(max_length=123, blank=False, null=False)
    name = models.CharField(max_length=123, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    category = models.ForeignKey(Category, blank=False, null=True, on_delete=models.SET_NULL)
    image_title = models.ImageField(upload_to="images/", blank=False, null=False)
    image_name = models.ImageField(upload_to="images/", blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Trainers(models.Model):
    name = models.CharField(max_length=123, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    image = models.ImageField(upload_to="images/", blank=False, null=False)

    def __str__(self):
        return self.name


class Events(models.Model):
    name = models.CharField(max_length=123, blank=False, null=False)
    title = models.CharField(max_length=123, blank=False, null=False)
    image = models.ImageField(upload_to="images/", blank=False, null=False)


