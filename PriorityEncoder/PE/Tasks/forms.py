from django import forms

class AccountForm(forms.Form):
    username=forms.CharField(max_length=25)

class TaskForm(forms.Form):
    Description=forms.CharField(max_length=100)
    Type=forms.ChoiceField(choices=[('Curricular','Curricular'),('Co-Curricular','Co-Curricular'),('Extra-Curricular','Extra-Curricular'),('Personal','Personal')])
    Due_Date=forms.DateField(label="Due Date")
    #Weight=forms.IntegerField(label="Enter Importance on a scale of 1-10",max_value=10,min_value=0)


