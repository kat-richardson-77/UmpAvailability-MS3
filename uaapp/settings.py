import psycopg2
conn = psycopg2.connect(host="localhost", dbname="postgres", user="postgres"
                      password="catykins1977!", port=5432)

cur = conn.cursor()

# cur.execute("""SELECT * FROM clubmembers, umpires where enid=[] and surname=[] and password=[];""")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp',  # Your app
]

DEBUG = False
ALLOWED_HOSTS = ['.herokuapp.com']