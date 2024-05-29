import requests

url="https://www.geeksforgeeks.org/courses?source=google&medium=cpc&device=c&keyword=geeksforgeeks&matchtype=e&campaignid=20039445781&adgroup=147845288105&gad_source=1&gclid=CjwKCAjwgdayBhBQEiwAXhMxthi22uUIGEvDQ2sBmQXx2shbFVH3VNJTJlvkUGRKh509HNGUN5AOMhoCWgIQAvD_BwE"
r=requests.get(url)
print(r.status_code)
print(r.text)                # Content of the response

data = {
    'name': 'Geeks',
    'description': 'A computer science portal'
}
r1 = requests.post('https://httpbin.org/post', data)
print(r1.status_code)
print(r1.text)

response = requests.put('https://httpbin.org/put', data=data)
print(response.status_code)
print(response.text) 

response1 = requests.delete('https://httpbin.org/delete')
print(response1.status_code)
print(response1.text)  

response3 = requests.head(url)
print(response3.status_code)  
print(response3.headers)

data2 = {
    'description': 'Partially updated description'
}

response = requests.patch(url,data=data2)
print(response.status_code)
print(response.text)

params = {
    'search': 'python'
}

response = requests.get(url, params=params)
print(response.status_code)
print(response.url)  # Final URL with query parameters
print(response.text)

