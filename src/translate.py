import json
import logging
import decimalencoder
import todoList


def translate(event, context):
    data = json.loads(event['pathParameters'])
    if 'id' not in data or 'lang' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't translate the todo item.")
        return
    logging.log('INFO', "Query string:" + data)
    # translate text
    result = todoList.translate(event['pathParameters']['id'], 
                                event['pathParameters']['lang'])

    logging.log('INFO', "Received response:" + str(result))
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result,
                           cls=decimalencoder.DecimalEncoder)
    }
    logging.log('INFO', "Response is: " + response)
    return response
