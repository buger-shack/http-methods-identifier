import requests
import argparse
import pyfiglet

def get_args():
    parser = argparse.ArgumentParser(
        description='Python HTTP Method Identifier')
    parser.add_argument(
        '-u', '--url', type=str, help='target URL', required=True)
    args = parser.parse_args()
    URL = args.url
    return URL

url = get_args()

print("\033[1;34m")
header2 = pyfiglet.figlet_format("HTTP Method Identifier", font = "cybermedium")
print(header2)

verbs = ['GET', 'POST', 'PUT','HEAD', 'DELETE', 'OPTIONS', 'TRACE', 'TEST', 'PROPFIND', 'CONNECT']
print("\033[1;37m")
for verb in verbs:
    req = requests.request(verb, url)
    print(verb, req.status_code, req.reason)
    if verb == 'TRACE' and 'TRACE / HTTP/2' in req.text:
      print('\033[1;31mPossible Cross Site Tracing vulnerability found\nTRACE method used')
