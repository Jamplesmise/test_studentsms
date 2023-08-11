from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    courses = models.ManyToManyField('Course', blank=True)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.student_name


class Teacher(models.Model):
    teacher_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.teacher_name

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='courses_taught')  # 自定义related_name
    start_date = models.DateField()
    end_date = models.DateField()
    classroom = models.CharField(max_length=50, default='')

    # ... other fields ...

    def __str__(self):
        return self.course_name

class Exam(models.Model):
    exam_name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    classroom = models.CharField(max_length=50)

    def __str__(self):
        return self.exam_name
