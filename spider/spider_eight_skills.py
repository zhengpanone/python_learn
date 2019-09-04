import urllib.request

"""
get 方法
"""
def func_01_get():
    url = "http://stackoverflow.com"
    
    response = urllib.request.urlopen(url)
    print(response.read().decode("utf-8"))

"""
post方法
"""
def func_01_post():
    url = "http://stackoverflow.com"
    form = {"name":"abc","password":"1234"}
    form_data = urllib.urlencode(form)
    request = urllib.Request(url,form_data)
    response = urllib.request.urlopen(request)
    print(response.read())

"""
使用代理IP
"""
def func_02_proxyIP():
    proxy = urllib.ProxyHandler({"http":"127.0.0.1:8080"})
    

       
if __name__ == "__main__":
    func_01_get()