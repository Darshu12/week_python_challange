
import requests




def get_all_dress():
    URL="http://localhost:3000/dresses"
    response=requests.get(URL)
    data=response.json()
    for x in data:
        id=x.get('id')
        color=x.get('color')
        print("id=",id)
        print("color=",color)

get_all_dress()



def get_all_makeups():
    URL="http://localhost:3000/makeups"
    response=requests.get(URL)
    data=response.json()
    for x in data:
        id=x.get('id')
        items=x.get('item')
        print("id=",id)
        print("items=",items)
get_all_makeups()





def delet_dresses():
     num=int(input("enter the number for delete:"))
     URL=f"http://localhost:3000/dresses/{num}"
     response=requests.delete(URL)
     print(response)

    
delet_dresses()


def delet_makeup():
     num=int(input("enter the number for delete:"))
     URL=f"http://localhost:3000/makeups/{num}"
     response=requests.delete(URL)
     print(response)

    
delet_makeup()
     