#!/usr/bin/env python
from shutil import copy

copy('.ecmwfapirc', '/root')

from ecmwfapi import ECMWFDataServer

server = ECMWFDataServer()
server.retrieve({
    "class": "ea",
    "dataset": "era5",
    "expver": "1",
    "stream": "oper",
    "type": "an",
    "levtype": "sfc",
    "param": "165.128/166.128/167.128",
    "date": "2016-01-01/to/2016-01-02",
    "time": "00:00:00",
    "step": "0",
    "grid": "0.25/0.25",
    "area": "75/-20/10/60",
    "format": "netcdf",
    "target": "test.nc"
 })

