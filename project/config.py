# //
PRODUCTION = False

# Server
HOST = '0.0.0.0'
if PRODUCTION:
    import os
    PORT = int(os.environ['PORT'])
else:
    PORT = 8000
DEBUG = not PRODUCTION

# Database
DB_CLIENT = 'sqlite'
DB_TEST_CLIENT = 'sqlite'
DB_USER = 'postgres'
DB_PASSWORD = 'pgsql'
DB_PORT = 5432
DB_HOST = 'localhost'
DB_NAME = 'database.sqlite'
DB_TEST_NAME = 'test.sqlite'
SQL_DEBUG = not PRODUCTION
