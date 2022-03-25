from os import name
import string

class Social_media:
    def __init__(self,name):
        self._name=name

    @property  #getter
    def getName(self):
        return self._name
     
#------------------------------------------- 

class Twitter(Social_media):

    def __init__(self, name,t_list,type):
        super().__init__(name)
        self.t_list=[] 
        self._type=type
    def CreatNewTweeter(self):
        tweet=input("enter tweet  ")
        print("tweet is",tweet) 
        if len(tweet) < 280:
            self.t_list.append(tweet)

        else:
            print("Error")
            
    def getTweeter(self):
        return self.t_list                  


 
class Instagram(Social_media):

    def __init__(self, name,p_list,Type):
        super().__init__(name)
        self.post_list=[] 
        self._Type=Type
    def PublishNewPost(self):
        post=input("enter post  ")
        print("post is",post)
        if len(post) < 2200:
            self.p_list.append(post)
        else:
            print("Error")
                 
    def getPost(self):
        return self.p_list

 

T=Twitter("t1",[],"persiantweeter" )
T.CreatNewTweeter()  
print(T.getTweeter())

 