from pytube import YouTube

DOWNLOAD_FOLDER = "/home/ds/Download"

video_url = "https://www.youtube.com/watch?v=ofChsLBfBp0&list=RDMMofChsLBfBp0&start_radio=1"

video_obj = YouTube(video_url)

stream = video_obj.streams.get_highest_resolution()

stream.download(DOWNLOAD_FOLDER)
