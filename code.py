#Python 3.0 and above is used
import threading 
from threading import*
import time
#To store data, I used dictionary 'd'
d={} 

#For create operation, I also use syntax "create(key_name,value,timeout_value)"
def create(key,value,timeout_value=0): 
    if key in d:
        print("error: this key already exists") #print if key is generated already
    else:
        if(key.isalpha()):
            if len(d)<(1024*1020*1024) and value<=(16*1024*1024): #The file size never exceeds 1GB and The value is always a JSON object - capped at 16KB.
                if timeout==0:
                    l=[value,timeout_value]
                else:
                    l=[value,time.time()+timeout_value]
                if len(key)<=32: #The key is always a string - capped at 32chars
                    d[key]=l
            else:
                print("error: Memory limit exceeded!! ")#print if memory limit exceed
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")#print if the key_name is not string

#For read operation, I use syntax "read(key_name)"
def read(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #print if key is not created
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #Comparing the present time with expiry time
                string=str(key)+":"+str(b[0]) #To return "key_name:value"  in the format of Json Object
                return string
            else:
                print("error: time-to-live of",key,"has expired") #if time is expired
        else:
            string=str(key)+":"+str(b[0])
            return string

#for delete operation, I use syntax "delete(key_name)"
def delete(key):
    if key not in d:
        print("error: given key does not exist in database. Please enter a valid key") #print if key is not created
    else:
        b=d[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the current time with expiry time
                del d[key]
                print("key is successfully deleted")# key is deleted
            else:
                print("error: time-to-live of",key,"has expired") #if time is expired
        else:
            del d[key]
            print("key is successfully deleted")# key is deleted 


