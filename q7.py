#CREATING MY ROBOT
class machine:
    def __init__(self,id,n,d,h):
        self.id='Robot.'
        self.name='Sonic3D.'
        self.department='software.'
        self.hobbies='coding.'
    def intro(self,id,n,d,h):
        print('I am a',self.id,'MY name is',self.name,'I work with',self.department,'My hobbies are',self.hobbies)

m= machine('id','n','d','h')
m.intro('id','n','d','h')