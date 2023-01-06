import json
import logging
import decimalencoder
import todoList


def translate(event, context):
    data = json.loads(event['body'])
    if 'id' not in data or 'lang' not in data:
        logging.error("Validation Failed")
        raise Exception("Couldn't translate the todo item.")
        return
    # translate text
    logging.info("Path parameters: " + event['pathParameters'])
    # logging.info("Received ID:" + event['pathParameters']['id'])
    # logging.info("Received LANG:" + event['pathParameters']['lang'])
    logging.info("Received ID:" + event['pathParameters'][0])
    logging.info("Received LANG:" + event['pathParameters'][1])
    # result = todoList.translate(
    #    event['pathParameters']['id'],
    #    event['pathParameters']['lang'])
    result = todoList.translate(
        event['pathParameters'][0],
        event['pathParameters'][1])

    logging.log('INFO', "Received response:" + str(result))
    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result,
                           cls=decimalencoder.DecimalEncoder)
    }
    logging.log('INFO', "Response is: " + response)
    return response
