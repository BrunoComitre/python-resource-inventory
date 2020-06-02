from django.contrib import admin
from .models import Question, Choice


# Register your models here.

'''
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
'''

'''
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
'''

'''
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3
'''

'''
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
'''

'''
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
'''

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
