# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 15:21:26 2021

@author: risev
"""

from http.server import HTTPServer, CGIHTTPRequestHandler

server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)

print("HTTP server start on localhost:8000")
httpd.serve_forever()