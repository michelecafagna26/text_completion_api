import connexion
import six

from text_completion_service.models.completion_request import CompletionRequest  # noqa: E501
from text_completion_service.models.completion_response import CompletionResponse  # noqa: E501

from text_completion_service.core.generator import TextGenerator


def completion(completion_request):  # noqa: E501
    """Provide 5 text completion suggestions for a given prompt

     # noqa: E501

    :param completion_request:
    :type completion_request: dict | bytes

    :rtype: CompletionResponse
    """
    if connexion.request.is_json:
        completion_request = CompletionRequest.from_dict(connexion.request.get_json())  # noqa: E501

        text_generator = TextGenerator()
        output_sequences = text_generator.predict(prompt=completion_request.prompt)

        return CompletionResponse(completions=output_sequences)
