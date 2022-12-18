#!/usr/bin/env python

import json

FILE_LOCATION='/var/lib/awx/projects/hosts'

def inventory():
    return {
        'all': {
            'hosts': hosts(),
            'vars': {},
        }
    }

def hosts():
    inputs=[]
    f= open(FILE_LOCATION)
    for line in f.readlines():
        for item in line.split(','):
            if item and item.strip():
                inputs.append(item.strip())
    return inputs

print(json.dumps(inventory()))
