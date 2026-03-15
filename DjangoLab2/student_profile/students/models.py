from django.db import models


class Student(models.Model):

    COURSE_CHOICES = [
        ('BCA', 'BCA'),
        ('BSc', 'BSc'),
        ('BTech', 'BTech'),
        ('MCA', 'MCA'),
        ('MBA', 'MBA'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    course = models.CharField(max_length=20, choices=COURSE_CHOICES)
    enrollment_date = models.DateField(auto_now_add=True)

    # Optional profile image (for future admin preview feature)
    profile_image = models.ImageField(
        upload_to='students/',
        blank=True,
        null=True
    )

    slug = models.SlugField(unique=True, blank=True, null=True)


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-enrollment_date']
        verbose_name = "Student"
        verbose_name_plural = "Students"
