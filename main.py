from moviepy.editor import VideoFileClip

clip=VideoFileClip("video.mp4")
clip.write_gif("mysecgif.gif",fps=10)
