# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
#
# _user = "2412672282@qq.com"
# _pwd = "afjj494199078"
# _to = "494199078@qq.com"
#
# # 如名字所示Multipart就是分多个部分
# msg = MIMEMultipart()
# msg["Subject"] = "don't panic"
# msg["From"] = _user
# msg["To"] = _to
#
# # ---这是文字部分---
# part = MIMEText("乔装打扮，不择手段")
# msg.attach(part)
#
# # ---这是附件部分---
# # xlsx类型附件
# # part = MIMEApplication(open(r'D:\all_case\log.html', 'rb').read())
# # part.add_header('Content-Disposition', 'attachment', filename="log.html")
# # msg.attach(part)
#
# # jpg类型附件
# # part = MIMEApplication(open(r'D:\all_case\report.html', 'rb').read())
# # part.add_header('Content-Disposition', 'attachment', filename="report.jpg")
# # msg.attach(part)
#
# # # pdf类型附件
# # part = MIMEApplication(open('foo.pdf', 'rb').read())
# # part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
# # msg.attach(part)
# #
# # # mp3类型附件
# # part = MIMEApplication(open('foo.mp3', 'rb').read())
# # part.add_header('Content-Disposition', 'attachment', filename="foo.mp3")
# # msg.attach(part)
#
# s = smtplib.SMTP("smtp.qq.com", timeout=30)  # 连接smtp邮件服务器,端口默认是25
# s.login(_user, _pwd)  # 登陆服务器
# s.sendmail(_user, _to, msg.as_string())  # 发送邮件
# s.close()