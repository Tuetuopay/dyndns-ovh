#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import os, ovh
from optparse import OptionParser
import netifaces as ni

def setRecord(client, domain, subdomain, field, value):
    records = client.get('/domain/zone/%s/record' % (domain), fieldType=field, subDomain=subdomain)
    if len(records) == 0:
        out = client.post('/domain/zone/%s/record' % (domain), fieldType=field, subDomain=subdomain, target=value, ttl=0)
    else:
        out = client.put('/domain/zone/%s/record/%d' % (domain, records[0]), target=value)
    out2 = client.post('/domain/zone/%s/refresh' % (domain))
    return (out, out2)

def main():
    # Checking ENV args
    for key in ['KEY', 'SECRET', 'CONSUMER']:
        if 'OVH_APPLICATION_' + key not in os.environ:
            print('Missing key %s. Aborting.' % ("OVH_APPLICATION_" + key))
            exit()

    # Parse script arguments
    parser = OptionParser()
    parser.add_option("-i", "--interface",
                      help="sets the interface to fetch the IP from",
                      action="store", default="lo", dest="interface")
    parser.add_option("-d", "--domain", help="domain to act on", action="store",
                      dest="domain", default="example.com")
    parser.add_option("-s", "--subdomain",
                      help="subdomain to act on, empty for root",
                      action="store", dest="subdomain", default="")
    parser.usage = """%prog [options]"""
    parser.description = "Updates the A and AAAA (if available) records for subdomain.domain with the IPs from interface."

    (options, args) = parser.parse_args()
    interface, domain, subdomain = options.interface, options.domain, options.subdomain

    # OVH API
    client = ovh.Client(
        endpoint="ovh-eu",
        application_key=os.environ['OVH_APPLICATION_KEY'],
        application_secret=os.environ['OVH_APPLICATION_SECRET'],
        consumer_key=os.environ['OVH_APPLICATION_CONSUMER']
    )

    print("Host: %s.%s" % (subdomain, domain))

    # Fetch IP addresses
    addr = ni.ifaddresses(interface)
    try:
        ipv4 = addr[ni.AF_INET][0]['addr']
        print("Setting A record to %s" % (ipv4))
        print(setRecord(client, domain, subdomain, 'A', ipv4))
    except e:
        print("No IPv4 found for interface %s" % (interface))
    try:
        ipv6 = addr[ni.AF_INET6][0]['addr']
        print("Setting AAAA record to %s" % (ipv6))
        print(setRecord(client, domain, subdomain, 'AAAA', ipv6))
    except e:
        print("No IPv6 found for interface %s" % (interface))

if __name__ == '__main__':
    main()

