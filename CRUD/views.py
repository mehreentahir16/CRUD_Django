from django.http import HttpResponse


def home(request):
    html = """
    <h1>Django CRUD Example</h1>
   
    <a href="/CRUD_FBVs/">Function Based Views</a><br> 
    <a href="/CRUD_CBVs/">Class Based Views</a>   
    """
    return HttpResponse(html)
