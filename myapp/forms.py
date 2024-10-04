from django import forms

class EmployeeForm(forms.Form):

    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    designation=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    department=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))

    salary=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    contact=forms.IntegerField(widget=forms.NumberInput(attrs={"class":"form-control mb-3"}))

    address=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-3"}))


    def clean(self):

        cleaned_data=super().clean()
        salary=cleaned_data.get("salary")

        if salary not in range(15000,100000):

            error_msg="salary must be in between 15k and 1 Lakh"

            self.add_error("salary",error_msg)

