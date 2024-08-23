import requests

r = requests.get('https://liaoxuefeng.com/books/python/third-party-modules/requests/index.html',
                 params={'q': 'python', 'cat': '1001'},
                 headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'})
print(r.url)
print(r.status_code)
print(r.headers)

