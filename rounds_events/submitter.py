import logging
import voluptuous
import requests


__all__ = ['submit']
log = logging.getLogger('submitter')


def submit(a):
    voluptuous.Schema
    log.info('submiting %s', a)
    res = requests.get('http://google.com')
    return res.ok

