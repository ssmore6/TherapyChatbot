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
            self.Name = str(name)
    "slot2 = Age , filler = age (int)"
    def Age(self,age):
            self.Age = int(age)     
    "slot3 = Gender, filler = gender (string): F,M"
    def Gender(self,gender):
        def IF_ADDED(gender):
            if gender.lower() == 'male':
                return 'M'
            elif gender.lower() == 'female':
                return 'F'
            self.Gender = str(IF_ADDED(gender))

        


        
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
        self.Name = str(name)
    "slot2 = Synonyms, filler = synonym (string)"
    def Synonyms(self,synonym):
        self.synonyms.append(str(synonym))
        

            
"Generic frame"
class Condition:
    def __init__(self):
        "constructor"
    "Slot1 = Name , filler = name (string)" 
    def Name(self,name):
        self.Name = str(name)

            
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
        
        
"""
    
    tpatient (TherapyPatient)
    attr_list (string[])
    note: list that is constructed will be list of yes's and no's
    
    IN PROGRESS!

"""        
def create_attribute_list(patient, attr_list):
    list_for_tree=[]
    
    "if list of symptoms in Patient class is empty"
    if len(patient.symptoms) == 0 or len(patient.symptoms) < len(attr_list):
        return None
    "if list of symptoms in Patient class is at least same length as attr_list"
    if len(patient.symptoms) == len(attr_list):
        "for each attribute that decision tree needs"
        for attr in attr_list:
            "for now enter 'no' for this attr in list_for_tree since attribute we are looking for may not be present"
            list_for_tree[attr_list.index(attr)] = 'no'
            "for each Symptom object look through synonyms"
            for symp in patient.symptoms:
                "go through each synonym in symp(Symptom)"
                for syn in symp.synonyms:
                    "attribute is found among synonyms change to yes"
                    if syn == attr:
                        list_for_tree[attr_list.index(attr)] = 'no'
        return list_for_tree

if __name__ == '__main__': 
    supposed_attribute_list_for_tree = ['Sad','Tired', 'Lonely', 'Sleep Changes']        
    p = Patient()
    create_attribute_list(p, supposed_attribute_list_for_tree)
    """test"""
    
    """
    
    sample tree
    
            
    
    
    supposed_attribute_list_for_tree = ['Sad','Tired', 'Lonely', 'Sleep Changes']
    
    user_keywords = [...,...,..,...] //user_keywords can be at any length
    
    def search_for_attribute_inFrames(attribute:string):



    def prepare_attribute_list(user_keywords):
        
        for x in supposed_attribute_list_for_tree:
            for y in user_keywords:
                
        
        return at_list_for_tree
        
        
        
    DECISION_TREE.py
    
    method_that _determines_depressionOrNot(at_list_for_tree)
    
    """
   
    "create Depression frame"
    depressionFrame = MentalIllness()
    depressionFrame.Name("De[ression")
    
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
   
    



