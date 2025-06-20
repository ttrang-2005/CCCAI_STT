# -*- coding: utf-8 -*-
"""Wav2vec2.0

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1iUynoLpLpGGN7w8IrrNIVSye0OlEopQl
"""

!pip install --upgrade transformers

import transformers
print(transformers.__version__)

"""### Import Libraries"""

import librosa
import torch
import IPython.display as display
from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
import numpy as np

"""### Load pre-trained Wav2Vec model"""

#load pre-trained model and tokenizer
tokenizer = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

"""### Load Audio file"""

#load audio file
audio, sampling_rate = librosa.load("/content/4-2022-01-21-20-47-52 1 (1).mp3",sr=16000)

audio,sampling_rate

"""# Play the Audio"""

# audio
display.Audio("/content/4-2022-01-21-20-47-52 1 (1).mp3", autoplay=True)

"""### Speech to Text"""

input_values = tokenizer(audio, return_tensors = 'pt').input_values
input_values

# store logits (non-normalized predictions)
logits = model(input_values).logits
logits

# store predicted id's
# pass the logit values to softmax to get the predicted values
predicted_ids = torch.argmax(logits, dim =-1)

# pass the prediction to the tokenzer decode to get the transcription
transcriptions = tokenizer.decode(predicted_ids[0])

transcriptions