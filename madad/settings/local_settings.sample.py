# local settings for configuration that should not be checked into git
#
# NOTE importing variables into this file can change their values! this file
# can already access everything declared in base.py without imports.

DEBUG = True


# SECURITY WARNING: keep the secret key used in production secret!
# Make these unique, and don't share them with anybody.
# Generate from here https://randomkeygen.com/django-secret-key or similar
SECRET_KEY = ""

# configure & override database setting as needed; must set a password
DATABASES["default"]["PASSWORD"] = ""

# override default solr configuration as needed
# SOLR_CONNECTIONS['default']['URL'] = ''      # default http://localhost:8983/solr/
# SOLR_CONNECTIONS['default']['COLLECTION'] = ''  # default cdh_madad
# SOLR_CONNECTIONS['default']['CONFIGSET'] = ''   # default geniza
