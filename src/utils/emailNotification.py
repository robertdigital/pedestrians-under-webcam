#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib, ssl
from email.mime.text import MIMEText
from email.header import Header
import platform

def emailNotification(prefix, num, time_interval, start, end, url, method):
    platform = platform.system()
    
    try:
        sender = 'pedestriansunderwebcam@gmail.com'
        receivers = ['ruikun.li@rwth-aachen.de']  
        
        message = MIMEText(
            """
            <p> {} Task finished, there are {} samples, time interval is {} minutes  </p>
            <p>Start time at webcam timezone: {} </p>
            <p>End time at webcam timezone:{} </p>
            <p>Webcam url : {} </p>
            <p>Method: {}</p>
            <p>Platform: {}</p>
                            """.format(prefix, num, time_interval/60, start, end, url, method, platform), 'html', 'utf-8')
        
        subject = '{} task notification'.format(prefix)
        message['Subject'] = Header(subject, 'utf-8')

        mail = smtplib.SMTP('smtp.gmail.com',587)

        mail.ehlo()

        mail.starttls()

        mail.login('pedestriansunderwebcam@gmail.com','bruce5271527vae')

        mail.sendmail(sender, receivers, message.as_string())
    except Exception as e:
        print(e)
    finally:
        mail.close()
        print("Email Notification Sent")


