from flask import Flask,request,jsonify
import os
from dotenv import load_dotenv
from threading import Thread
import json
import requests
import pprint
import redis

try:
    # Connect to Redis
    print("connecting to redis....")
    r = redis.Redis(host='localhost', port=6379, db=0)
    print("connected to redis")
except Exception as e:
    print("Could  not connect to redis"+e)
    exit()

queue_name = "alphaQ"



