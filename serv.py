!!!!!!!!!!!!!!!ai
!pip install typing_extensions==4.4.0
import typing_extensions
from importlib import reload
reload(typing_extensions)
!pip install azure.ai.ml

# `pip3 install assemblyai` (macOS)
# `pip install assemblyai` (Windows)
import assemblyai as aai
aai.settings.api_key = "0ef1aaaef3de40b582e4cc9e27fc6f24"
transcriber = aai.Transcriber()
# transcript = transcriber.transcribe("https://assembly.ai/news.mp4")
transcript = transcriber.transcribe(r"H:\from_500GB\new\techworld-with-nana - devops-bootcamp-video/lesson7.mp4")
srt = transcript.export_subtitles_srt()
with open(r"H:\from_500GB\new\techworld-with-nana - devops-bootcamp-video/lesson7.srt", "w") as f:
    f.write(srt)

!translatesubs "H:\from_500GB\new\techworld-with-nana - devops-bootcamp-video/lesson1.srt" "H:\from_500GB\new\techworld-with-nana - devops-bootcamp-video/lesson1ru.srt" --to_lang ru --merge
