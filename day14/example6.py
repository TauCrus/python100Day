'''
发邮件
'''

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText


def main():
    # 请自行修改下面的邮件发送者和接收者
    # sender = 'wyxxx@163.com'
    sender = '123xxx333@qq.com'
    # receivers = ['123xxx333@qq.com']
    receivers = ['wyxxx@163.com']
    message = MIMEText('python入门到放弃.', 'plain', 'utf-8')
    message['From'] = Header('tx<123xxx333@qq.com>', 'utf-8')
    message['To'] = Header('wy<wyxxx@163.com>', 'utf-8')
    message['Subject'] = Header('Python 100 Day', 'utf-8')
    # smtper = SMTP('smtp.163.com')
    smtper = SMTP('smtp.qq.com')
    # 请自行修改下面的登录口令
    # smtper.login(sender, '密码')
    smtper.login(sender, '密码')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成!')


if __name__ == '__main__':
    main()
