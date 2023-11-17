from django import forms
from .models import Topic,Entry
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=['name','image']
        labels={'name':''}
class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields=['name']
        labels={'name':'Entry:'}
        widgets={'name':forms.Textarea(attrs={'cols':80})}        