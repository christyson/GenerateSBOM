import sys
import requests
import argparse
import json
from veracode_api_signing.plugin_requests import RequestsAuthPluginVeracodeHMAC
from veracode_api_py import VeracodeAPI as vapi
api_target = "https://analysiscenter.veracode.com/api/5.0/deletebuild.do"
headers = {"User-Agent": "Python HMAC Example"}

def main():

    parser = argparse.ArgumentParser(
        description='This script takes an app name and generates an SBOM in cycloneDX format in a json file nameded after the app with _sbom appended.')
    parser.add_argument('-a', '--app', help='App name to generate an SBOM for',required=True)
    args = parser.parse_args()

    data = vapi().get_app_by_name(args.app)
    found = False
    for app in data:
        profile = app.get("profile")
        if (profile.get("name") == args.app):
           found = True
           print("App found : "+args.app)
           app_guid = app.get("guid")
           sbom = vapi().get_sbom(app_guid)
           app_name=args.app+"_sbom.json"
           print("SBOM for App: "+args.app +" is saved to "+app_name)
           with open(app_name, 'w') as f:
              print(json.dumps(sbom), file=f)
    if (not found):
       print ('App: '+args.app+' does not exist')
    exit(0)

if __name__ == '__main__':
    main()
