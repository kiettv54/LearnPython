import json;
items =  json.loads('[{"id":1,"text":"Item 1"},{"id":2,"text":"Item 2"}]')
for item in items:
   if item['id'] == 2:
       print(item) 
