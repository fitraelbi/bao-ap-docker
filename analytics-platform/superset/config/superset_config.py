# Number of worker threads
SUPERSET_WORKERS = 4

# Gunicorn server port
SUPERSET_WEBSERVER_PORT = 8089

# Enable logging to file
ENABLE_TIME_ROTATE = True

# Encryption key
SECRET_KEY = 'change-me'

# SuperSet PostgreSQL metadata database connection
SQLALCHEMY_DATABASE_URI = 'postgresql://bao:analytics-platform@ap-db/superset'

# Caching with Redis
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 3600,
    'CACHE_KEY_PREFIX': 'superset_results',
    'CACHE_REDIS_URL': 'redis://redis:6379/3',
}

# Flask-WTF flag for CSRF
WTF_CSRF_ENABLED = False
TALISMAN_ENABLED = False
CSRF_ENABLED = False

# Add endpoints that need to be exempt from CSRF protection
WTF_CSRF_EXEMPT_LIST = []

# A CSRF token that expires in 1 year
WTF_CSRF_TIME_LIMIT = 60 * 60 * 24 * 365

# Set this API key to enable Mapbox visualizations
MAPBOX_API_KEY = ''

# Enable CORS to allow embedded dashboards
ENABLE_CORS = True
ALLOW_ORIGINS = ['https://analyticsplatform.services', 'https://hmis-apache-superset.xyz']
CORS_OPTIONS = {
    'supports_credentials': True,
    'allow_headers': ['*'],
    'resources':['*'],
    'origins': ALLOW_ORIGINS
}

# Disable CSP due to bug in Superset
TALISMAN_ENABLED = False

# Enable proxy headers to support nginx
ENABLE_PROXY_FIX = True

# Enable embedded dashboards
FEATURE_FLAGS = {
    "EMBEDDED_SUPERSET": True,
    "DASHBOARD_RBAC": True,
    "EMBEDDABLE_CHARTS": True
}

# Dashboard embedding
GUEST_ROLE_NAME = "Gamma"
