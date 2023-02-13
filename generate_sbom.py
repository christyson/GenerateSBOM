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
        description='This script takes an app name and generates a CycloneDX or SPDX SBOM in a json file named after the app with _sbom appended.')
    parser.add_argument('-a', '--app', help='App name to generate an SBOM for',required=True)
    parser.add_argument('-t', '--type', help='SBOM type. Valid values are "cyclonedx" (default) or "spdx"',required=False)
    parser.add_argument('-l', '--linked', help='Include components from linked projects? Valid values are "true" (default) or "false"',required=False)

    args = parser.parse_args()

    type = args.type
    if (type is None):
        type = "cyclonedx"
    else:    
        if (type not in ["cyclonedx", "spdx"]):
            print("Error: Type argumnet must be either \"cyclonedx\" or \"spdx\"")
            return

    linked_str = args.linked
    linked = True
    if (linked_str is not None):
        if (linked_str.lower() not in ["true", "false"]):
            print("Error: --linked must be either \"true\" or \"false\"")
            return
        else:
            linked = True if (linked_str.lower()=="true") else False

    data = vapi().get_app_by_name(args.app)
    found = False
    for app in data:
        profile = app.get("profile")
        if (profile.get("name") == args.app):
           found = True
           print("App found : "+args.app)
           app_guid = app.get("guid")
           sbom = vapi().get_sbom(app_guid, type, linked)
           app_name=args.app+"_sbom.json"
           print("SBOM for App: "+args.app +" is saved to "+app_name)
           with open(app_name, 'w') as f:
              print(json.dumps(sbom), file=f)
    if (not found):
       print ('App: '+args.app+' does not exist')
       exit(1)

    exit(0)

if __name__ == '__main__':
    main()
