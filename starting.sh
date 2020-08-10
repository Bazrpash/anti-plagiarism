# this script should be run if server has been restarted

/home/dh_mwbawy/redis/redis-stable/src/redis-server --daemonize yes
source env/bin/activate
pkill gunicorn
sleep 5
celery multi stop worker
sleep 5
gunicorn --daemon --workers 3 --bind unix:/home/dh_mwbawy/websocket/web.sock antiplagiarism.wsgi:application
celery multi start worker -A antiplagiarism -B -Q mail_queue,celery --concurrency=2
