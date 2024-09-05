def index(request):
    search_field = request.GET.get('search')
    if search_field :
        users = User.objects.filter(pseudo__icontains=search_field)
        context = {
            'users': users,
            'search_field': search_field,
        }
    else:
        users = User.objects.all()
        numbers_users = users.count()
        context = {
            'users': users,
            'total': numbers_users,
        }
    return render(request, "user/list.html", context)
[<form method="GET">
            <input type="text" id="myInput" name="search" value="{{search_field}}" placeholder="Rechercher...">
            <button onclick=""> Rechercher</button>
        </form>
def index(request):
    search_field = request.GET.get('search')
    if search_field:
        students = StudentModel.objects.filter(last_name__icontains=search_field)
        today = datetime.now().year
        context = {
            'students' : students,
            'today': today,
        }
    else:
        students = StudentModel.objects.filter(status=True)
        today = datetime.now().year

        context = {
            'students': students,
            'today': today,
        }
    return render(request, "student/list.html", context)