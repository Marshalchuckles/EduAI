from django.db import models

# Create your models here.


from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    is_educator = models.BooleanField(default=False)

class Quiz(models.Model):
    title = models.CharField(max_length=200)
    questions = models.TextField()  # JSON format for simplicity
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

class Performance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.IntegerField()
    feedback = models.TextField(blank=True)
