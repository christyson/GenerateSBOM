# Veracode Generate SBOM

A simple example script generate a CycloneDX SBOM for an app in a json file.

## Setup

Clone this repository:

    git clone https://github.com/christyson/GenerateSBOM.git

Install dependencies:

    cd GenerateSBOM
    pip install -r requirements.txt

(Optional) Save Veracode API credentials in `~/.veracode/credentials`

    [default]
    veracode_api_key_id = <YOUR_API_KEY_ID>
    veracode_api_key_secret = <YOUR_API_KEY_SECRET>

## Usage for a single app profile or and app profile with a sandbox

`generate_sbom.py [-h] <arguments>`

Arguments:
* `-a` or `--app` : (required) Name of the application within Veracode
* `-t` or `--type` : (optional) Type of SBOM to generate; valid values are 'cyclonedx' (default) or 'spdx'
* `-l` or `--linked` : (optional) Include components from linked projects or not; valid values are 'true' (default) or 'false'

## Run

If you have saved credentials as above you can run:

`python generate_sbom.py -a <your app name>`

Otherwise you will need to set environment variables as follows:

```
export VERACODE_API_KEY_ID=<YOUR_API_KEY_ID>
export VERACODE_API_KEY_SECRET=<YOUR_API_KEY_SECRET>
python generate_sbom.py -a <your app name>
```

Both of these methods will generate a CycloneDX SBOM in a file called "your app name"_sbom.json

If the app is not found an error message will be printed.
