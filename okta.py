import pandas as pd
import json

data = [

 {
    "actor": {
      "id": "00uunrjAXkpQdiZqQ693",
      "type": "User",
      "alternateId": "freetrialorgcreator@okta.com",
      "displayName": "FreeTrial OrgCreator",
      "detailEntry": ""
    },
    "client": {
      "userAgent": {
        "rawUserAgent": "Java/11.0.18",
        "os": "Unknown",
        "browser": "UNKNOWN"
      },
      "zone": "OFF_NETWORK",
      "device": "Unknown",
      "id": "",
      "ipAddress": "52.207.21.207",
      "geographicalContext": {
        "city": "Ashburn",
        "state": "Virginia",
        "country": "United States",
        "postalCode": "20149",
        "geolocation": {
          "lat": 39.0469,
          "lon": -77.4903
        }
      }
    },
    "device": "",
    "authenticationContext": {
      "authenticationProvider": "",
      "credentialProvider": "",
      "credentialType": "",
      "issuer": "",
      "interface": "",
      "authenticationStep": 0,
      "externalSessionId": "trstTnNsvNvTZKpOjwAIMklHQ"
    },
    "displayMessage": "Update application",
    "eventType": "application.lifecycle.update",
    "outcome": {
      "result": "SUCCESS",
      "reason": ""
    },
    "published": "2023-03-12T02:15:46.689Z",
    "securityContext": {
      "asNumber": "",
      "asOrg": "",
      "isp": "",
      "domain": "",
      "isProxy": ""
    },
    "severity": "INFO",
    "debugContext": {
      "debugData": {
        "requestId": "ZA010XnesYGs4o0vCXX_nQAACpg",
        "requestUri": "/api/internal/orgs",
        "url": "/api/internal/orgs?"
      }
    },
    "legacyEventType": "app.generic.config.app_updated",
    "transaction": {
      "type": "WEB",
      "id": "ZA010XnesYGs4o0vCXX_nQAACpg",
      "detail": {}
    },
    "uuid": "ccbe579e-c07b-11ed-9614-bb2873f5e6ca",
    "version": "0",
    "request": {
      "ipChain": [
        {
          "ip": "52.207.21.207",
          "geographicalContext": {
            "city": "Ashburn",
            "state": "Virginia",
            "country": "United States",
            "postalCode": "20149",
            "geolocation": {
              "lat": 39.0469,
              "lon": -77.4903
            }
          },
          "version": "V4",
          "source": ""
        }
      ]
    },
    "target": [
      {
        "id": "0oa4igrxlueUtCRAx697",
        "type": "AppInstance",
        "alternateId": "Okta Admin Console",
        "displayName": "Okta Admin Console",
        "detailEntry": ""
      }
    ]
  }

    
]

#print(data)


#json_data = json.dumps(data)

#dict_data = json.loads(data)
#print(dict_data)

#df = pd.json_normalize(data)

#print(df)
