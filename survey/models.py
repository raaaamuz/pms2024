from django.db import models
import uuid

class Survey(models.Model):
    survey_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    researcher_in_charge = models.CharField(max_length=100)
    project_name = models.CharField(max_length=100)
    job_number = models.CharField(max_length=100)
    year = models.IntegerField()
    month = models.CharField(max_length=20)
    dp_or_scripting = models.CharField(max_length=20)
    scripting_in_charge = models.CharField(max_length=100, null=True, blank=True)
    dp_in_charge = models.CharField(max_length=100, null=True, blank=True)
    
    # Fields for each question response
    Q1 = models.CharField(max_length=255, null=True, blank=True)
    Q2 = models.CharField(max_length=255, null=True, blank=True)
    Q3 = models.CharField(max_length=255, null=True, blank=True)
    Q4 = models.CharField(max_length=255, null=True, blank=True)
    Q5 = models.CharField(max_length=255, null=True, blank=True)
    Q6 = models.CharField(max_length=255, null=True, blank=True)
    Q7 = models.CharField(max_length=255, null=True, blank=True)
    Q8 = models.TextField(null=True, blank=True)  # For open-ended responses, use TextField

    def __str__(self):
        return self.project_name
