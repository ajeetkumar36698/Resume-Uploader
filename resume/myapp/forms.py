from django import forms
from .models import Resume
gender_choice=[
    ('male','male'),
    ('Female','Female')
]
job_city_choice=[
    ('Delhi','Delhi'),
    ('Pune','Pune'),
    ('Ranchi','Ranchi'),
    ('Mumbai','Mumbai'),
    ('Dhanbad','Dhanbad'),
    ('Banglore','Banglore')
]
class ResumeForm(forms.ModelForm):
    gender=forms.ChoiceField(choices=gender_choice,widget=forms.RadioSelect)
    job_city=forms.MultipleChoiceField(label="Preferred Job Location",choices=job_city_choice,widget=forms.CheckboxSelectMultiple())
    class Meta:
        model=Resume
        fields=["id","name","dob","gender",'city','pin','state','mobile','city','email','job_city','profile_image','my_file']
        labels={'name':'Full Name','dob':'Date of Birth',
        'pin':'Pin Code','Mobile':'Mobile No',
        'profile_image':'Profile Image','my_file':'Document'}
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control'}),
            'locality':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
            'pin':forms.NumberInput(attrs={'class':'form-control'}),
            'state':forms.Select(attrs={'class':'form-control'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }