# OpenAI API Examples

![Running GIF](https://camo.githubusercontent.com/1140a4f2ffe1d7d5432df78421909e56c97909423568e609983ec3d4fbcb0b22/68747470733a2f2f726561646d652d747970696e672d7376672e6865726f6b756170702e636f6d3f666f6e743d4f72626974726f6e2673697a653d343026636f6c6f723d253233373941353030266865696768743d3637266475726174696f6e3d333030302663656e7465723d74727565266c696e65733d254630253946253835254236254630253946253836253831254630253946253835254234254630253946253835254234254630253946253836253833254630253946253835254238254630253946253835254244254630253946253835254236254630253946253836253832)




This repository contains examples of how to use the OpenAI API for different tasks. It demonstrates generating text using the GPT-3 model and creating images using the OpenAI API.

## Chatting with GPT-3 Model

### `chating.py`

This code demonstrates how to use the OpenAI API to generate text using the GPT-3 model. It showcases the completion API to generate text based on a prompt.

#### How the Code Works

The code interacts with the OpenAI API to generate text using the GPT-3 model. It does the following:

1. Sets the OpenAI API key.
2. Uses the completion API to generate text based on a given prompt.
3. Prints the generated text.

#### Usage

1. Sign up and obtain an API key from [OpenAI](https://beta.openai.com/signup/).
2. Replace `"API-Key"` with your actual OpenAI API key.

3. Run the script using a Python interpreter.

4. The script will generate text based on the prompt provided and print the output.

#### Additional Notes

- You can modify the `prompt` and `model` parameters to customize the generated text.
- The code also includes commented-out code demonstrating the usage of the chat completion API, which allows for more interactive conversations.

#### Requirements

- [OpenAI Python](https://github.com/openai/openai-python)

## Image Creation with OpenAI API

### `createimage.py`

This code demonstrates how to use the OpenAI API to create images. It generates images based on a given prompt.

#### How the Code Works

The code uses the OpenAI API to create images based on the provided prompt. It does the following:

1. Sets the OpenAI API key.
2. Specifies a prompt for the image.
3. Requests an image creation based on the prompt.
4. Prints the URL of the generated image.

#### Usage

1. Sign up and obtain an API key from [OpenAI](https://beta.openai.com/signup/).
2. Replace `"API-Key"` with your actual OpenAI API key.

3. Run the script using a Python interpreter.

4. The script will generate an image based on the prompt provided and print the URL of the image.

#### Additional Notes

- You can modify the `prompt`, `n`, and `size` parameters to customize the generated image.

#### Requirements

- [OpenAI Python](https://github.com/openai/openai-python)

  ![Running GIF](  https://raw.githubusercontent.com/trinib/trinib/82213791fa9ff58d3ca768ddd6de2489ec23ffca/images/footer.svg)
