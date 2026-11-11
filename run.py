def update_umpires():

def update_clubs():

def update_matches():

def update_confirmations():

def create_umpires():

def create_clubs():

def create_matches():

def create_confirmations():

def login():
    conn = psycopg2.connect(
        host="localhost",
        database='umpavailability',
        user='postgres',
        password='catykins1977!',
        port='5432'
        
    