from django.db import models


class Category(models.Model):
    name = models.CharField("Category", max_length=150)
    imgpath = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Branch(models.Model):
    latitude = 42.8667
    longitude = 74.566742
    address = 'Бишкек, Байтик баатыра 70'
    BRANCH_CHOISES = [
        (latitude, 'Latitude'),
        (longitude, 'Longitude'),
        (address, 'Address'),
    ]

    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

    def __str__(self):
        return self.address


class Contact(models.Model):

    phone = 996709202111
    facebook = 'www.facebook.com'
    email = 'course@gmail.com'
    CONTACT_CHOISES = [
        (phone, 'Phone'),
        (facebook, 'Facebook'),
        (email, 'Email'),
    ]

    def __str__(self):
        return self.phone


class Course(models.Model):

    name = models.CharField("Name", max_length=100)
    description = models.TextField("Description")
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    logo = models.CharField("logo", max_length=100)
    contacts = models.CharField(max_length=50,
                                choices=Contact.CONTACT_CHOISES,
                                default=Contact.phone)
    branches = models.CharField(max_length=300,
                                choices=Branch.BRANCH_CHOISES,
                                default=Branch.address)

    def __str__(self):
        return self.name
