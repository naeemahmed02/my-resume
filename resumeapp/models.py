from django.db import models
from django.core.exceptions import ValidationError


class Resume(models.Model):
    title = models.CharField(max_length=200, help_text="Resume title (e.g., AI Engineer Portfolio)")
    summary = models.TextField(blank=True, help_text="Short professional summary or bio")
    resume_pdf = models.FileField(upload_to='resumes/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Resumes"
        ordering = ['-created_at']


class PersonalInfo(models.Model):
    resume = models.OneToOneField(Resume, on_delete=models.CASCADE, related_name="personal_info")
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=120)
    profile_image = models.ImageField(upload_to='profile/', default='/profile/profile.avif', null=True, blank=True)
    profession_title = models.CharField(max_length=150, help_text="e.g., AI Engineer | Computer Vision Specialist")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name_plural = "Personal Info"



class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='education')
    title = models.CharField(max_length=200, help_text="Degree or Certification name")
    institute = models.CharField(max_length=200)
    specialization = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200)
    percentage_cgpa = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Percentage/CGPA")
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.title} - {self.institute}"

    class Meta:
        verbose_name_plural = "Education"
        ordering = ['-end_date']



class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experience')
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    currently_working = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)

    def clean(self):
        if self.currently_working and self.end_date:
            raise ValidationError("End date should be empty if currently working.")

    def __str__(self):
        return f"{self.position} at {self.company}"

    class Meta:
        verbose_name_plural = "Experience"
        ordering = ['-start_date']



class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(default=0, help_text="Skill level 0–100")

    def __str__(self):
        return f"{self.name} ({self.proficiency}%)"

    class Meta:
        verbose_name_plural = "Skills"
        ordering = ['-proficiency']



class Project(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=300, help_text="Comma-separated technologies used")
    github_link = models.URLField(null=True, blank=True)
    demo_link = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to='projects/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Projects"
        ordering = ['title']



class Social(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='socials')
    platform = models.CharField(max_length=100)
    link = models.URLField(max_length=300)

    def __str__(self):
        return f"{self.platform}: {self.link}"

    class Meta:
        verbose_name_plural = "Social Links"
