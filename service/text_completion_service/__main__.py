#!/usr/bin/env python3

import connexion
from flask_cors import CORS
from text_completion_service import encoder

app = connexion.App(__name__, specification_dir='./openapi/')


def main():
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('openapi.yaml',
                arguments={'title': 'Text Completion API'},
                pythonic_params=True)

    CORS(app.app)
    app.run(port=9994)


if __name__ == '__main__':
    main()
