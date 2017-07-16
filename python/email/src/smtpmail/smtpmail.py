'''
Created on 2017年5月1日

@author: lleo
'''
import email.mime.multipart
import email.mime.text
import email.header
import smtplib
from smtplib import SMTPException

def sendsmtpmail():
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = 'll_501@163.com'
    msg['to'] = 'll_501@163.com'
    msg['subject'] = 'test'
    content = '''
                                你好，
                                        这是一封自动发送的邮件。
                            
                                    www.beibei.com
                        '''
    txt = email.mime.text.MIMEText(content)
    msg.attach(txt)
    
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com', '25')
    smtp.login('ll_501@163.com', '860501 ')
    smtp.sendmail('ll_501@163.com', 'll_501@163.com', str(msg))
    smtp.quit()
    
class SmtpMail(object):
    '''
    classdocs
    '''
   
    def __init__(self, server=None, port=None, user=None, passwd=None):
        if server is None:
            self._mail_smtp_server = 'smtp.163.com'
        if port is None:
            self._mail_smtp_port = '25'
        if user is None:
            self._mail_user_name = 'll_501@163.com'
        if passwd is None:
            self._mail_user_passwd = '860501 '
        
    def sendmail(self, mail_to, subject, body):
        msg = email.mime.multipart.MIMEMultipart()
        msg['From'] = self._mail_user_name
        msg['To'] = mail_to
        msg['Subject'] = email.header.Header(subject, 'utf-8')
#         msg['body'] = body
        content = '''i love you        '''
        txt = email.mime.text.MIMEText(content)
        msg.attach(txt)
        print('msg:' + str(msg))
        smtp = smtplib.SMTP()
        try:
            smtp.connect(self._mail_smtp_server, self._mail_smtp_port)
            smtp.login(self._mail_user_name, self._mail_user_passwd)
            print(mail_to)
            smtp.sendmail(self._mail_user_name, mail_to, msg.as_string())
        except SMTPException as e:
            print('sendmail err...')
            print(e)
        finally:
            smtp.quit()
        
# sendsmtpmail()

sm = SmtpMail()
# sm.sendmail('ll_501@163.com', 'i love you', 'Beibei')
# sm.sendmail('beibei2006hd@163.com', 'i love you', 'Beibei')
sm.sendmail('ll_501@126.com', 'i love you', 'Beibei')
