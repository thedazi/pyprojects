# import smtplib
# import ssl

# my_email = 'Donotreplydazbot@gmail.com'
# ps = 'awlyatnjagmrmqql'

# smtp_server = "smtp.gmail.com"
# smtp_port = 587
# connection = smtplib.SMTP(smtp_server,smtp_port)

# simple_email_context = ssl.create_default_context()

# # this secures the connection (why im not sure)

# connection.starttls(context=simple_email_context)
# connection.login(user=my_email,password=ps)
# connection.sendmail(from_addr=my_email, to_addrs='chenyiqing2129@gmail.com',msg="Subject:happy valentines\n\nI love you")
# connection.close()

# -------------- can also use 'with' command
# with smtplib.SMTP(smtp_server,smtp_port) as connection:
#   connection.starttls(context=simple_email_context)
#   connection.login(user=my_email,password=ps)
#   connection.sendmail(from_addr=my_email, to_addrs='chenyiqing2129@gmail.com',msg="Subject:happy valentines\n\nI love you")

import datetime as dt

now = dt.datetime.now()
year = now.year
print(now)        #### Comes out as a datetime object
# print(type(now))
# print(year)       #### Comes out as a integer
# # print(type(year))

# dob = dt.datetime(year=1996, month=1, day=23, hour=11,minute=46)
# print(dob)