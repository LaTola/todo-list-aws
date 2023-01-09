import json
import logging
import todoList


def translate(event, context):
    # translate text
    result = todoList.translate(event['pathParameters']['id'],
                                event['pathParameters']['lang'])

    logging.info("Received response: " + str(result))
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result)
    }
    return response
