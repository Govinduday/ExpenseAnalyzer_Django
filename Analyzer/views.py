from django.shortcuts import render
from django.http import HttpResponse
from Analyzer.models import user_profile, general_expenses, mandatory_expenses, debts
import array
# Create your views here.

def dashboard(request):
    return render(request,'examples/dashboard.html')

def user(request):
    
    return render(request,'examples/user.html')

def summary(request):
    
    Date_spentodrer=general_expenses.objects.order_by('date_spent')
    Amount_order=general_expenses.objects.order_by('amount')
    Category_order=general_expenses.objects.order_by('category')
    total= [0, 0, 0, 0, 0, 0,0,0,0,0]
    for i in range(0,9):
        for data in Category_order :
            if data.category==i:
                 total[i]=total[i]+data.amount  
            
    summar_dict={'Date':Date_spentodrer,'amount':Amount_order,'category':Category_order,'total':total}
    return render(request,'examples/summary.html',context=summar_dict)

def debts(request):
    return render(request,'examples/debts.html')

def mandatory(request):
    return render(request,'examples/mandatory.html')

def analyze(request):
    return render(request,'examples/analyze.html')

def notification(request):
    return render(request,'examples/notification.html')

def addExpense(request):
    return render(request,'examples/AddExpense.html')

def addMoney(request):
    return render(request,'examples/AddMoney.html')



    
 