import requests
import json

data = {
    "cacheKey":"JTdCJTIyYWRkcmVzcyUyMiUzQSUyMjU1NSUyMENhbGlmb3JuaWElMjBTdCUyMiUyQyUyMnJlZmVyZW5jZSUyMiUzQSUyMkNoSUo0N2ZZTUlxQWhZQVJiZ3FCYVBab0FKNCUyMiUyQyUyMnJlZmVyZW5jZVR5cGUlMjIlM0ElMjJnb29nbGVfcGxhY2VzJTIyJTJDJTIybGF0aXR1ZGUlMjIlM0EzNy43OTIyMzY3JTJDJTIybG9uZ2l0dWRlJTIyJTNBLTEyMi40MDQzMzA1JTdE/DELIVERY///1/1/eyJwbHVnaW4iOiJyZWNvbW1lbmRhdGlvbkZlZWRQbHVnaW4iLCJyZWNvbW1UeXBlIjoicHJvbW90ZWRfcmVzdGF1cmFudHMifQ==/JTVCJTVE////////HOME",
    "feedSessionCount": {
        "announcementCount": 0,
        "announcementLabel": ""
    },
    "showSearchNoAddress": False,
    "userQuery": "",
    "date": "",
    "startTime": 0,
    "endTime": 0,
    "carouselId": "",
    "sortAndFilters": [{
        "uuid": "2c7cf7ef-730f-431f-9072-27bc39f7c021",
        "options": [{
            "uuid": "2c7cf7ef-730f-431f-9072-26bc39f7c025"
        }]
    }],
    "marketingFeedType": "",
    "billboardUuid": "",
    "feedProvider": "",
    "promotionUuid": "",
    "targetingStoreTag": "",
    "venueUuid": "",
    "favorites": "",
    "pageInfo": {
        "offset": 0,
        "pageSize": 10000
    }}

headers = {
    "x-csrf-token": "x",
    "content-type": "application/json",
    "cookie": "uev2.id.xp=5b8026ae-54b6-441a-ac0f-6acdb5ec290d; dId=9ba7bb10-2afb-4f5c-9a7f-c6b95ba4d8b4; uev2.id.session=005451bd-17f1-4da7-902f-f1ab8277ac6f; uev2.ts.session=1638550366399; marketing_vistor_id=4b474bbe-8790-4474-b633-47a5b04bc0d3; jwt-session=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE2Mzg1NTAzNjYsImV4cCI6MTYzODYzNjc2Nn0.P3DEjz7qGPGQPnQLk_24ZbQppHOXuu72SPSFQJtGUSo; uev2.gg=true; utag_main=v_id:017d81368dae0007a59165814adf0004c001b00900bd0$_sn:1$_se:25$_ss:0$_st:1638553377514$ses_id:1638550375855%3Bexp-session$_pn:6%3Bexp-session; _userUuid=31971362-13ad-4984-9293-5a721bb26859; utm_medium=undefined; CONSENTMGR=c1:1%7Cc2:1%7Cc3:1%7Cc4:1%7Cc5:1%7Cc6:1%7Cc7:1%7Cc8:1%7Cc9:1%7Cc10:1%7Cc11:1%7Cc12:1%7Cc13:1%7Cc14:1%7Cc15:1%7Cts:1638550375870%7Cconsent:true; _rdt_uuid=1638550375999.ac13bcc7-8851-47ae-97a4-6a296e7838b7; _gcl_au=1.1.960269758.1638550376; _scid=6728a20d-3eaa-4a2f-b636-644e5b1f687d; _ts_yjad=1638550377007; _ga=GA1.2.1627877633.1638550377; _gid=GA1.2.1435400044.1638550377; sid=QA.CAESELd8LJpNIkKsupWp9sSVKxkYjbrHjgYiATEqJDMxOTcxMzYyLTEzYWQtNDk4NC05MjkzLTVhNzIxYmIyNjg1OTI8UtvuxPBCS7QUrBvN1QF5RTOX4Iem60aCi9kkE9pdjH9X28w67uOY3CpBGbVbjYnwNWgsbyELn08gwQ_8OgExQg0udWJlcmVhdHMuY29t.AOGfEW2C57VIaffXv2NgybCZN5kY5Jwp5rHN9gApKK4; uev2.loc=%7B%22address%22%3A%7B%22address1%22%3A%22Pla%C3%A7a%20de%20la%20Universitat%2C%205%22%2C%22address2%22%3A%2208007%20Barcelona%22%2C%22aptOrSuite%22%3A%22%22%2C%22eaterFormattedAddress%22%3A%22Pla%C3%A7a%20de%20la%20Universitat%2C%205%2C%2008007%20Barcelona%2C%20Espa%C3%B1a%22%2C%22subtitle%22%3A%2208007%20Barcelona%22%2C%22title%22%3A%22Pla%C3%A7a%20de%20la%20Universitat%2C%205%22%2C%22uuid%22%3A%22%22%7D%2C%22latitude%22%3A41.3853921%2C%22longitude%22%3A2.1644227%2C%22reference%22%3A%22ChIJ_1uOUYuipBIRhyTLRZTs3wA%22%2C%22referenceType%22%3A%22google_places%22%2C%22type%22%3A%22google_places%22%2C%22addressComponents%22%3A%7B%22STREET_NAME%22%3A%22Pla%C3%A7a%20de%20la%20Universitat%22%2C%22FIRST_LEVEL_SUBDIVISION_CODE%22%3A%22CT%22%2C%22CITY%22%3A%22Barcelona%22%2C%22HOUSE_NUMBER%22%3A%225%22%2C%22COUNTRY_CODE%22%3A%22ES%22%2C%22POSTAL_CODE%22%3A%2208007%22%7D%2C%22originType%22%3A%22user_autocomplete%22%7D; _uetsid=76a34870545911ec8d7e57d1878d8609; _uetvid=76a39cd0545911ecb0c0ff9dbfaed1d5; _gat_tealium_0=1"
}

r = requests.post(
    "https://www.ubereats.com/api/getFeedV1?localeCode=es", json=data, headers=headers)

if r.status_code != 200:
    print("Unexpected response code.")
    print(r.status_code)
    exit()

categories = {}

data = r.json()['data']['feedItems']
print(data[0])
for feedItem in data:
    title = feedItem['store']['title']['text']
    signpost = "NOTHING"
    if len(feedItem['store']['signposts']) > 0:
        signpost = feedItem['store']['signposts'][0]['text']
    if not signpost in categories:
        categories[signpost] = []
    categories[signpost].append(title)

for key,value in categories.items():
    if key.startswith("Gasta"):
        print("OFERTITA: " + key + ", EN:")
        print(value)
        print()