import argparse
import asyncio
import json
import websockets
import sys
import uuid

import module

from requests import *

def pretty_print_json(data):
    print(json.dumps(data, indent=4))

async def send_request(request_data, url):
    async with websockets.connect(url) as websocket:
        await websocket.send(json.dumps(request_data))
        response = json.loads(await websocket.recv())
        print("Response:")
        pretty_print_json(response)

def check_module(req_name):
    module = f"requests.{req_name}"
    if sys.modules.get(module):
        return True
    else:
        return False

def get_module(req_name):
    module = f"requests.{req_name}"
    return sys.modules.get(module)

def main():
    parser = argparse.ArgumentParser(description="OCPP Request Sender CLI")
    parser.add_argument("--action", type=str, help="Action of the OCPP request")
    parser.add_argument("--url", type=str, required=True, help="WebSocket URL of the CSMS or Charge Point")
    parser.add_argument("--params", type=str, help="JSON string of the parameters for the request")
    parser.add_argument("--option")
    
    args = parser.parse_args()

    action   = args.action
    req_name = action + "Request"

    req_url    = args.url
    req_param  = args.params
    option     = args.option
    print(action)
    if not check_module(req_name):
        print(f"Request {action} is not supported.")
        exit(-1)

    check_list = ["RequestStartTransactionRequest", "RequestStopTransactionRequest"]
    if req_name in check_list:
        action = req_name[7:]

    module = get_module(req_name)
    request = getattr(module, req_name)

    params = [
        2,
        str(uuid.uuid4()),
        action
    ]
    
    req_data = json.loads(args.params) if args.params else request.sample(option=option)
    params.append(req_data)
    
    print("Request:")
    pretty_print_json(params)
    
    asyncio.run(send_request(params, req_url))

if __name__ == "__main__":
    main()
