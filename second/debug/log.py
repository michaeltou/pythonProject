import logging as log

log.basicConfig(level=log.INFO, filename='app.log', format='%(asctime)s - %(levelname)s - %(message)s')


log.info('This is an info message')

log.warning('This is an warning message')
log.error('This is an error message')
