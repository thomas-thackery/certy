#!/usr/bin/env python3

# Usage: Takes customer supplied multiline CSR details and creates a single command to generate CSR

def multi_input():
    print("Please paste in the CSR details provided by the customer")
    try:
        while True:
            customer_input=input()
            if not customer_input: break
            yield customer_input
    except KeyboardInterrupt:
        return

customer_input = list(multi_input())

def create_command(customer_details): 
    command = ''
    for detail in range(len(customer_details)):
        customer_details[detail] = customer_details[detail].replace('#','')
        #customer_details[detail] = customer_details[detail].replace('-','\-')
        customer_details[detail] = customer_details[detail].replace(',','\,')
        customer_details[detail] = customer_details[detail].strip()
        customer_details[detail] = common_name(customer_details[detail])
        customer_details[detail] = dns_names(customer_details[detail])
        customer_details[detail] = emails(customer_details[detail])
        customer_details[detail] = org(customer_details[detail])
        command += customer_details[detail] + ','
    return command

def common_name(detail):
    if "common name" in detail.lower():
        detail = detail.lower().replace("common name","common_name")
        detail = detail.replace(":","=")
        detail = detail.replace(" ","")
    return detail

 # DNS names: some-site.example.com, some-other-sub.example.com
def dns_names(detail):
    if "dns names" in detail.lower():
        detail = detail.lower().replace("dns names","dns_names")
    if "dns name" in detail.lower():
        detail = detail.lower().replace("dns name","dns_names")
        detail = detail.replace(":","=")
        detail = detail.replace(",",":")
        detail = detail.replace(" ","")
    return detail

# Email addresses boing-rwtegd@dsafj.com me@po-do.us
def emails(detail):
    if "Email addresses [optional]".lower() in detail.lower():
        detail = detail.lower().replace("email addresses [optional]","emails=")
    if "Email addresses".lower() in detail.lower():
        detail = detail.lower().replace("email addresses","emails=")
    if "E-mail address: Optional".lower() in detail.lower():
        detail = detail.lower().replace("e-mail address: optional","emails=")
        #detail = detail.replace(" ","20%")
        detail = detail + "'"
        detail = detail.replace(" ","")
        #detail = detail.replace(":","=")
        # detail = detail.replace(",",":")
        detail = detail.replace(" ",":")
        detail = detail + "'"
    return detail

def org(detail):
    if "Organization:" in detail:
        detail = detail.replace("Organization:","org='")
        detail = detail.lstrip()
        detail = detail.replace("-","\-")
        detail = detail.replace(",","\,")
        detail = detail + "'"
    return detail

def org_unit(detail):
    return detail

def country(detail):
    return detail

def locality(detail):
    return detail

def province(detail):
    return detail

def technical_detail(detail):

    return detail

print("pan site_certs.get_csr:" + create_command(customer_input))

# test input
# Email addresses boing-rwtegd@dsafj.com me@po-do.us

# Common name: some-sub.example.com
 # DNS names: some-site.example.com, some-other-sub.example.com 
# Email addresses [optional] boink-daslfj@2345267.io.co
# Organization: Some-Org, Inc.
# Organizational unit: IT-Brain, 
# Country: US
# Locality: San Pasquale
# State / Province: Rhode Island

