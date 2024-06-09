from flask import Flask, render_template, request, redirect, url_for, flash
import os
from pytube import YouTube
# from instascrape import Reel
import time 

app = Flask(__name__)
app.secret_key = '1234'

# Function to download YouTube video
def download_yt_v(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path)
        return True
    except Exception as e:
        print("Error:", str(e))
        return False

# Function to download Instagram reel
# def download_instagram_reel(url, output_path):
#     try:
#         SESSIONID = "blah blah"
 
#         headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)\AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.74 \Safari/537.36 Edg/79.0.309.43","cookie": f'sessionid={SESSIONID};'}
#         insta_reel = Reel(url)
#         insta_reel.scrape(headers=headers)
#         insta_reel.download(fp=f".\\Desktop\\reel{int(time.time())}.mp4")
#         print('Downloaded Successfully.')
#     except Exception as e:
#         print("Error:", str(e))
#         return False
# def download_instagram_reel(url, output_path, headers):
#     try:
#         insta_reel = Reel(url)
#         insta_reel.scrape(headers=headers)
#         insta_reel.download(fp=output_path)
#         return True
#     except Exception as e:
#         print("Error downloading Instagram reel:", str(e))
#         return False
    
@app.route('/home')
def index():
    return render_template('indexx.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    platform = request.form['platform']
    output_path = 'downloads/'

    if platform == 'youtube':
        if download_yt_v(url, output_path):
            flash('YouTube video downloaded successfully!', 'success')
        else:
            flash('Failed to download YouTube video. Please check the URL and try again.', 'error')
    # elif platform == 'instagram':
    #     if download_instagram_reel(url, output_path):
    #         flash('Instagram reel downloaded successfully!', 'success')
    #     else:
    #         flash('Failed to download Instagram reel. Please check the URL and try again.', 'error')
    else:
        flash('Invalid platform selected.', 'error')

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)