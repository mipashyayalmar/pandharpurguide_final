from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    heading = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.heading


from django.db import models

class Advertisement(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='advertisements/')
    order = models.PositiveIntegerField()
    is_google_adsense = models.BooleanField(default=False)
    position = models.CharField(
        max_length=50,
        choices=[
            ('upper-menu', 'Upper menu'),
            ('below-menu', 'Below menu'),
            ('left-side-of-page', 'Left side of the page'),
            ('right-side-of-page', 'Right side of the page'),
            ('below-page', 'Below the page'),
            ('below-footer', 'Below footer'),
        ],
        default='upper-menu'
    )
    status = models.CharField(
        max_length=10,
        choices=[('enable', 'Enable'), ('disable', 'Disable')],
        default='enable'
    )

    def __str__(self):
        return self.title