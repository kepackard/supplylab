from django.forms import ModelForm
from .models import Classroom, Item

# ========== CLASSROOM Form ==========
class ClassroomForm(ModelForm):
    class Meta:
        model = Classroom
        fields = (
            'school_name', 
            'state', 
            'district', 
            'address', 
            'zipcode', 
            'grade', 
            'teacher_name', 
            'teacher_email', 
            'school_url', 
            'notes',
        )

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = (
            'name',
            'amount',
            'thumbnail',
            'notes',
        )