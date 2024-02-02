from django.db import models
from users.models import User


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class Course(models.Model):

    title = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    discount = models.PositiveIntegerField()

    image = models.ImageField(upload_to="courses/")

    short_content = models.CharField(max_length=200)
    content = models.TextField()

    buy_user = models.ManyToManyField(User, related_name="buy_course", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "course"
        verbose_name_plural = "courses"


class Lesson(models.Model):
 
    title = models.CharField(max_length=100)
    total_time = models.BigIntegerField()

    related_course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="course_part"
    )


class Lesson_video(models.Model):
    title = models.CharField(max_length=255)
    video_time = models.PositiveIntegerField()
    video = models.FileField(upload_to='media/lessons/')
    description = models.TextField()

    related_course = models.ForeignKey(
        Lesson, 
        on_delete=models.CASCADE)

class LessonUser(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    time_watched = models.IntegerField(default=0)  # 280  # seconds, Example: 5 min = 300 sec
    total_time = models.IntegerField(default=0)  # 300  # seconds, Example: 5 min = 300 sec

    def __str__(self):
        return f"{self.user} - {self.lesson}"

    def is_finished(self):
        return self.total_time * 0.9 <= self.time_watched

    @property
    def status(self):
        if self.is_finished():
            return "finished"
        if self.time_watched > 0:
            return "in_progress"
        return "not started"


class LessonUserWatched(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(LessonUser, on_delete=models.CASCADE)

    from_time = models.IntegerField(default=0)
    to_time = models.IntegerField(default=0)
    

class Comments(BaseModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    comment = models.CharField(max_length = 100)



