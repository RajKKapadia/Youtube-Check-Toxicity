from flask import Flask, request, jsonify
from flask_cors import CORS

from toxic_comment.logger import logging
from toxic_comment.model.model import check_text_toxicity

logger = logging.getLogger(__name__)

app = Flask(__name__)
CORS(app=app)

def get_formated_response(
    status,
    message,
    response
) -> dict:
    ''' Get formated response for the API\n
        Takes -> status, message, and base64\n
        Returns -> jsonified response
    '''
    return jsonify(
        {
            'status': status,
            'message': message,
            'response': response
        }
    )

@app.route('/')
def home():
    return 'OK'

@app.route('/api/text', methods=['POST'])
def api_text():
    logger.info('A new request came at /api/text')
    if request.is_json:
        body = request.get_json()
        logger.info(body)
        if 'text' in body.keys():
            result = check_text_toxicity(body['text'])
            return jsonify(result)
        else:
            logger.info('Request has no parameter text.')
            return get_formated_response(
                -1,
                'Request has no parameter text',
                {}
            )
    else:
        logger.info('Request has no body.')
        return get_formated_response(
            -1,
            'Request has no body.',
            {}
        )
