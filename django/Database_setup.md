## Database Setup

Django의 기본적으로 Database 구성은 SQLite를 사용합니다. SQLite는 Python에 포함되어 있으므로 데이터베이스를 지원하기 위해 별도의 설치가 필요 없습니다. 만약, 다른 Database를 사용하려면 Database 바인등을 설치하고, 연결 설정을 변경합니다.

```
ENGINE – Either 'django.db.backends.sqlite3', 
'django.db.backends.postgresql', 'django.db.backends.mysql', or 
'django.db.backends.oracle'. Other backends are also available.
```

* SQLite 사용 시 : BASE_DIR / 'db.sqlite3' 에서 설정을 확인할 수 있습니다.

* 타 데이터베이스 사용 시 : Host에 별도의 User, PASSWORD 및 추가 설정이 필요합니다. 
