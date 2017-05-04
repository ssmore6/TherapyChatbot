"""Knowledge representation: Frame Based"""



"""
Generic frame: Mental illness
Individual frame: Depression, Anxiety, Insomnia
"""

import datetime
import utils

#SLIDE: upper case for generic frames
"Generic frame"
class Directory:
    def __init__(self):
        "cosntructor"
    "slot1 = IS_A  , filler = genericframe (<type>?)"
    def IS_A(self, genericframe = "Directory"):#can i do this??? can a frame be an instance of itself
        self.IS_A = genericframe #is IS A even needed here? confused
    "slot2 = Name , filler = name (string)"
    def Name(self, name):
        self.Name = name
    "slot3 = FirstPatient , filler = firstPatient (pointer to Patient frame)"
    def FirstPatient(self, firstPatient):
        self.FirstPatient = firstPatient
    "slot4 = LastPatient , filler = lastPatient (pointer to Patient frame)"
    def LastPatient(self,lastPatient):
        self.LastPatient = lastPatient
    
        
#SLIDE: upper case for generic frames
"Generic frame"
class Patient:
    def __init__(self):
        "constructor"
    "slot1 = IS_A, filler = genericframe (<type>?)"
    def IS_A(self,genericframe):
        self.IS_A = genericframe
    "slot2 = FirstName , filler = fname (string)"
    def FirstName(self,name):
        self.Name = name
    "slot3 = LastName , filler = lname (string)"
    def LastName(self, lname):
        self.LastName = lname
    "slot4 = Age , filler = age (int)"
    def Age(self,age):
        self.Age = age
    "slot5 = Gender, filler = gender (char)"
    def Gender(self,gender):
        self.Gender = gender
    "slot6 = Symptoms , filler = symptoms (string[])"
    def Symptoms(self,symptoms):
        self.Symptoms = symptoms
    "slot7 = AdditionalInfo , filler = addInfo (string)" #to add to patient info concatenate addInfo with additional string
    def AdditionalInfo(self,addInfo):
        self.AdditionalInfo = addInfo
    "slot8 = Diagnosis , filler  = diagnosisList (pointer to MentalIllness[])"
    def Diagnosis(diagnosisList):
        self.Diagnosis = diagnosisList
            
"Generic frame"
class MentalIllness:
    def __init__(self):
        "constructor"
    "Slot1 = IS_A, filler = genericframe (<type>?)" #???? can generic frame be an IS A of itself??
    def IS_A(self, genericframe = "MentalIllness"):#what type should generic frame be??
        self.IS_A = genericframe
    "Slot2 = Name , filler = name (string)" 
    def Name(self,name):
        self.Name = name
    "Slot3  = PhysicalSymptoms, filler = symptoms (string[])"
    def PhysicalSymptoms(self,physymptoms):
        self.PhysicalSymptoms = physymptoms
    "Slot4 = EmotionalSymptoms, filler = emosymptoms (string[])"
    def EmotionalSymptoms(self,emosymptoms):
        self.EmotionalSymptoms = emosymptoms
        
        
            
"Generic frame"          
class Diagnosis:
    def __init__(self):
        "constuctor"       
    "Slot1 = Patient , filler  = patient (pointer to Patient)" #patient that diagnosis belongs to 
    def Patient(self,patient):
        self.Patient = patient
    "Slot2 = SessionTime , filler = sessionTime (<type>?)"
    def SessionTime(self,sessionTime):
        self.SessionTime = sessionTime
    "Slot3 = detectedConditions , filler = detectedCond (array of pointers to MentalIllness frames)"
    def DetectedConditions(self,detectedCond):
        self.DetectedConditions = detectedCond            
    "Slot4 = NextPatient , filler = nextPatient (pointer to a Patient)" #may need to instantiante with if-needed or as-needed etc
    def NextPatient(self,nextPatient):
        self.NextPatient = nextPatient
    "Slot5 = LastPatient , filler = lastPatient (boolean) " 
    def LastPatient(self,lastPatient):
        self.LastPatient = lastPatient
        






"""                         SEARCH - put in a seperate module
**shweta will implement
    
I was thinking of passing in a Directory frame since Directory serves a root node/head 
? Do we have different searches for different purposes?
    ex: a search for a particular patient?
    ex: a search for a particular mental illness?
        def search_patient(...)
        def search_illness(...)

"""
def search(Directory, frameToSearchFor):
    "needs to be implemented"
    "search could be in seperate module which will be imported"
    
    
    

def add_patient(name,age,gender):
    "create a uniqueID for patient and create Patient variable during runtime using vars()"
    "patientID = hash firstname , lastname, and datetime Patient object is being created"


"""
Note: main will be in the chatbot code
    main in this module will be changed to set up method
        additional methods:
                methods that act as getters and setters for frames
                display frame frame representation kb
                new patient
        
        need to work on
            collect data for decision learning tree method 
                = SEARCH
"""
if __name__ == '__main__': 
    """test"""
    "-------------------------MentalIllness frames + Directory frame will be created before patient converses with chatbot------------"
    
    "create Frame(Indivdual): depression"
    depression = MentalIllness()
    depression.Name("Depression")
    depression.PhysicalSymptoms(["tired","exhausted", "weak", "trouble sleeping", "trouble waking up", "undereating", "overeating"])
    depression.EmotionalSymptoms(["hopelessness","down", "sad", "irritable", "withdrawn","isolated", "discouraged", "guilty", "suicidal"])
    
    "create Frame(Individual); anxiety"
    anxiety = MentalIllness()
    anxiety.Name("Anxiety")
    anxiety.PhysicalSymptoms(["shakiness", "sweaty", "heart palpitations","dizziness", "chest pain",
        "headaches", "neck tension", "pulsing in ear", "nausea", "shortness of breath", "weakness in legs",
        "sleep problems","inability to rest" , "restless", "racing throughts", "muscle tension", "dry mouth"])
    anxiety.EmotionalSymptoms(["anxious", "emotionless", "disconnected" ])
    
    "create Frame(Individual): insomnia"
    insomnia = MentalIllness()
    insomnia.Name("Insomnia")
    insomnia.PhysicalSymptoms(["fatigue", "tired", "cant concentrate", "daytime sleepiness"])
    insomnia.EmotionalSymptoms(["unmotivated", "moody", "irritable"])
    
    
    "create a directory"
    directory = Directory()
    dt = datetime.datetime.now()
    directory.Name("chatbot therapy session : "+dt.strftime('%m/%d/%Y'))
   
   
    "-------------------------------Patient Frame will be created after chatbot gets info about current Patietn-----------------"
    
    
    
    
    
    "use extracted words/key words that can be used to fill in slots for the frames listed above"
    """NOTE : instantiate a Patient class and fill in slot for lastPatient in Directory BEFORE user quits
        update when another patient wants to start a session"""

   


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