import multiprocessing


workers = multiprocessing.cpu_count() // 2
# workers = 8
threads = workers * 2
# bind = 'unix:apiagro.sock'
bind = '0.0.0.0:8000'
worker_class = 'uvicorn.workers.UvicornWorker'
# worker_connections = 1000
# keepalive = 2
# umask = 0o007
timeout = 600


#logging
accesslog = 'logs/access.log'
errorlog = 'logs/err.log'
capture_output = True
log_level = "debug"
loglevel = "debug"
access_log_format = '%({X-Real-IP}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" '
# certificate = 'ssl/cer.crt'
# keyfile = 'ssl/cer.key'
