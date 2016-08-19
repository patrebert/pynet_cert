#!/usr/bin/env python
import email_helper
recipient='patrebert@yahoo.com'
subject='python email test'
sender='prebert@pylab8b.twb-tech.com'
message="""
  This is a test.
  This is only a test.
"""
email_helper.send_mail(recipient, subject, message, sender)
