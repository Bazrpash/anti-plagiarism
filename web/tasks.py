import requests
from antiplagiarism.celery import app
from .models import Account


@app.task()
def new_user_signed(user_id):
    try:
        user_account = Account.objects.get(id=user_id)
    except (KeyError, Account.DoesNotExist):
        return

    token = '1236733329:AAHdQ0gnBSXdaWMBpYJQSCGCQS88807YUB0'
    chat_id = '-1001297837201'
    url_template = 'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
    url = url_template.format(
        token=token,
        chat_id=chat_id,
        text='امضای جدید از طرف {} {}'.format(
            'دکتر' if user_account.is_professor else 'دانشجو', 
            user_account.first_and_last_name,
        ),
    )
    requests.get(url)
