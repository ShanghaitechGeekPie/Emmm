for i,t in enumerate(range(0,300,10)):
    print "mkdir {0} && ffmpeg -ss 00:{1:02d}:{2:02d} -t 00:00:10 -i ~/Videos/GOPR0025.MP4 -pix_fmt yuv420p -an {0}/clip.mp4".format(i,t//60,t%60)

