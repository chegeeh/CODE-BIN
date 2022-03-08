
from __main__ import app,request,requests,pprint,json,my_util,os
from my_util import get_page_id,get_PAT

dayek_crm_ua_token = os.environ.get('INSTA_UA_TOKEN')  


@app.route('/insta/read_messages',methods=['POST'])
def insta_read_messages():
    pat = get_PAT()
    data = request.json.get('data')
    thread_id = data.get('thread_id')
    res = requests.get("https://graph.facebook.com/v12.0/{}?fields=participants,messages&access_token={}".format(thread_id,pat)).json() 
    messages = res.get('messages').get('data') 
    for i,x in enumerate(messages):
        res1 = requests.get("https://graph.facebook.com/v12.0/{}?fields=message&access_token={}".format(x.get('id') ,pat)).json() 
        x.update({'message': res1.get('message')})
    return {
        'data':messages[::-1]
    },200
    

@app.route('/insta/send_message',methods=['POST'])
def insta_send_message():
    msg  = request.json['msg']
    pat = get_PAT()
    req_body = {
        "recipient":{"id":4721754214547787},
        "message":{"text":msg}
    }
    requests.post("https://graph.facebook.com/v12.0/me/messages?access_token={}".format(pat),
    json=req_body)

    return {
        'msg':'OK'
    },200

@app.route('/insta/get_thread_ids',methods=['GET'])
def insta_get_thread_ids():
    page_id = get_page_id()
    pat = get_PAT()
    res1 = requests.get("https://graph.facebook.com/v12.0/{}/conversations?platform=instagram&access_token={}".format(page_id,pat) ).json()
    thread_ids = res1.get('data')

    return {
        'data':thread_ids
    },200

   
@app.route('/insta/listen_for_message',methods=['GET'])
def insta_webhook_verify():
    params = dict(request.args)
    if params['hub.verify_token'] == os.environ.get('WEBHOOK_TOKEN'):
        return params.get('hub.challenge'),200
    return 'Error, wrong validation token',400
    

@app.route('/insta/listen_for_message',methods=['POST'])
def insta_webhook_callback():
    pprint.pprint(request.json)
    return {
        'msg':'OK'
    },200 
