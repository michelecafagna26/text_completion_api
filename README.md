# Text Completion API
A simple text completion API using GPT-J-6B.
The API follows the [OpenAPI 3.0](https://swagger.io/specification/) specification

## Basic Requirements
- Python 3.9
- Pytorch > 1.1.0

## Usage
Clone this repo:
```bash
git clone git@github.com:michelecafagna26/text_completion_api.git
```
### Create a virtual environment
I suggest to use a Python3.9 virtual environment
```bash
python3.9 -m venv venv
source venv/bin/activate

# optional
pip install --upgrade pip
```
This repo has been tested with:

```txt
torch                    2.0.0
torchaudio               2.0.1
torchvision              0.15.1
CUDA Version             12.0
```

Install pytorch (preferebly with gpu support) compatible with your system:
```bash
pip3 install torch torchvision torchaudio
```
check [here](https://pytorch.org/get-started/previous-versions/) for older versions.

## Install the dependencies
```bash
cd text_completion_api/service
pip install -r requirements.txt
```
# Run the server
To run the server on localhost, run:
```bash
python3 -m text_completion_service
```
navigate to 
```
http://127.0.0.1:9994/api/ui/
```
You will see the Swagger UI from where you can test the API.

You'll see a single endpoint ```(post)/completion```. Press on the `Try it out` button and edit the request with your prompt. For example:

```json
{
  "prompt": "Hello world! How"
}
```
The first request will take longer, due to the model initialization overhead. However successive requests will be faster.

You should receive a response like this:
```json
{
  "completions": [
    "Hello world! How are you doing? I'm good. I have a",
    "Hello world! How are you? I am doing great. I am so",
    "Hello world! How are you?\n\nI am not sure if you",
    "Hello world! How are you? I am good, thanks for asking.",
    "Hello world! How are you? I hope you are doing great. Today"
  ]
}
```
# Further optimizations (optional)
if your GPU supports 8-bit precision, you can save extra GPU memory by loading the model in 8bits.

To enable it, edit the file:
```
text_completion_api/service/text_completion_service/core/config.py
```
and set  ```LOAD_IN_8BIT = True``` before running the server.

In the ```config.py``` file you can also find other parameters related to the generation.

## Hardware
This code has been tested on a 2-gpu server:
> NVIDIA TITAN Xp 12GB

> NVIDIA GeForce RTX 2080 Ti 11GB
