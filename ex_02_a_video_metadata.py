from videoprops import get_video_properties

props = get_video_properties('data/video.h264')

print (props.keys())

# Ausgabe alle Werte:
for k in props.keys():
    print("%s : %s" % (k, props[k]))


# Ausgabe einzelner Werte, z.B. Breite und Hoehe
w = props['width']
h = props['height']
print("Dimension: (%s , %s)" % (w,h))