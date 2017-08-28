form urllib import request

get_url = 'http://localhost/dashboard/phpinfo.php'

def download_file(csv_url):
    #check the internet connection
    response = request.urlopen(csv_url)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goo.csv'
    fx = open(dest_url,"w")
    for line in lines:
        fx.write(line + '\n')
    fx.close()
download_file(get_url)