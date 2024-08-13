from flask import Flask, render_template
import os

app = Flask(__name__)

VIDEO_DIR = os.path.join(app.static_folder, 'videos')

@app.route('/')
def index():
    video_files = [f for f in os.listdir(VIDEO_DIR) if f.endswith('.mp4')]
    return render_template('index.html', videos=video_files)

if __name__ == '__main__':
    app.run(debug=True)
