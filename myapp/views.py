from django.shortcuts import render,redirect

from django.views.generic import View

from myapp.forms import EmployeeForm

from myapp.models import Employee

from django.contrib import messages


# view=>view for creating new Employee
# methods:GET,POST
# url:lh:8000/employees/add


class EmployeeCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=EmployeeForm()

        return render(request,"employees_add.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Employee.objects.create(

                name=data.get("name"),

                designation=data.get("designation"),

                department=data.get("department"),

                salary=data.get("salary"),

                contact=data.get("contact"),

                address=data.get("address")
            )

            messages.success(request,"Employee has been added")

            return redirect("employee-list")
        
        else:

            messages.error(request,"Failed to add Employee")

            return render(request,"employees_add.html",{"form":form_instance})
    


class EmployeeListView(View):

    def get(self,request,*args,**kwargs):

        qs=Employee.objects.all()

        return render(request,"employees_list.html",{"employee":qs})
    

# employee detail View
# url:lh:8000/employee/<int:pk>/


class EmployeeDetailView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Employee.objects.get(id=id)

        return render(request,"employees_detail.html",{"employee":qs})

# employeedeleteview

class EmployeeDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Employee.objects.get(id=id).delete()

        messages.success(request,"Employee removed")

        return redirect("employee-list")
    


class EmployeeUpdateView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        emp_obj=Employee.objects.get(id=id)

        emp_dict={

            "name":emp_obj.name,
            "designation":emp_obj.designation,
            "department":emp_obj.department,
            "salary":emp_obj.salary,
            "contact":emp_obj.contact,
            "address":emp_obj.address
        }

            
        form_instance=EmployeeForm(initial=emp_dict)

        return render(request,"employee_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)

        id=kwargs.get("pk")

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            Employee.objects.filter(id=id).update(**data)

            return redirect("employee-list")
        
        else:

            return render(request,"employee_edit.html",{"form":form_instance})
        
        