from django.db import models

# Create your models here.
friends = 'friends'
search = 'search'
advertisement = 'ad'
other = 'other'

OPTIONS = (
    (friends, 'Friends'),
    (search, 'Search Engine'),
    (advertisement, 'Advertisement'),
    (other, 'Other'),
)

class Newsletter(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    news = models.BooleanField(default=True)
    find = models.CharField(choices=OPTIONS, max_length=100, default=friends, null=True)
    message=models.TextField()
    def __str__(self):
        return '{} {} {} {}'.format(self.name, self.email, self.news, self.find)



