## Django 프로젝트

Django는 초기 설정에 주의가 필요합니다. project를 구성하는 코드를 자동 생성해야 하는데, 이 과정에서 데이터베이스 설정, Django 위한 옵션들, 어플리케이션을 위한 설정들과 같은 Django 인스턴스를 구성하는 수많은 설정들이 생성되기 때문입니다.

```
https://docs.djangoproject.com/
```

## Django 프로젝트 만들기

#### 1. startproject

```
$ django-admin startproject mysite
```

![image](https://user-images.githubusercontent.com/56064985/148037481-817adf43-67a8-4bd1-9559-779571978d97.png)


* ```manage.py``` : 커맨드라인의 유틸리티

* ```mysite/``` : 프로젝트를 위한 실제 Python 패키지들이 저장

* ```mysite/__init__.py```: Python으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일 

* ```mysite/settings.py```: 프로젝트의 환경 및 구성을 저장(settings에서 환경 설정이 어떻게 동작하는지 확인 가능)

* ```mysite/urls.py```: project 의 URL 선언을 저장

* ```mysite/asgi.py```: An entry-point for ASGI-compatible web servers to serve your project. See ASGI를 사용하여 배포하는 방법 for more details.

* ```mysite/wsgi.py```: 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점


#### 2. runserver

```
$ python3 manage.py runserver
```

![image](https://user-images.githubusercontent.com/56064985/148042103-e89dec0c-5cdc-4a7a-896a-2c8e32264b10.png)


### Error 발생 시

runserver 명령어 입력 시, ```django.core.exceptions.ImproperlyConfigured: SQLite 3.8.3 or later is required (found 3.7.17).``` 발생할 경우가 있습니다. 이는 django에서 요구하는 SQLite의 버전은 3.9.0 이상이지만, 설치되어 있는 SQLite 의 버전이 3.7.X 이기 때문에 이슈가 발생한 것으로 sqlite를 최신 버전으로 설치하여 이슈를 해결합니다.

![image](https://user-images.githubusercontent.com/56064985/148043797-1895193f-104d-47e1-b1ef-c31119f53b6e.png)

* sqlite3 최신 버전 설치

```
$ wget https://www.sqlite.org/2019/sqlite-autoconf-3280000.tar.gz
$ tar zxvf sqlite-autoconf-3280000.tar.gz
$ sudo yum -y install gcc
$ ./configure --prefix=/usr/local
$ make
$ sudo make install
```

* 컴파일 후 시스템 링크 라이브러리에 반영

```
$ sudo -i           // 관리자 계정에서만 echo 명령어 가능
# echo "/usr/local/lib" >> /etc/ld.so.conf
# /sbin/ldconfig
# exit
```

* 설치한 sqlite3 경로 설정

```
$ cd ~
$ vi .bashrc

#SQLITE3 Setting
export LD_LIBRARY_PATH=/usr/local/lib

:wq!

$ source .bashrc
```

* 참조 : https://ossian.tistory.com/109


#### 3. Creating the Polls app

#### 1) Polls 프로젝트 

```
$ python3 manage.py startapp polls
```

![image](https://user-images.githubusercontent.com/56064985/148711093-196efb09-ba03-49a7-825b-696e0ce2c7b0.png)


#### 2) View 작성

```
$ vi ~/mysite/polls/views.py

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
   
:wq!
```

![image](https://user-images.githubusercontent.com/56064985/148711630-3983b8b2-dfaa-45c4-bb69-0cd7c4cbfddf.png)


#### 3) urls.py 생성

View를 호출하려면, URL 매핑이 되어야 하며, 이를 위해서는 URLconf가 필요합니다.

polls 디렉토리에 URLconf를 생성하려면 urls.py를 생성해야 합니다.

```
$ vi ~/mysite/polls/urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]

:wq!
```

![image](https://user-images.githubusercontent.com/56064985/148720186-d29dd6d5-1648-4424-8b45-ba095e611737.png)


#### 4) polls.urls 생성

 polls.urls 모듈에서 루트 URLconf를 지정해야 합니다. 이에, mysite/urls.py 을 생성합니다.

```
$ vi ~/mysite/urls.py

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
]
```

![image](https://user-images.githubusercontent.com/56064985/148720204-bfdd0941-47a8-4217-9261-6db09c67cbfd.png)


#### 4. Access to APP

#### 1) Allowed Hosts 설정

해당 웹에는 허가된 Host만 접근이 가능합니다. 따라서, ```~/mysite/mysite/settings.py``` 파일에 Allowed Hosts에 접근 허용할 Host의 IP를 설정합니다.

```
$ vi ~/mysite/mysite/settings.py

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

ALLOWED_HOSTS = ['X.X.X.X','localhost','127.0.0.1', 'X.X.X.X']         // 삽입

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

:wq!
```

#### 2) Runserer

```
$ python3 ~/mysite/manage.py runserver 0.0.0.0:8000
```

![image](https://user-images.githubusercontent.com/56064985/148721194-ee3df84a-0c4f-486a-997d-cbaf60f72c16.png)


#### 3) Access Web App

![image](https://user-images.githubusercontent.com/56064985/148720681-c0827827-9035-4eb7-aa45-86381dfbe154.png)

