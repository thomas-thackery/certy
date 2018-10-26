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
#customer_input = str(customer_input)
#customer_input = "pan site_certs.get_csr " + customer_input.replace('#','')

def create_command(customer_details): 
    command = ''
    for detail in range(len(customer_details)):
        customer_details[detail] = customer_details[detail].replace('#','')
        customer_details[detail] = customer_details[detail].replace('-','\-')
        customer_details[detail] = customer_details[detail].replace(',','\,')
        customer_details[detail] = customer_details[detail].strip()
        customer_details[detail] = common_name(customer_details[detail])
        command += customer_details[detail]
    return command

def common_name(detail):
    if "common name" in detail.lower():
        detail = detail.lower().replace("common name","common_name")
        detail = detail.replace(" ","")
    return detail + ","

def dns_names(detail):
    return detail + ","

def emails(detail):
    return detail + ","

def org(detail):
    return detail + ","

def org_unit(detail):
    return detail + ","

def country(detail):
    return detail + ","

def locality(detail):
    return detail + ","

def province(detail):
    return detail + ","

print("pan site_certs.get_csr:" + create_command(customer_input))

# test input
# Common name: some-sub.example.com
 # DNS names: some-site.example.com, some-other-sub.example.com 
# Organization: Some-Org, Inc.
# Organizational unit: IT-Brain, 
# Country: US
# Locality: San Pasquale
# State / Province: Rhode Island
