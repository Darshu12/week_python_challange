import requests
import json

def get_all_dresses():
    URL="http://localhost:3000/dresses"
    response=requests.get(URL)
    data=response.json()
    for x in data:
        num=x.get('num')
        color=x.get('color')
        type=x.get('type')
        print("num=",num)
        print("color=",color)
        print("type=",type)

def get_all_makeups():
    URL="http://localhost:3000/makeups"
    response=requests.get(URL)
    data=response.json()
    for x in data:
        id=x.get('id')
        items=x.get('item')
        print("id=",id)
        print("items=",items)

def delete_dresses():
     num=int(input("enter the number for delete dresses:"))
     URL=f"http://localhost:3000/dresses/{num}"
     response=requests.delete(URL)
     print(response)

def delete_makeup():
     num=int(input("enter the number for delete makeup:"))
     URL=f"http://localhost:3000/makeups/{num}"
     response=requests.delete(URL)
     print(response)

def insert_makeup():
     print
     URL="http://localhost:3000/makeups/"
     # dictionary -> python
     # Frontend needs JSON
     #  json.dumps: Dictionary       ->      JSON
     #  json.loads: JSON             ->      Dictionary 
     
     data={ 
            "id":7,
           "item":"blusher"
        }
     
     json_data = json.dumps(data)
    #  print(data, type(data))
    #  print(json_data, type(json_data))
     response=requests.post(URL,json_data)
     print(response.text)

def insert_dresses(): 
     URL="http://localhost:3000/dresses"
     data={ 
            "num":2,
           "color":"white",
           "type":"crop-top"
        }
     json_data=json.dumps(data)
     response=requests.post(URL,json_data)
     print(response)
     print(response.text)

print("1.get_all_dresses\n2.get_all_makeups\n3.delete_dresses\n4.delete_makeup\n5.insert_dresses\n6.insert_makeup")
ch=int(input("enter the number"))

if ch==1:
     get_all_dresses()
elif ch==2:
     get_all_makeups()
elif ch==3:
     delete_dresses()
elif ch==4:
     delete_makeup()
elif ch==5:
     insert_dresses()
elif ch==6:
     insert_makeup()
else:
     ("Invalid your choices:-")
