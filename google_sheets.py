import json
import gspread
import warnings
warnings.filterwarnings("ignore")
def connect_to_google_sheet(name):
    google_key = {
        "type": "service_account",
        "project_id": "parsing-360910",
        "private_key_id": "b78d533fa22f4480cf8b374466e409997fa4cf3e",
        "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEugIBADANBgkqhkiG9w0BAQEFAASCBKQwggSgAgEAAoIBAQDK8oEixR13RAOh\nGL+v0cKgfRLXM9rBKukCnWX8A7rbl5PZaVD5iDwa2UO2hfI+rEU3mgyBMKshUmPl\nohwljlEKD6+csgTnlZelOu5BDvdMrkb7q4Y/jzuwxQYnIL4cNgPOyELXWde7GYAU\nitDcDaOG/no0KbVyEl+TfhespX1jwzt48IXniPvkEkJ36B5U+lWZUZJG1i4VBmlY\nGeaqjtUp1xUHhhZIkMkYYZ3kh8mKQYRGNq8dcX5rKAeDKFKbAvrq9E7hYqjl9nZC\ngvpksExxLRTTJPkiVLjjRGFoYftzIpqbrfjh1Zb34bnSBxcNoNm5kOYBMtoyYFxs\nl9hqN+rjAgMBAAECgf9LLd+ogbHopx6xDqSeUkCcMw5HqhiJy4YwRx5VvQv7TKtN\ns+B15NcJxcd6Vc7nEz87hFVy22new3vov6StmjVrBLnefL5UYOtMH13Nu+g1qlmh\nNmkEzTUkxoJWUaAbKJHrMpmQLOKS7LSwPLwiHZX2QU6uWW+y/MYVsnVn/ztJON/H\nBPakSm81htxrazcQNxjd0d+TzXZeKt45qFOqnRg4r41kN+H5cnMBFCd8WnlqHl9u\nwseXsaSsVEK9moMQZIU30mo4qW9mm1vPxtkibvY2Cu5feiBP+YtY+yrZVBEOkjpW\nZvKwLT4iNNabTcbp6tH7Vx7bck2TASz3ogcOU7UCgYEA+PUpuUmIMyLYKH/CDt28\n6Ps2vIZJDEHOCQvq1PW8dXWX/gaRyZ+HeiIq+CLTO1Z0jU4f4UV/M9JfPQ2PYykj\nL01neNyEPco+1i+b0+fDHOJ4wLQ7WVH6cYcFWWcBmOUE50s/7ig8Dm7IG+bQoOBj\nCH6rvJ1ToCOsmE/HGaCx3bUCgYEA0LAnx67dCRe2/N6l6/iNhn3vciY015RU+86W\n2737D51xpBFSCnP00ZFbj/yfhHsV+YezQBEoGB2VOr+/2H8t2inmAnGKT/HDEpJP\n/5XPrn4LrW5YTgxeQ8pn7tGyfzWPqMNBoTOjnjGBLCVRUgvfmpz+FJxhRMyicdq+\nwznxxTcCgYACGM6JKP1ksN5xOOJBjcyRicwkOl1TJRq/KMKJmKhFtP/au+Nud1GE\nzdTe0ixFS60fo5DRLOytWxBCS2Lxyt7o/xXoBrN2ccWluDDvz/vsuluaA+qcDfy2\nCBUbc6qnxwYLjK61KtGWrYgx8/e94yXyZF697/VMXACQJ9vdc2UMIQKBgEopb9mc\noNxsWxE+JoTXTaQv+Pn97eV2x0S9RAtPVntUHmCJ7zfbwXMATyO6SQ4Rl9uXh/IK\nps77JF8+aXUMrUTMgvr3UonahtKAwIE5whZmoMu/XQ5Pguhgc9MBHofqhuUYjqg0\n6756JUeE84NOyOXvSLQWZtLGTixb6lMCspK9AoGAIMeA+Pt4tS88leLn+IK6ru0r\n0twTwBw4nQwZRZ7pJS88apU84lHsb9VZUoXLcmeVgMqNR/hmqkQ176JsE+bNeHW7\nlrHTstXwM8xp18//b9NOBLCj4ocwrRCxnE9HX+Zfq+wfiRUNRbW7usC6PMqceOxQ\nA1DTLKLLY1vqpGcOEQc=\n-----END PRIVATE KEY-----\n",
        "client_email": "parsing@parsing-360910.iam.gserviceaccount.com",
        "client_id": "104700695693505507681",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/parsing%40parsing-360910.iam.gserviceaccount.com"
    }
    with open("google_key_1.json", "w") as outfile:
        json.dump(google_key, outfile)
    creds = gspread.service_account(filename="google_key_1.json")
    sh = creds.open("Парсинг")
    worksheet = sh.worksheet(name)
    return worksheet
