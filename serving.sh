source env/bin/activate
pkill gunicorn
sleep 5
gunicorn --daemon --workers 3 --bind unix:/home/dh_mwbawy/websocket/web.sock antiplagiarism.wsgi:application
