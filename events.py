import logging
import requests

log = logging.getLogger('submitter')

def submit(a):
    log.info('submiting %s', a)
    res = requests.get('http://google.com')
    return res.ok
