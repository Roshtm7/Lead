from django.db import models

class Lead(models.Model):
    source=models.CharField(max_length=200)
    name=models.CharField(max_length=150)
    contact=models.CharField(max_length=50)
    course=models.CharField(max_length=150)

    status_option=(
        ("open","open"),
        ("in-progress","in-progress"),
        ("pending","pending"),
        ("closed","closed"),
    )

    status=models.CharField(max_length=200,choices=status_option,default="open")
    remarks=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name
        

