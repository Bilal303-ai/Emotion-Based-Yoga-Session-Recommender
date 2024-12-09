from transformers import pipeline
from sessions import sessions
import torchaudio
import torchaudio.transforms as T
import gradio as gr

pipe = pipeline(
    "audio-classification",
    model="BilalHasan/distilhubert-finetuned-ravdess",
)

audio_batch = []
def split_audio(array):
    len_of_each_array = 30 * 16000
    arr1, arr2 = array[0: len_of_each_array], array[int(len_of_each_array / 2):]
    audio_batch.append(arr1)
    if len(arr2) > len_of_each_array:
        split_audio(arr2)
    else:
        audio_batch.append(arr2)
    return audio_batch


def prediction(path):
    predictions = []
    array, sr = torchaudio.load(path)
    resampler = T.Resample(sr, 16000)
    resampled_audio = resampler(array)
    audio_batch = split_audio(resampled_audio[0].numpy())
    for i in range(len(audio_batch)):
        predictions.append(pipe(audio_batch[i])[0]['label'])
    mood = max(set(predictions), key = predictions.count)
    if mood in ['neutral', 'calm', 'happy', 'surprised']:
        mood = 'other'
    session = sessions.mood2session[mood]
    return mood, session


demo = gr.Interface(
    fn=prediction,
    inputs=[gr.Audio(type="filepath")],
    outputs=[gr.Textbox(label="Mood"), gr.Textbox(label="Recommended Yoga Session")]
)
demo.launch(debug=True)
