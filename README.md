**Freshworks Assignment**

Build a file-based key-value data store that supports the basic CRD (create, read, and delete)operations. This data store is meant to be used as a local storage for one single process on one

laptop. The data store must be exposed as a library to clients that can instantiate a class and work with the data store.

**The data store will support the following functional requirements.**

1. It can be initialized using an optional file path. If one is not provided, it will reliably create itself in a reasonable location on the laptop.

2. A new key-value pair can be added to the data store using the Create operation. The key

is always a string - capped at 32chars. The value is always a JSON object - capped at 16KB.

3. If Create is invoked for an existing key, an appropriate error must be returned.

4. A Read operation on a key can be performed by providing the key, and receiving the value in response, as a JSON object.

5. A Delete operation can be performed by providing the key.

6. Every key supports setting a Time-To-Live property when it is created. This property is optional. If provided, it will be evaluated as an integer defining the number of seconds the key must be retained in the data store. Once the Time-To-Live for a key has expired, the key will no longer be available for Read or Delete operations.

7. Appropriate error responses must always be returned to a client if it uses the data store in unexpected ways or breaches any limits.

**The data store will also support the following non-functional requirements.**

1. The size of the file storing data must never exceed 1GB.

2. More than one client process cannot be allowed to use the same file as a data store at any given time.

3. A client process is allowed to access the data store using multiple threads, if it desires to.The data store must therefore be thread-safe.

4. The client will bear as little memory costs as possible to use this data store, whilederiving maximum performance with respect to response times for accessing the data store.






**Follow the steps given to create a module in python**

The folder structure used to test the code is as follows:

modtest/

`	`**code.py**

`	`**sample.py**	

Step 1) Create a file and name it **code.py**

Step 2) Inside **code.py** create a functions called **create(),read(),delete()**

Step 3) Now create another file **sample.py**

Step 4) Inside **sample.py** import the **code.py** file, as shown below:

`            `**import code**

While importing, you don't have to mention the **code.py** but just the name of the file.

Step5)Then you can call the functions from **code.py** inside **sample.py**, you need to make use of **module\_name.function\_name**.

Step 6)When you execute **sample.py,** you will get the output

**Go through the code.py file, sample.py file and sample.pdf file that are attached here with in order to understand clearly how the code works and how to perform operations in this.**


**Reference:** 
- **key-value datastore - [**https://en.wikipedia.org/wiki/Key%E2%80%93value_database](https://www.google.com/url?q=https://en.wikipedia.org/wiki/Key%25E2%2580%2593value_database&sa=D&ust=1609430663989000&usg=AFQjCNGDBGrLknEvhFS9KqX922wSE9gvWg)**
- **JSON object            - [**https://www.w3schools.com/js/js_json_objects.asp](https://www.google.com/url?q=https://www.w3schools.com/js/js_json_objects.asp&sa=D&ust=1609430663989000&usg=AFQjCNHhIRysZXQuXFxEOvbtLWfkRWVARg)**
- **Thread Safety          - [**https://en.wikipedia.org/wiki/Thread_safety](https://www.google.com/url?q=https://en.wikipedia.org/wiki/Thread_safety&sa=D&ust=1609430663989000&usg=AFQjCNEJp8U0cc2vhn4AELpjh41Jod-sjg)**

