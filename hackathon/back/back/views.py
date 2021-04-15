from django.http import JsonResponse
from django.http import HttpResponse
from . import diabetes
from . import heart
def dia(request,name,gluc,bp,tri,ins,bmi):
    """ test for diabetes"""
    my_dict = {"B":float(gluc), "C":float(bp),"D":float(tri), "E":float(ins), "F": float(bmi)}
    output = diabetes.check_input(my_dict)
    if output==0:
        r={"result":"Diagnosis suggests that patient does not suffers from diabetes."}
    else:
        r={"result":"Our diagnosis suggests patient does suffer from diabetes.\nPlease get checked soon."}
    response=JsonResponse(r)
    response['Access-Control-Allow-Origin'] = '*'
    return response
def hea(request,age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    l=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    print("list",l)
    output=heart.heart(l)
    if output==0:
        r={"result":"Diagnosis suggests that patient does not suffers from Heart-Disease."}
    else:
        r={"result":"Our diagnosis suggests patient does suffer from Heart-Disease.\nPlease get checked soon."}
    print(r["result"])
    response=JsonResponse(r)
    response['Access-Control-Allow-Origin'] = '*'
    return response
def get(request):
    print("gottem")
    r={'yee':'ad'}
    return JsonResponse(r,safe=False)