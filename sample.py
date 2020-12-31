#Build a file-based key-value data store that supports the basic CRD (create, read, and delete) operations.
#Run the module of main file and import mainfile as a library(Mainfile = code.py)
#importing the main file
import code as c

#A new key-value pair can be added to the data store using the Create operation
c.create("ab@99",22) #Invalind key_name

c.create("anushaa",36) #valid key_name

#key already exists
c.create("anushaa",44)

#A Read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object
c.read("anushaa")

#timeout in create operation
c.create("apples",54,60)  #timeout value is 60sec

#after one min
c.read("apples")

#given key does not exist in database
c.read("avocados")

# delete operation
c.delete("anushaa")

#delete expired key
c.delete("apples")

#given key does not in database
c.delete("blueberries")

#after deleting key
c.read("anushaa")

#we can access these using multiple threads like
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
