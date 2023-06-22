from pytube import YouTube
import re
import os

def sanitize_filename(filename, replacement='_'):
	invalid_chars_pattern = re.compile(r'[<>:"/\\|?*]')

	# replace the invalid characters with the replacement character
	sanitized_filename = invalid_chars_pattern.sub(replacement, filename)

	return sanitized_filename


def download(urls):
	all = len(str(len(urls)))

	for i, url in enumerate(urls):
		SAVE_PATH = "D:\\ReactJs" #to_do

		link=url

		while 1:
			try:
				yt = YouTube(link)
				title = yt.title

				name = sanitize_filename(f"{str(i+1).zfill(all)}-{title}.mp4")
				print(name)

				path = f"{SAVE_PATH}\\{name}"
				if os.path.exists(path):
					print(f"{name} downloaded already")

				else:
					yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(filename=name,output_path=SAVE_PATH)
					print(f"{name} downloaded successfully")
				break
			except:
				pass



videos = [
  "https://www.youtube.com/watch?v=pBgnb1L8OzI",
  "https://www.youtube.com/watch?v=lXaip0PMnKM",
  "https://www.youtube.com/watch?v=D0pIuwWU7x0",
  "https://www.youtube.com/watch?v=e8uAqkw8g6c",
  "https://www.youtube.com/watch?v=R0sg13seWbI",
  "https://www.youtube.com/watch?v=etnJuly1gE0",
  "https://www.youtube.com/watch?v=denycZ1vVzs",
  "https://www.youtube.com/watch?v=L51a5afyFag",
  "https://www.youtube.com/watch?v=U679hiarLoE",
  "https://www.youtube.com/watch?v=kVmoEwb230c",
  "https://www.youtube.com/watch?v=TMQvKXyecuA",
  "https://www.youtube.com/watch?v=FO7vlWhNw9A",
  "https://www.youtube.com/watch?v=1cHUIwc_Pfg",
  "https://www.youtube.com/watch?v=Sw2XLiStcuk",
  "https://www.youtube.com/watch?v=Y1RrCzL7kkc",
  "https://www.youtube.com/watch?v=25kr91D9Gi4",
  "https://www.youtube.com/watch?v=rcrDGngRbeg",
  "https://www.youtube.com/watch?v=SQlo93yXObg",
  "https://www.youtube.com/watch?v=MJQRfMA-sNc",
  "https://www.youtube.com/watch?v=zSnevjNpZ2A",
  "https://www.youtube.com/watch?v=hqdoAHPk75w",
  "https://www.youtube.com/watch?v=c9EFnIRtXhI",
  "https://www.youtube.com/watch?v=wkMmLce77ZE",
  "https://www.youtube.com/watch?v=h0VSKf-N1Ec",
  "https://www.youtube.com/watch?v=8DN0MLXgASM",
  "https://www.youtube.com/watch?v=UOO8y7Y7aLg",
  "https://www.youtube.com/watch?v=jat22DNNzjk",
  "https://www.youtube.com/watch?v=3GuDq-4hiSY",
  "https://www.youtube.com/watch?v=YpVkocx8z0I",
  "https://www.youtube.com/watch?v=XkOLlW2ARKQ",
  "https://www.youtube.com/watch?v=MOQtamyQS3g",
  "https://www.youtube.com/watch?v=1NKcTb3KTUw",
  "https://www.youtube.com/watch?v=w07xY-AftO0",
  "https://www.youtube.com/watch?v=pMFTGZqMq7U",
  "https://www.youtube.com/watch?v=VqtlkGklX04",
  "https://www.youtube.com/watch?v=7YW23b2DDGM",
  "https://www.youtube.com/watch?v=pZS6hhsiHy0",
  "https://www.youtube.com/watch?v=t9DJM3Ma2JQ",
  "https://www.youtube.com/watch?v=e8FMZs5o2Io",
  "https://www.youtube.com/watch?v=lIGh1w52IFQ",
  "https://www.youtube.com/watch?v=824cqQWYWpk",
  "https://www.youtube.com/watch?v=-bedMWu5RqI",
  "https://www.youtube.com/watch?v=06GvVe_Z6P0",
  "https://www.youtube.com/watch?v=H2ODE2rrsiY",
  "https://www.youtube.com/watch?v=ufiGjDGJpYc",
  "https://www.youtube.com/watch?v=iquOTU-nJTs",
  "https://www.youtube.com/watch?v=nTjAEah8YM4",
  "https://www.youtube.com/watch?v=1Dx7j5-5XB0",
  "https://www.youtube.com/watch?v=NZ4wsy4mhIY",
  "https://www.youtube.com/watch?v=gtDjNukVlVA",
  "https://www.youtube.com/watch?v=gMdG3ViyYok",
  "https://www.youtube.com/watch?v=_y1aCB20U5c",
  "https://www.youtube.com/watch?v=R1R30InLJg4",
  "https://www.youtube.com/watch?v=R5qQXvPA9L0",
  "https://www.youtube.com/watch?v=iQI1o4ZzQNM",
  "https://www.youtube.com/watch?v=SBFEpF4RXSg",
  "https://www.youtube.com/watch?v=IoPQunhiQAY",
  "https://www.youtube.com/watch?v=FfMdNWIqles",
  "https://www.youtube.com/watch?v=KwWIrzEofGc",
  "https://www.youtube.com/watch?v=DVntLyvhlyk",
  "https://www.youtube.com/watch?v=A9qqjvZC53I",
  "https://www.youtube.com/watch?v=hqz4xHdnusg",
  "https://www.youtube.com/watch?v=nJBs73MIwmk",
  "https://www.youtube.com/watch?v=Ms0B4QgrouA",
  "https://www.youtube.com/watch?v=Pvj0qklINws",
  "https://www.youtube.com/watch?v=P2gF_QFZ8tw",
  "https://www.youtube.com/watch?v=99RSqp54UgM",
  "https://www.youtube.com/watch?v=P1YrWcNCyiE",
  "https://www.youtube.com/watch?v=9Jyl3Uu8BKY",
  "https://www.youtube.com/watch?v=2RBKvO2xEe4",
  "https://www.youtube.com/watch?v=SUXNGjU7Vjk"
]

download(videos)
