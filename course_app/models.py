from django.db import models


class Category(models.Model):
    name = models.CharField("Category", max_length=150, unique=True)
    imgpath = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField("Name", max_length=100, unique=True)
    description = models.TextField("Description")
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    logo = models.CharField("logo", max_length=100, unique=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    phone = 'Phone'
    facebook = 'Facebook'
    email = 'Email'

    CONTACT_CHOISES = [
        (phone, 'Phone'),
        (facebook, 'Facebook'),
        (email, 'Email'),
    ]
    course = models.ForeignKey(Course, related_name='contacts', on_delete=models.CASCADE)
    content_type = models.CharField(choices=CONTACT_CHOISES, max_length=150)
    value = models.CharField(max_length=150, null=False)

    def __str__(self):
        return "{} {}".format(self.content_type, self.value)


class Branch(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=50, null=True)
    longitude = models.CharField(max_length=50, null=True)
    address = models.CharField(max_length=100, null=True, unique=True)

    def __str__(self):
        return self.course

