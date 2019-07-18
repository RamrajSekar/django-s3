AWS_ACCESS_KEY_ID = "ae0-reliability-appengineplatform-u3"
AWS_SECRET_ACCESS_KEY = "l9CXod2h+cIBCdaacZn9Plaxa9r68GXOy2Z3wrwH"
AWS_STORAGE_BUCKET_NAME = "ae0-reliability-appengineplatform-qa-1"
AWS_S3_ENDPOINT_URL = "https://ecsams.bnymellon.net:9021"
AWS_AUTO_CREATE_BUCKET = True
AWS_QUERYSTRING_AUTH = False
S3_BROWSER_SETTINGS = "djangoS3Browser"
TEMPLATES = [{ 'OPTIONS': {'libraries': {'s3-load': 'djangoS3Browser.templatetags.s3-tags',},}}]
SECRET_KEY = 'y130-j9oz4r5aoamn_n=+s-*7n)*3^s$jmf4(qw6ik28()g^(n'
DEBUG = True
ALLOWED_HOSTS = ['*']
ROOT_URLCONF= 'djangoS3Browser.s3_browser.urls'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
STATIC_URL = '{}/static/'.format(AWS_S3_ENDPOINT_URL)
STATIC_ROOT = '/static/'