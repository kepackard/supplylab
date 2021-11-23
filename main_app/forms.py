from django.forms import ModelForm
from .models import Classroom

# ========== Classroom Form ==========
class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = ('school_name', 'state', 'district', 'address', 'zipcode', 'grade', 'teacher_name', 'teacher_email', 'school_url', 'notes',)