from django.contrib import admin

from course import models
# Register your models here.


admin.site.register(models.Course)
admin.site.register(models.Lesson_video)
admin.site.register(models.Lesson)
admin.site.register(models.LessonUser)
admin.site.register(models.LessonUserWatched)