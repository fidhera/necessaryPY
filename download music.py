# Downloader Youtube
import os
from pytube import YouTube
from moviepy.editor import AudioFileClip

def download_audio_from_youtube(youtube_url, output_filename):
    try:
        # Create a PyTube object and get the audio stream
        yt = YouTube(youtube_url)
        audio_stream = yt.streams.filter(only_audio=True).first()

        if not audio_stream:
            print("No audio stream found.")
            return

        # Download the audio stream as a temporary file
        temp_file = audio_stream.download(filename="temp_audio.mp4")

        # Convert the audio stream to an MP3 file using MoviePy
        audio_clip = AudioFileClip(temp_file)

        # Define the Downloads directory path
        downloads_directory = os.path.join(os.path.expanduser("~"), "Downloads")

        # Ensure the Downloads directory exists
        if not os.path.exists(downloads_directory):
            os.makedirs(downloads_directory)

        # Define the full path for the MP3 file
        mp3_file = os.path.join(downloads_directory, output_filename + ".mp3")

        # Write the audio file in MP3 format
        audio_clip.write_audiofile(mp3_file, codec='mp3')

        # Close the audio clip to release resources
        audio_clip.close()

        # Clean up the temporary file
        os.remove(temp_file)

        print("Audio extracted and saved as MP3 file to", mp3_file)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    # Input YouTube URL and output filename from user
    youtube_url = input("Enter the YouTube URL: ")
    output_filename = input("Enter the desired output filename (without extension): ")

    download_audio_from_youtube(youtube_url, output_filename)
