import random
import urllib.request

#image download from website
def get_image_from_web(url):
    #randrage takes the parameter value as starting point and ending point
    name = random.randrange(1, 1000)
    #str(name) convert into string
    fullname = str(name) + ".jpg"
    urllib.request.urlretrieve(url,fullname)
#get_image_from_web("http://localhost/attendance/assets/img/logo.gif")