## Database Setup

Django의 기본적으로 Database 구성은 SQLite를 사용합니다. SQLite는 Python에 포함되어 있으므로 데이터베이스를 지원하기 위해 별도의 설치가 필요 없습니다. 만약, 다른 Database를 사용하려면 Database 바인등을 설치하고, 연결 설정을 변경합니다.

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

```
$ python3 manage.py migrate
```


[변경 사항이 없을 경우는 하기의 이미지와 같습니다.]

![image](https://user-images.githubusercontent.com/56064985/148888976-92911a77-22c7-4223-aebf-1fc5d4e2dca4.png)



#### 3. Playing with the API

쉘 진입 후, Database API를 확인 할 수 있습니다.

```
$ python3 manage.py shell

>>> from polls.models import Choice, Question  # Import the model classes we just wrote.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())
>>> q.save()
>>> q.id
>>> q.question_text
>>> q.pub_date
>>> q.question_text = "What's up?"
>>> q.save()
>>> Question.objects.all()
```



#### 1) polls/models.py 수정

```
$ vi ~/mysite/mysite/polls/models.py

from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

# 삽입
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    chice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


# 삽입
    def __str__(self):
        return self.choice_text

:wq!
```

![image](https://user-images.githubusercontent.com/56064985/148891856-dfece4f9-0285-45f7-92c5-630afd11a9f0.png)



