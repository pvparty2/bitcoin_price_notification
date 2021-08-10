import requests


def webhook_notify(event, value, key='<your-personal-IFTTT-key>') -> None:
    '''
        Post to IFTTT applet webhook URL.
        The URL can be found by clicking 'Documentation' at: https://ifttt.com/maker_webhooks
        The event is the name of the Maker Event of the IFTTT applet.
        The value is any value.
        The default key used to be my personal key.
    '''
    ifttt_webhook_url = f'https://maker.ifttt.com/trigger/{event}/with/key/{key}'
    data = {'value1': value}
    requests.post(ifttt_webhook_url, json=data)
