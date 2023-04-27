# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from text_completion_service.models.completion_request import CompletionRequest  # noqa: E501
from text_completion_service.models.completion_response import CompletionResponse  # noqa: E501
from text_completion_service.test import BaseTestCase


class TestCompletionController(BaseTestCase):
    """CompletionController integration test stubs"""

    def test_completion(self):
        """Test case for completion

        Provide 5 text completion suggestions for a given prompt
        """
        completion_request = {
  "prompt" : "Hello world! How"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/api/completion',
            method='POST',
            headers=headers,
            data=json.dumps(completion_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
