from account.models import Student

def get_student_from_user(user):
    try:
        return Student.objects.get(user=user)
    except:
        return None
