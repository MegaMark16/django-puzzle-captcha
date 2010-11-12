from django.contrib import admin
from test_app.models import Submission

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'submission_date')
    class Meta:
        model = Submission
        
    
admin.site.register(Submission, SubmissionAdmin)

