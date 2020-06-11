import requests
def send_message(to_,message_):
    url = "https://inteltech.p.rapidapi.com/send.php"
    payload = "username=YOUR_USERNAME&key=YOUR_API_KEY&sms={RECIPIENT_MOBILE_NUMBER}&message={MESSAGE_TO_BE_SENT}".format(to_,message_)
    
    headers = {
        'x-rapidapi-host': "inteltech.p.rapidapi.com",
        'x-rapidapi-key': "45e8eed7e3msh8ce5de589183bb9p111ef1jsn46ee5b9d3850",
        'content-type': "application/x-www-form-urlencoded"
    }
    
    response = requests.request("POST", url, data=payload, headers=headers)
