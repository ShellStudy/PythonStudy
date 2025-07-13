import os

origins = [
    "http://localhost",
    "http://localhost:80",
    "http://localhost:5500",
    "http://127.0.0.1",
    "http://127.0.0.1:80",
    "http://127.0.0.1:5500",
]

conn_params = {
    "user" : os.getenv('MARIADB_USER'),
    "password" : os.getenv('MARIADB_PASSWORD'),
    "host" : os.getenv('MARIADB_HOST'),
    "database" : os.getenv('MARIADB_DATABASE'),
    "port" : int(os.getenv('MARIADB_PORT'))
}

api_key = os.getenv('API_KEY')