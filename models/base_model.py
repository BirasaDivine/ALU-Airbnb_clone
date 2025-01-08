#Create basemodel class withe the following attributes:
#1.id
#2.created_at
#3.updated_at
#4._str_:should print: [<class name>] (<self.id>) <self.__dict__>
#5.save:updates the public instance attribute updated_at with the current datetime
#6.to_dict:returns a dictionary containing all keys/values of __dict__ of the instance
#format:%Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
#you can use isoformat() of datetime object
from datetime import datetime
import uuid
import os
class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        return "({}) ({}) {}".format(self.__class__ .__name__,self.id,self.__dict__)
    
    def save(self):
        self.updated_at= datetime.now()
    
    