try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('sentry-dingding-rebot').version
except Exception, e:
    VERSION = 'unknown'