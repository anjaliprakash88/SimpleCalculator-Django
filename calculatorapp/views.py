from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    c = ''
    if request.method == "POST":
        n1 = float(request.POST.get('num1'))
        n2 = float(request.POST.get('num2'))
        oper = request.POST.get('opr')
        if oper == "+":
            c = n1 + n2
        elif oper == "-":
            c = n1 - n2
        elif oper == "*":
            c = n1 * n2
        elif oper == "/":
            if n2 == 0:
                c = "Division by zero is not allowed"
            else:
                c = n1 / n2
        else:
            return HttpResponse("invaild")
    return render(request, 'calculator.html', {'c': c})
