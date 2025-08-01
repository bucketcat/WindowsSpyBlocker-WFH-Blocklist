
## Usage

If you want updates, import the blocklist from github. You may also clone the repo and manually add the blocklist to your DNS servers blocklist if you do not want to pull it remotely.

* If using Unbound DNS through OPNsense.

Navgiate to `Services > Unbound DNS > Blocklist` in OPNsense. Click `Àdvanced mode`. Copy the raw url of the file Converted.conf into the textbox under `URLs of Blocklists`. The raw file can be accessed by clicking on Converted.conf in github, then the button called "Raw". Simply paste the raw.githubusercontent.com/<stuff> url into the previously mentioned box.

Add the microsoft subdomain listed at the bottom of this ReadMe to your whitelist if your WFH (Work from home) is in a Microsoft/Azure Active Directory/Active Directory tenant.

* If using Unbound DNS through other software or standalone.

 simply add the "Converted.conf" raw link to wherever it is you import blocklists.
 
 * If using Technitium DNS
 
 ToDo, unknown format.
 
 
 * If using dnscrypt
 
 The minimized.txt file is in dnscrypt format. It should work as is. It should, though I have yet to test it, also work in Ublock Origin.




## Usage: Forks and local

The dnscrypt_to_localzone.py converts the dnscrypt/ublock origin format to Unbound format. Update minimized.txt and run the python script to automatically update the Unbound blocklist (converted.conf)

## Contents

This is a static backup url of the spy.txt combined with a small excerpt of the extra.txt from https://github.com/crazy-max/WindowsSpyBlocker/.
The primary goal is to have a load balanced url for my unbound install combined with manually curated urls from the extra.txt list, without affecting WFH in both on-prem AD and cloud based Azure tenants.

I have also added some of my static (not wildcard, ToDo) manual entries.

Update: Started adding Swedish and Norwegian advertisement subdomains as this doesn't really exist in a Unbound supported format from what I've found.


### Whitelist

```

### https://github.com/crazy-max/WindowsSpyBlocker/issues/522

ztd.dds.microsoft.com

```