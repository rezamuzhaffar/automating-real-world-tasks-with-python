#!/usr/bin/env python3

import psutil
import shutil
import os
import socket
import emails

def cpu_usage_checks():
    cpu_usage = psutil.cpu_percent(1)
    return cpu_usage > 80

def disk_space_checks(path):
    d_usage = psutil.disk_usage(path)
    d_space = d_usage.free / d_usage.total * 100
    return d_space < 20

def memory_space_checks():
    m_space = psutil.virtual_memory().available / (1024 ** 2)
    return m_space < 500

def localhost_checks():
    localhost = socket.gethostbyname('localhost')
    return localhost == "127.0.0.1"

if cpu_usage_checks():
    message = emails.generate_email(
        sender = "automation@example.com",
        recipient = "{}@example.com".format(os.environ.get('USER')),
        subject = "Error - CPU usage is over 80%",
        body = "Please check your system and resolve the issue as soon as possible.",
        attachment_path = ""
    )
    emails.send_email(message)

if disk_space_checks("/"):
    message = emails.generate_email(
        sender = "automation@example.com",
        recipient = "{}@example.com".format(os.environ.get('USER')),
        subject = "Error - Available disk space is less than 20%",
        body = "Please check your system and resolve the issue as soon as possible.",
        attachment_path = ""
    )
    emails.send_email(message)

if memory_space_checks():
    message = emails.generate_email(
        sender = "automation@example.com",
        recipient = "{}@example.com".format(os.environ.get('USER')),
        subject = "Error - Available memory is less than 500MB",
        body = "Please check your system and resolve the issue as soon as possible.",
        attachment_path = ""
    )
    emails.send_email(message)

if localhost_checks():
    message = emails.generate_email(
        sender = "automation@example.com",
        recipient = "{}@example.com".format(os.environ.get('USER')),
        subject = "Error - localhost cannot be resolved to 127.0.0.1",
        body = "Please check your system and resolve the issue as soon as possible.",
        attachment_path = ""
    )
    emails.send_email(message)