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

![image](https://user-images.githubusercontent.com/56064985/148043499-5b75d824-cda8-4097-9e37-0e73b3164be9.png)


![image](https://user-images.githubusercontent.com/56064985/148043582-b0ea5fa1-2ffa-4455-956a-27c36eb08f7a.png)


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

