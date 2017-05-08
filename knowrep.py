"""Knowledge representation: Frame Based"""



"""
Generic frame: Mental illness
Individual frame: Depression, Anxiety, Insomnia
"""

import datetime
import utils
import sys

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
        self.symptoms = []
    "slot1 = IS_A, filler = frame (<class>)"
    def IS_A(self,frame):
        self.is_a.append(frame)
    "slot2 = IS_A, filler = frame (<class>)"
    def AS_INSTANCE(self, frame):
        "{ClassName : ClassInstance (Class())}"
        self.as_instance[frame.__name__] = frame()
    "slot3 = Symptoms , filler = symptom (Symptom)"
    def Symptoms(self,symptom):
        if isinstance(symptom, Symptom):
            self.symptoms.append(symptom)

        
"Generic frame"
class TherapyPatient:
    def __init__(self):
        "list of Condition objects"
        self.diagnosis = []
        self.as_instance = {}
    "slot1 = IS_A, filler = frame (<class>)"
    def AS_INSTANCE(self, frame):
        "{ClassName : ClassInstance (Class())}"
        self.as_instance[frame.__name__] = frame()
    "slot2 = Diagnosis , filler  = condition (Condition)"
    def Diagnosis(self,mentill):
        if isinstance(mentill, MentalIllness):
            self.diagnosis.append(mentill)


"Generic frame"
class Symptom:
    def __init__(self):
        self.synonyms = []
    "slot1 = Name, filler = name (string)"
    def Name(self,name):
        try:
            self.Name = str(name)
        except ValueError:
            print "name must be a string"
    "slot2 = Synonyms, filler = synonym (string)"
    def Synonyms(self,synonym):
        try:
            self.synonyms.append(str(synonym))
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
        self.phy_symptoms = []
        self.emo_symptoms = []
    "Slot1 = IS_A, filler = frame (<class>)" 
    def IS_A(self, frame):
        self.is_a.append(frame)
    "Slot2 = AS_INSTANCE , filler = frame (<class>)"
    def AS_INSTANCE(self, frame):
        "{ClassName : ClassInstance (Class())}"
        self.as_instance[frame.__name__] = frame()
    "Slot3  = PhysicalSymptoms, filler = symptom (Symptom)"
    def PhysicalSymptoms(self,symptom):
        self.phy_symptoms.append(symptom)
    "Slot4 = EmotionalSymptoms, filler = symptom (Symptom)"
    def EmotionalSymptoms(self,symptom):
        self.emo_symptoms.append(symptom)
        

if __name__ == '__main__': 
    """test"""
   
    "create Depression frame"
    depressionFrame = MentalIllness()
    depressionFrame.Name(2.3)
    
    "create Symptom frames for Depression frames"
    "emotional"
    sadFrame = Symptom()
    sadFrame.Name('Sad')
    sad_syns = ['Low', 'Down', 'Unhappy', 'Downcast', 'Heartbroken','Glum','Gloomy','Doleful','Despairing']
    for x in sad_syns:
        sadFrame.Synonyms(x)
    depressionFrame.EmotionalSymptoms(sadFrame)
    
    "physical"
    tiredFrame = Symptom()
    tiredFrame.Name('Tired')
    tired_syns = ['Exhausted','Weary', 'Fatigued','Drained','Enervated']
    for x in tired_syns:
        tiredFrame.Synonyms(x)
    depressionFrame.PhysicalSymptoms(tiredFrame)
        
    weightFrame = Symptom()
    weightFrame.Name('Weight Change')
    weight_syns = ['Weight gain','Weight loss', 'Fatter', 'Skinnier', 'Thinner']
    for x in weight_syns:
        weightFrame.Synonyms(x)   
    depressionFrame.PhysicalSymptoms(weightFrame)
 
        
    sleepFrame = Symptom()
    sleepFrame.Name('Sleep Changes')
    sleep_syns = ['Early','Awakening', 'Excess sleepiness', 'Insomnia', 'Restless sleep', 'Sleepier']
    for x in sleep_syns:
        sleepFrame.Synonyms(x)
    depressionFrame.PhysicalSymptoms(sleepFrame)

    
    appetiteFrame = Symptom()
    appetiteFrame.Name('Appetite Changes')
    appetite_syns = ['More hungry', 'Less Hungry', 'Hungrier', 'Starving']
    for x in appetite_syns:
        appetiteFrame.Synonyms(x)
    depressionFrame.PhysicalSymptoms(appetiteFrame)

    
    cognitiveFrame = Symptom()
    cognitiveFrame.Name('Cognitive Changes')
    cog_syns = ['lack of concentration', 'slowness in activity', 'thoughts of suicide']
    for x in cog_syns:
        cognitiveFrame.Synonyms(x)    
    depressionFrame.PhysicalSymptoms(cognitiveFrame)
   
    



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

