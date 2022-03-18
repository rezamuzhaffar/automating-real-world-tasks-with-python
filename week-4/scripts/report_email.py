#!/usr/bin/env python3

import sys
import os
from datetime import date
import reports
import emails

def load_data(directory):
    content_format = ['name', 'weight']
    data = []
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename)) as txtfile:
            dict = {}
            reader = txtfile.read().split("\n")
            for i in range(len(content_format)):
                dict[content_format[i]] = reader[i]
            data.append(dict)
    return data

def process_data(data):
    summary = []
    for item in data:
        item_info = "name: {}<br/>weight: {}".format(item['name'], item['weight'])
        summary.append(item_info)
    return summary

def main(argv):
    today = date.today()
    data = load_data("supplier-data/descriptions/")
    summary = process_data(data)
    print(summary)
    reports.generate_report(
        attachment = "/tmp/processed.pdf",
        title = "Processed Update on {}".format(today.strftime("%B %d, %Y")),
        paragraph = "<br/><br/>".join(summary)
    )
    message = emails.generate_email(
        sender = "automation@example.com",
        recipient = "{}@example.com".format(os.environ.get('USER')),
        subject = "Upload Completed - Online Fruit Store",
        body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        attachment_path = "/tmp/processed.pdf"
    )
    emails.send_email(message)

if __name__ == "__main__":
    main(sys.argv)