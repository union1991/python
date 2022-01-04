## Django 프로젝트

Django는 초기 설정에 주의가 필요합니다. project를 구성하는 코드를 자동 생성해야 하는데, 이 과정에서 데이터베이스 설정, Django 위한 옵션들, 어플리케이션을 위한 설정들과 같은 Django 인스턴스를 구성하는 수많은 설정들이 생성되기 때문입니다.


## Django 프로젝트 만들기

#### 1. startproject

```
$ django-admin startproject mysite
```

![image](https://user-images.githubusercontent.com/56064985/148037481-817adf43-67a8-4bd1-9559-779571978d97.png)


* manage.py: 커맨드라인의 유틸리티

* mysite/ : 프로젝트를 위한 실제 Python 패키지들이 저장

* mysite/__init__.py: Python으로 하여금 이 디렉토리를 패키지처럼 다루라고 알려주는 용도의 단순한 빈 파일 

* mysite/settings.py: 프로젝트의 환경 및 구성을 저장(settings에서 환경 설정이 어떻게 동작하는지 확인 가능)

* mysite/urls.py: project 의 URL 선언을 저장

* mysite/asgi.py: An entry-point for ASGI-compatible web servers to serve your project. See ASGI를 사용하여 배포하는 방법 for more details.

* mysite/wsgi.py: 프로젝트를 서비스하기 위한 WSGI 호환 웹 서버의 진입점


#### 2. 장고 설치

```
$ python3 -m pip install Django
$ python3
>>> import django
>>> print(django.get_version())
```
