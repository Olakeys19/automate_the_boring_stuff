# # GENERATING SPEECH AUDIO WITH PYTTSX3
# import pyttsx3
# engine = pyttsx3.init()
# engine.say('Hello. How are you doing?')
# engine.runAndWait()  # The computer speaks.
# feeling = input('>')
# engine.say('Yes. I am feeling ' + feeling + ' as well.')
# engine.runAndWait()  # The computer speaks again.


# # Getting Properties
# import pyttsx3
# engine = pyttsx3.init()
# engine.getProperty('volume')
# engine.getProperty('rate')
# engine.getProperty('voices')

# # Get available voices
# for voice in engine.getProperty('voices'):
#     print(voice.name, voice.gender, voice.age, voice.languages)

# # Change voice settings
# engine.setProperty('rate', 300)     # Speed percent (can go over 100)
# engine.setProperty('volume', 0.5)   # Volume 0-1
# voices = engine.getProperty('voices')           # Get available voices
# engine.setProperty('voice', voices[1].id)       # Change to second voice
# engine.say('The quick brown fox jumps over the yellow lazy dog.')   
# engine.runAndWait()     # This method must be called to process the voice commands and make the computer speak.


# # Saving Speech Audio to WAV Files
# import pyttsx3
# engine = pyttsx3.init()
# engine.save_to_file('Hello. How are you doing?', 'hello.wav')
# engine.runAndWait()  # The computer creates hello.wav.

# # NOTE: The pyttsx3 module can save .wav files only, not .mp3 files or any other audio format.


# # SPEECH RECOGNITION
# import os
# import whisper
# model = whisper.load_model("base")      # Load the whisper model
# result = model.transcribe("hello.wav")  # Transcribe the audio file
# print(result['text'])                   # Print the transcribed text, the text attributes of the result dictionary contains the transcribed text.

# # Specifying language
# model.transcribe('hello.wav', language='English')       # 

# # To use the GPU, replace the whisper.load_model('base') code in this chapter with whisper.load_model('base', device='cuda').


# # Creating Subtitle Files
# import whisper
# model = whisper.load_model('base')          # Load the whisper model
# result = model.transcribe('_Prison_Break_Season_1_Episode_3_720p_@Tv_Series_ETY_.mkv')      # Transcribe the audio file
# write_function = whisper.utils.get_writer('srt', '.')       # first argument is the subtitle format, second argument is the output directory
# write_function(result, 'audio')         # Write the subtitle file to audio.srt. The first argument is the result dictionary, the second argument is the output file name without extension.


# Downloading Videos From Websites
import yt_dlp               # The yt_dlp module is a fork of the youtube-dl module. It can download videos from YouTube and other websites.
video_url = 'https://youtu.be/X309yhLouKs?si=SksE_uMklAGcQeEO'
with yt_dlp.YoutubeDL() as ydl:
    ydl.download([video_url])       # The download() method downloads the video from the specified URL. The argument is a list of URLs, so you can download multiple videos at once by passing a list of URLs to the download() method.


# # Extracting Audio From Videos
# import yt_dlp
# video_url = 'https://youtu.be/X309yhLouKs?si=SksE_uMklAGcQeEO'
# options = {
#     'quiet': True,  # Suppress the output.
#     'no_warnings': True,  # Suppress warnings.
#     'outtmpl': 'downloaded_content.%(ext)s',    # The output template specifies the name of the downloaded file. The %(ext)s placeholder will be replaced with the appropriate file extension based on the format of the downloaded content.
#     'format': 'm4a/bestaudio/best', 'postprocessors': [{  # Extract audio using ffmpeg.
#         'key': 'FFmpegExtractAudio',    # The key specifies the postprocessor to use. In this case, we are using the FFmpegExtractAudio postprocessor to extract audio from the downloaded video.
#         'preferredcodec': 'm4a',    # The preferred codec specifies the audio codec to use for the extracted audio. In this case, we are using the m4a codec.
#         }]
#     }

# with yt_dlp.YoutubeDL(options) as ydl:
#     ydl.download([video_url])

# # Getting the exact name of the downloaded audio file
# from pathlib import Path            # The Path class is used to work with file paths. It provides methods to manipulate file paths and perform operations on files and directories.
# matching_filenames = list(Path().glob('downloaded_content.*'))      # The glob() method returns a generator that yields all the file paths that match the specified pattern. In this case, we are looking for files that start with 'downloaded_content.' and have any file extension. The list() function converts the generator to a list of file paths.
# downloaded_filename = str(matching_filenames[0])        # The first element of the list is the exact name of the downloaded audio file. We convert it to a string to get the file name as a string.
# print(downloaded_filename)  

# # Downloading only video metadata
# import yt_dlp, json
# video_url = 'https://www.youtube.com/watch?v=kSrnLbioN6w'
# options = {
#     'quiet': True,  # Suppress the output.
#     'no_warnings': True,  # Suppress warnings.
#     'skip_download': True,  # Do not download the video.
# }

# with yt_dlp.YoutubeDL(options) as ydl:
#     info = ydl.extract_info(video_url)      # Extract the video metadata. The extract_info() method returns a dictionary containing the metadata of the video, including the title, description, uploader, upload date, duration, view count, like count, dislike count, and more.
#     json_info = ydl.sanitize_info(info)     # Sanitize the metadata dictionary. The sanitize_info() method removes any sensitive information from the metadata dictionary, such as the uploader's email address or phone number.
#     print('TITLE:', json_info['title'])  # Print the video title.
#     print('KEYS:', json_info.keys())    # Print the keys of the metadata dictionary.
#     with open('metadata.json', 'w', encoding='utf-8') as json_file:
#         json_file.write(json.dumps(json_info))

