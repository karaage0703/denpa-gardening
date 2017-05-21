#!/usr/bin/env python
# -*- coding: utf-8 -*-

# send mail utf-8 using gmail smtp server /w jpegs

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

from email.Header import Header
from email.Utils import formatdate
import smtplib

def send_email_with_jpeg(from_addr, to_addr, subject, body, jpegs=[], server='smtp.gmail.com', port=587):
    encoding='utf-8'
    msg = MIMEMultipart()
    mt = MIMEText(body.encode(encoding), 'plain', encoding)

    if jpegs:
        for fn in jpegs:
            img = open(fn, 'rb').read()
            mj = MIMEImage(img, 'jpeg', filename=fn)
            mj.add_header("Content-Disposition", "attachment", filename=fn)
            msg.attach(mj)
        msg.attach(mt)
    else:
        msg = mt

    msg['Subject'] = Header(subject, encoding)
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Date'] = formatdate()

    _user = "xxxx@gmail.com"
    _pass = "xxxxxxxxxxxxxxxxxxxx"

    smtp = smtplib.SMTP(server, port)
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(_user, _pass)
    smtp.sendmail(from_addr, [to_addr], msg.as_string())
    smtp.close()

###
if __name__ == '__main__':
    body = u'\n%s\n' % (u'写真')
    js = ['test.jpeg']
    send_email_with_jpeg('xxxx@gmail.com', 'xxxx@blog.hatena.ne.jp', u'今日の家庭菜園', body, js)
