from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['topic', 'languages_used', 'duration_weeks']
        labels = {
            'topic': 'Project Topic',
            'languages_used': 'Languages Used for the Project',
            'duration_weeks': 'Duration (Weeks)'
        }
