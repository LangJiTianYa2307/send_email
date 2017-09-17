from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header

#qq邮箱smtp服务器
host_server = 'smtp.qq.com'
#发送方qq和授权码
sender_qq = '979972717'
sender_password = 'ojyxuilmvlovbeje'

# 邮件内容
mail_content ="hello!"
# 邮件标题
mail_title = "hello"

#发送方的qq邮箱
sender_qq_mail = '979972717@qq.com'

#接受方的qq邮箱
receiver_google_mail = 'huzhenglang@gmail.com'

#ssl登陆
smtp = SMTP_SSL(host_server)
smtp.set_debuglevel(1)
smtp.ehlo(host_server)
smtp.login(sender_qq,sender_password)

msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = sender_qq_mail
msg["To"] = receiver_google_mail
smtp.sendmail(sender_qq_mail,receiver_google_mail,msg.as_string())
smtp.quit()


