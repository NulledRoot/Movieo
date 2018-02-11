import glob, os
from shutil import copyfile, move
from subliminal import download_best_subtitles, save_subtitles, scan_videos
from babelfish import Language

#Vuse Torrent Default: userProf + "/Documents/Vuze Downloads"
#BiglyBT Torrent Default: userProf + "/Documents/BiglyBT Downloads"

__author__ = "TooSlepy"
__PyVer__ = "3.6"
userProf = os.getenv("userprofile")
videoSaveLoc = userProf + "/Documents/Vuze Downloads"
saveLoc = "D:/Moviex/"
lang = "eng"

os.chdir(videoSaveLoc)
for x in ("*.avi", "*.mkv", "*.mp4", "*.mpg"):
    for file in glob.glob(x):
        fileDir = file.rsplit('.', 1)[0]
        if not os.path.exists(fileDir):
            os.mkdir(fileDir)
        move(file, fileDir + "/" + file)
        # scan for videos in a folder
        videos = scan_videos(fileDir)
        # download best subtitles
        subtitles = download_best_subtitles(videos, {Language(lang)})
        # save them to disk, next to the video
        for v in videos:
            save_subtitles(v, subtitles[v])
        move(fileDir, saveLoc + "/" + fileDir)
        print(file + " has been moved and subtitled.")