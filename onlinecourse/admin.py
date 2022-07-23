from django.contrib import admin
# <HINT> Import any new Models here
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission



class QuestionInline(admin.StackedInline):
    model = Question
    extra = 1

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1

# Register your models here.
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline,QuestionInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('question_text', 'grade_point', 'difficulty_level')

# Will need to look more deeply into nested inlines. This doesn't seem to nest in the intuitive way I would have expected
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)


# class LessonInline(admin.StackedInline):
#     model = Lesson
#     extra = 3