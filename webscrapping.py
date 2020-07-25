import urllib.request

with urllib.request.urlopen("https://openweathermap.org/find?q=bangalore") as url:
    s = url.read()
    # I'm guessing this would output the html source code ?
    print(s[600:1200])
