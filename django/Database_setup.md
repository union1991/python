## Database Setup

Django는 기본적으로 SQLite Database를 사용합니다. SQLite는 Python에 포함되어 있어 별도의 설치 과정이 필요 없습니다. 만약, 다른 Database를 사용하려면 Database 바인 등을 설치하고, 연결 설정을 변경합니다.

```
ENGINE – Either 'django.db.backends.sqlite3', 
'django.db.backends.postgresql', 'django.db.backends.mysql', or 
'django.db.backends.oracle'. Other backends are also available.
```

* ```SQLite 사용 시``` : BASE_DIR / 'db.sqlite3' 에서 설정을 확인할 수 있습니다.

* ```타 데이터베이스 사용 시``` : Host에 별도의 User, PASSWORD 및 추가 설정이 필요합니다. 


#### 1. Database 테이블 생성

migrate명령은 INSTALLED_APPS설정을 살펴보고 mysite/settings.py파일 의 데이터베이스 설정 과 앱과 함께 제공되는 데이터베이스 마이그레이션에 따라 필요한 Database 테이블을 생성합니다 

```
$ python3 manage.py migrate
```

![image](https://user-images.githubusercontent.com/56064985/148726508-af911334-a3b6-4fdc-aeaa-2446fafddb83.png)


#### 2. Model 생성

추가 메타데이터를 사용하여 기본적으로 데이터베이스 레이아웃인 모델을 정의합니다.

설문조사 앱에서 ```Question``` 및 ```Choice```의 두 가지 모델을 만듭니다. ```Question```에게 질문과 발행일을, ```Choice```에는 선택 텍스트와 투표 집계라는 두 개의 필드가 있습니다. 

```
$ vi ~/mysite/polls/models.py

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
:wq!
```

![image](https://user-images.githubusercontent.com/56064985/148727597-85e2fb36-a050-4aba-b14e-324f65e400ec.png)



#### 3. Model 활성화

다음은 모델을 생성하는 과정입니다. 모델이란 부가적인 메타데이터를 가진 데이터베이스의 구조(layout)를 말합니다. 해당 과정에서는 ```Question``` 과 ```Choice``` 라는 두 개의 모델을 생성합니다.

프로젝트에 앱을 포함하려면 INSTALLED_APPS설정 에서 구성 클래스에 대한 참조를 추가해야 합니다. PollsConfig클래스에 polls/apps.py의 경로가 있으므로, 파일 'polls.apps.PollsConfig'. mysite/settings.py파일을 편집하고 해당 경로를 INSTALLED_APPS설정에 추가 합니다.

#### 1) settings.py 설정 삽입

```
$ vi ~/mysite/mysite/settings.py

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

ALLOWED_HOSTS = ['172.16.100.48','localhost','127.0.0.1', '172.16.101.185']

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 삽입
INSTALLED_APPS = [                                           
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

:wq!
```

#### 2) polls 포함 확인

```
$ python3 manage.py makemigrations polls
```

![image](https://user-images.githubusercontent.com/56064985/148728880-e0d33e8c-e798-421a-bd17-c190d3931694.png)



#### 3) 마이그레이션  실행(데이터베이스 스키마 동기화)


데이터베이스 테이블 생성합니다.


```
$ python3 manage.py migrate
```


[변경 사항이 없을 경우는 하기의 이미지와 같습니다.]

![image](https://user-images.githubusercontent.com/56064985/148888976-92911a77-22c7-4223-aebf-1fc5d4e2dca4.png)



#### 3. Playing with the API

쉘 진입 후, Database API를 확인 할 수 있습니다.

```
$ python3 manage.py shell
>>> from polls.models import Choice, Question                   #Import the model classes we just wrote
>>> Question.objects.all()                  # Create a new Question.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()                    # Save the object into the database. You have to call save() explicitly.
>>> q.id                        # Now it has an ID
1
>>> q.question_text         # 확인
"What's new?"
>>> q.pub_date              # 만들어지 시간으로 추측
>>> q.question_text = "What's up?"              # q 값 변경
>>> q.save()                    # 변경 사항 저장하기
>>> Question.objects.all()                  # 모든 값 확인하기
<QuerySet [<Question: What's up?>]>
```



#### 1) polls/models.py 수정


```
$ vi ~/mysite/mysite/polls/models.py

import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

# 삽입
    def __str__(self):
        return self.question_text
# 삽입(커스텀 메소드)
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


# 삽입
    def __str__(self):
        return self.choice_text

:wq!
```

![image](https://user-images.githubusercontent.com/56064985/148891856-dfece4f9-0285-45f7-92c5-630afd11a9f0.png)


#### 2) 변경 사항 확인

```
$ python3 manage.py shell

>>> from polls.models import Choice, Question                   #Import the model classes we just wrote

# 검색 방법(ID)
>>> Question.objects.filter(id=1)              
<QuerySet [<Question: What's up?>]>

# 검색 방법(starts with)
>>> Question.objects.filter(question_text__startswith='What')               
<QuerySet [<Question: What's up?>]>

# 타임존 설정
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Primary Key로 검색 찾기
>>> Question.objects.get(pk=1)
<Question: What's up?>

# 앞서 생성한 커스텀 메소드 동작 확인
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# 선택 사항 생성(3개)
>>> q = Question.objects.get(pk=1)

>>> q.choice_set.all()
<QuerySet []>

>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)


>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
>>> c.delete()

```






