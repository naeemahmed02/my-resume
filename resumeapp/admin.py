from django.contrib import admin
from .models import (
    Resume,
    PersonalInfo,
    Education,
    Experience,
    Skill,
    Project,
    Social
)


# Inline Configurations

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1
    fields = ('title', 'institute', 'specialization', 'city', 'percentage_cgpa', 'start_date', 'end_date')
    ordering = ['-end_date']


class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1
    fields = ('company', 'position', 'city', 'currently_working', 'start_date', 'end_date')
    ordering = ['-start_date']


class SkillInline(admin.TabularInline):
    model = Skill
    extra = 1
    fields = ('name', 'proficiency')
    ordering = ['-proficiency']


class ProjectInline(admin.TabularInline):
    model = Project
    extra = 1
    fields = ('title', 'tech_stack', 'github_link', 'demo_link')
    ordering = ['title']


class SocialInline(admin.TabularInline):
    model = Social
    extra = 1
    fields = ('platform', 'link')
    ordering = ['platform']



@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)
    inlines = [EducationInline, ExperienceInline, SkillInline, ProjectInline, SocialInline]
    ordering = ['-created_at']


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'city', 'profession_title')
    search_fields = ('first_name', 'last_name', 'email', 'profession_title')
    list_filter = ('city',)
    ordering = ('first_name',)


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('title', 'institute', 'specialization', 'percentage_cgpa', 'start_date', 'end_date', 'resume')
    search_fields = ('title', 'institute', 'specialization')
    list_filter = ('city', 'institute')
    ordering = ['-end_date']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'city', 'currently_working', 'start_date', 'end_date', 'resume')
    search_fields = ('company', 'position')
    list_filter = ('currently_working', 'city')
    ordering = ['-start_date']


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'proficiency', 'resume')
    search_fields = ('name',)
    list_filter = ('proficiency',)
    ordering = ['-proficiency']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'github_link', 'demo_link', 'resume')
    search_fields = ('title', 'tech_stack')
    list_filter = ('tech_stack',)
    ordering = ['title']


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('platform', 'link', 'resume')
    search_fields = ('platform', 'link')
    ordering = ['platform']
