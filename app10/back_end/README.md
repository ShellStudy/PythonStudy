# uv 초기화
```cmd
uv init
```

# uv 패키지 구성

```
ROOT/
├── fastapi[standard]
├── mariadb
└── python-multipart
```

### 1. FastAPI 추가
```cmd
uv add fastapi --extra standard
```

### 2. MariaDB 추가
```cmd
uv add mariadb
```

### 3. Form Data 추가
```cmd
uv add python-multipart
```

# 환경 변수 관리

```
app_config/
├── origins
├── conn_params
└── api_key
```

# 실행 명령어
```cmd
uv run fastapi dev
```