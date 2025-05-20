import argparse
import asyncio
import json
import websockets
import sys
import uuid

from module import *

def pretty_print_json(data):
    print(json.dumps(data, indent=4))

async def send_request(request_data, url):
    async with websockets.connect(url, subprotocols=["ocpp1.6"]) as websocket:
        await websocket.send(json.dumps(request_data))
        response = json.loads(await websocket.recv())
        print("Response:")
        pretty_print_json(response)

def check_module(req_name):
    module = f"message.{req_name}"
    if sys.modules.get(module):
        return True
    else:
        return False

def get_module(req_name):
    module = f"message.{req_name}"
    return sys.modules.get(module)

def main():
    parser = argparse.ArgumentParser(description="OCPP Request Sender CLI")
    parser.add_argument("--request", type=str, help="Action of the OCPP request")
    parser.add_argument("--url", type=str, required=True, help="WebSocket URL of the CSMS or Charge Point")
    parser.add_argument("--params", type=str, help="JSON string of the parameters for the request")
    parser.add_argument("--option")
    
    args = parser.parse_args()

    req_name   = args.request

    req_url    = args.url
    req_param  = args.params
    option     = args.option
    print(req_name)
    if not check_module(req_name):
        print(f"Request '{req_name}' is not supported.")
        exit(-1)

    # check_list = ["GetDiagnosticsRequest", "RequestStopTransactionRequest", "AuthorizeRequest"]
    # if req_name in check_list:
    #     action = req_name[7:]

    module = get_module(req_name)
    request = getattr(module, req_name)

    if "Request" in req_name:
        action = req_name.replace("Request", "")
        params = [
            2,
            str(uuid.uuid4()),
            action
        ]
    elif "Response" in req_name:
        action = req_name.replace("Response", "")
        params = [
            3,
            str(uuid.uuid4()),
            action
        ]
    else:
        raise ValueError("Not Support action")
    
    req_data = json.loads(args.params) if args.params else request.get_sample(option=option)
    params.append(req_data)
    
    print("Request:")
    pretty_print_json(params)

    asyncio.run(send_request(params, req_url))