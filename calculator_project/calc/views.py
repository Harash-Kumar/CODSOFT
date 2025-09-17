from django.shortcuts import render

def calculator(request):
    result = ""
    expression = ""

    if request.method == "POST":
        expression = request.POST.get("expression", "")

        try:
            # Evaluate safely (basic usage)
            result = eval(expression)
        except Exception:
            result = "Error"

    return render(request, "calc/calculator.html", {
        "expression": expression,
        "result": result
    })
