#!/usr/bin/env python3
import argparse, json, sys
from tools import calculator, notes, weather_stub, file_writer

def plan_mock(task):
    steps=[]
    t = task.lower()
    if "weather" in t:
        steps.append({"id":1,"action":"weather","args":{"city":"Goa"}})
    if any(x in t for x in ["calculate","budget","sum","cost"]):
        steps.append({"id":2,"action":"calculator","args":{"numbers":[1000,2000]}})
    if any(x in t for x in ["save","write","file","store"]):
        steps.append({"id":3,"action":"file:write","args":{"filename":"out.txt","text":f"Result for: {task}"}})
    steps.append({"id":99,"action":"final","args":{"text":f"Completed mock plan for: {task}"}})
    return steps

def execute(steps):
    trace=[]
    for s in steps:
        act=s["action"]; args=s.get("args",{})
        if act=="calculator":
            res=calculator.calculator_tool(**args)
        elif act=="notes:add":
            res=notes.add_note(args.get("text",""))
        elif act=="file:write":
            res=file_writer.write_file(args.get("filename","out.txt"), args.get("text",""))
        elif act=="weather":
            res=weather_stub.get_weather(args.get("city",""))
        elif act=="final":
            res=args.get("text","")
        else:
            res=f"unknown action {act}"
        trace.append({"id": s.get("id"), "action": act, "args": args, "result": res})
    return trace

if __name__=="__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument('--task', required=True)
    parser.add_argument('--mode', default='mock')
    args=parser.parse_args()
    steps = plan_mock(args.task)
    trace = execute(steps)
    print(json.dumps({"task":args.task,"trace":trace}))
    sys.exit(0)
