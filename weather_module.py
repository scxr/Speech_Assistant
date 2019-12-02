import urllib.request, json, ast
def gettemp(requested_location):
    with urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=API_KEY'%(requested_location)) as url:
        response = url.read()
    data = json.loads(response.decode('utf-8'))
    a=ast.literal_eval(json.dumps(data))
    main = a['main']
    temperature = int(main['temp']) - 273.15
    temperature = round(temperature,2)
    return temperature
