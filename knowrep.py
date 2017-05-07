"""Knowledge representation: Frame Based"""



"""
Generic frame: Mental illness
Individual frame: Depression, Anxiety, Insomnia
"""

import datetime
import utils

"***************************************** frame based kb module *****************************************"
              
class Person:
    def __init__(self):
        "constructor"
    "slot1 = Name , filler = name (string)"
    def Name(self,name):
        try:
            self.Name = str(name)
        except ValueError:
            print "name must be a string"
    "slot2 = Age , filler = age (int)"
    def Age(self,age):
        try:
            self.Age = int(age)
        except ValueError:
            print "age must be an int"        
    "slot3 = Gender, filler = gender (string): F,M"
    def Gender(self,gender):
        def IF_ADDED(gender):
            if gender.lower() == 'male':
                return 'M'
            elif gender.lower() == 'female':
                return 'F'
        try:
            self.Gender = str(IF_ADDED(gender))
        except ValueError:
            print "gender must be a string"
        


        
class Patient(Person):
    def __init__(self):
        self.is_a = []
        self.is_a.append(Person)        
        self.as_instance = {}
        self.Symptoms = []
    "slot1 = IS_A, filler = frame (<class>)"
    def IS_A(self,frame):
        self.is_a.append(frame)
    "slot2 = IS_A, filler = frame (<class>)"
    def AS_INSTANCE(self, frame):
        "{ClassName : ClassInstance (Class())}"
        self.as_instance[frame.__name__] = frame()
    "slot3 = Symptoms , filler = symptom (Symptom)"
    def Symptoms(self,symptom):
        try:
            s = Symptom(symptom)
        except ValueError:
            print "symptom must be a Symptom object"
        
        
"Generic frame"
class TherapyPatient:
    def __init__(self):
        "list of Condition objects"
        self.Diagnosis = []
        self.as_instance = {}
    "slot1 = IS_A, filler = frame (<class>)"
    def AS_INSTANCE(self, frame):
        "{ClassName : ClassInstance (Class())}"
        self.as_instance[frame.__name__] = frame()
    "slot2 = Diagnosis , filler  = condition (Condition)"
    def Diagnosis(self,mentill):
        def IF_ADDED(mentill):
            if isinstance(mentill, MentalIllness):
                return mentill
        
        self.Diagnosis.append(IF_ADDED(mentill))
        

"Generic frame"
class Symptom:
    def __init__(self):
        self.Synonyms = []
    "slot1 = Name, filler = name (string)"
    def Name(self,name):
        try:
            self.Name = str(name)
        except ValueError:
            print "name must be a string"
    "slot2 = Synonyms, filler = synonym (string)"
    def Synonyms(self,synomym):
        try:
            self.Synonyms.append(str(synomym))
        except ValueError:
            print "synonym must be a string"
        

            
"Generic frame"
class Condition:
    def __init__(self):
        "constructor"
    "Slot1 = Name , filler = name (string)" 
    def Name(self,name):
        try:
            self.Name = str(name)
        except ValueError:
            print "name must be a string"
            
            
class MentalIllness(Condition):
    def __init__(self):
        self.is_a = []
        self.is_a.append(Condition)
        self.as_instance = {}
        self.PhysicalSymptoms = []
        self.EmotionalSymptoms = []
    "Slot1 = IS_A, filler = frame (<class>)" 
    def IS_A(self, frame):
        self.is_a.append(frame)
    "Slot2 = AS_INSTANCE , filler = frame (<class>)"
    def AS_INSTANCE(self, frame):
        "{ClassName : ClassInstance (Class())}"
        self.as_instance[frame.__name__] = frame()
    "Slot3  = PhysicalSymptoms, filler = symptom (Symptom)"
    def PhysicalSymptoms(self,symptom):
        self.PhysicalSymptoms.append(symptom)
    "Slot4 = EmotionalSymptoms, filler = symptom (Symptom)"
    def EmotionalSymptoms(self,symptom):
        self.EmotionalSymptoms.append(symptom)
        

if __name__ == '__main__': 
    """test"""
   
    "create Depression frame"
    depressionFrame = MentalIllness()
    depressionFrame.
    

    
 

   


"""
comments:       
    
    Basic idea (incomplete)
    *can even have a slot in patient that contains pointer to its respective directory4
    *ref - SLIDE 28 OF week_9_slides_v1
    
    -------------           -------------           --------------
    - Directory -----------> Patient    ----------->    Diagnosis
    -  (dir1)   -           _ (patient1)_           - (diagnosis1)
    -------------           -------------           --------------
    
"""

"""
questions:
    Can we have two seperate networks of frames?
        or do all the frames that exist have to be connected in one way or another?
    Do all the frames have to strictly be one module
        or can a knowldege base module have additional methods
"""

"""
TO DO:
    add procedures, if needed, if added
    in comments above each class comment in a frame structure with <>'s like in slides   
    remove comments following # later
    check with professor to see if this is all correct
"""




"""
notes/references:

http://www.cs.utexas.edu/users/qr/algy/algy-expsys/node2.html
-slots serve as pointers
-a slot can hold multiple values 

http://slideplayer.com/slide/6224186/
-in some cases a slot may have a procedure (which determines a value) instead of some value
-frame provides storing of knowledge in slots
-slot may contain a default value or a pointer to another frame, set of rules or a procedure by which slot value is obtained
    
"""


"""
        Frame(Generic) - Person
        -----------------------
        -
        - Name (string) 
        - Age (int)
        - Gender (string) 
        -
        -----------------------<-----------------Patient
                                                --------------------
        
            
        

"""