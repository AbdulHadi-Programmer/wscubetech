from django import forms

# A form is created by this class and forms.Form import "forms" from "Form" class
class UserForm(forms.Form):
    num1 = forms.CharField(label='Num 1', widget=forms.TextInput(attrs={'class':'form-control'})) # label change the field name  
    num2 = forms.CharField(label='Num 2', widget=forms.TextInput(attrs={'class':'form-control'}))
    num3 = forms.CharField(label='Value 3', required=False, widget=forms.TextInput(attrs={'class':'form-control'})) # Required False mean this field doesnot require any data
    num4 = forms.CharField(label='Value 4', required=False, widget=forms.TextInput(attrs={'class':'form-control'})) # TextInput take text input and it cover whole row 
    # Creating a widget with forms.textarea field and attribute is class form-control
    email = forms.EmailField()