from __main__ import app,request,requests,pprint,json,my_util,os
from my_util import get_page_id,get_PAT

dayek_crm_ua_token = os.environ.get('INSTA_UA_TOKEN')  
app_id = os.environ.get('APP_ID')
fb_pat = os.environ.get('FB_PAGE_ACCESS_TOKEN')

@app.route('/fb/listen_for_message',methods=['GET'])
def fb_webhook_verify():
    params = dict(request.args)
    if params['hub.verify_token'] == os.environ.get('WEBHOOK_TOKEN'):
        return params.get('hub.challenge'),200
    return 'Error, wrong validation token',400
    

@app.route('/fb/listen_for_message',methods=['POST'])
def fb_webhook_callback():
    pprint.pprint(request.json)
    return {
        'msg':'OK'
    },200    


@app.route('/fb/get_conversations',methods=['GET'])
def fb_get_thread_ids():
    page_id = get_page_id()
    pat = get_PAT()
    print(page_id)
    print(app_id)
    res1 = requests.get("https://graph.facebook.com/v12.0/{}/conversations?fields=participants&access_token={}".format(page_id,pat) ).json()

    return {
        'data':res1
    },200

@app.route('/fb/read_messages',methods=['POST'])
def fb_read_messages():
    pat = get_PAT()
    data = request.json.get('data')
    thread_id = data.get('thread_id')
    res = requests.get("https://graph.facebook.com/v12.0/{}?fields=messages&access_token={}".format(thread_id,pat)).json() 
    messages = res.get('messages').get('data') 
    for i,x in enumerate(messages):
        res1 = requests.get("https://graph.facebook.com/v12.0/{}?fields=message&access_token={}".format(x.get('id') ,pat)).json() 
        x.update({'message': res1.get('message')})

    return {
        'data':messages[::-1]
    },200


@app.route('/fb/send_message',methods=['POST'])
def fb_send_message():
    data = request.json.get('data')
    msg  = request.json.get('msg')
    user_id = data.get('user_id')
    pat = get_PAT()
    req_body = {
        "messaging_type":"UPDATE",
        "recipient":{"id":user_id},
        "message":{"text":msg}
    }
    requests.post("https://graph.facebook.com/v12.0/me/messages?access_token={}".format(pat),
    json=req_body)

    return {
        'msg':'OK'
    },200    
