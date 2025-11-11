#!/usr/bin/env python3
import sys
import urllib.parse
from bs4 import BeautifulSoup

all = sys.stdin.read()
if all.startswith("<!DOCTYPE html>"):
    soup = BeautifulSoup(all, "html.parser")
    input = soup.get_text()
else:
    input = all
output = "".join(sorted(set(input)))
print(urllib.parse.quote(output))
