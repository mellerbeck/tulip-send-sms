"""
Send SMS from
"""
import json
import boto3
import logging
import os

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

sns = boto3.client('sns')

def lambda_handler(event, context):

    try:
        phone_number = event['queryStringParameters']['phone_number']
        the_message = event['queryStringParameters']['message']
        sns.publish(PhoneNumber = phone_number, Message=the_message)
    except Exception as e:
        logging.error(e)
        logging.error("Error trying to update endpoint")
        
        html = "<html><head><title>HTML from API Gateway/Lambda</title></head><body><h2>fail</h2></body></html>"
        return {
            "statusCode": 404,
            "body": html,
            "headers": {"Content-Type": "text/html"}
        }
    
    html = "<html><head><title>HTML from API Gateway/Lambda</title></head><body><h2>sent</h2></body></html>"

    return {
        "statusCode": 200,
        "body": html,
        "headers": {"Content-Type": "text/html"}
    }
