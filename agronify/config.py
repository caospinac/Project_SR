# //
PRODUCTION = False

if PRODUCTION:
    import os
    PORT = int(os.environ['PORT'])
else:
    PORT = 8000

server = {
    'HOST': '0.0.0.0',
    'PORT': PORT,
    'DEBUG': True,
}

database = {
    'DB_CLIENT': 'sqlite',
    'DB_TEST_CLIENT': 'sqlite',
    'DB_USER': 'postgres',
    'DB_PASSWORD': 'pgsql',
    'DB_PORT': 5432,
    'DB_HOST': 'localhost',
    'DB_NAME': 'database.sqlite',
    'DB_TEST_NAME': 'test.sqlite',
    'SQL_DEBUG': not PRODUCTION,
}
