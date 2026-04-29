from django.db import models #django가 가진 모듈(기능) 가져오기

class Burger(models.Model): #햄버거를 나타내는 Model 클래스 정의 시작
    name = models.CharField(max_length=20)    #문자열을 저장하는 CharField
    price = models.IntegerField(default=0)    #숫자를 저장하는 IntegerField
    calories = models.IntegerField(default=0) #숫자를 저장하는 IntegerField

    def __str__(self):
        return self.name