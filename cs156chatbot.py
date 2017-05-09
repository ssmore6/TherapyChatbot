"""
NOTES:
    preferably we could be using TextBlob and NLTK which will reduce the amount
    of effort we have to spend on defining/tokening verbs, nouns etc
    
    but it requires us to install TextBlob and NLTK as modules and i don't remember
    if professor said anything regarding installing/using third-party modules? could
    someone ask him about that?
    
SAMPLE GRAMMAR:
    User: I feel <emotion>
    (if positive) AI: I'm glad to hear you're feeling <emotion>
    (if negative) AI: I'm sorry to hear you're feeling <emotion>
    (if unknown) AI: Do you like feeling <emotion>?
    User: Yes/No (AI will add emotion and its positive/negativity to knowledge base
    
    provide for cases where user says 'I don't/do not feel <emotion>'
    
TO DO:
*   remember previous user inputs to put current input into context ?

*    implement frame-based representation (?)
    <illness>
        <typeof: mental>
            <mental_name: depression>
                <symptoms: insomnia, fatigue>
            <mental_name: anxiety>
                <symptoms: panic attacks>
                <...>
               
    maybe use classes and subclasses, keep symptoms in an array of strings? how to identify synonyms? (tired = fatigue, etc)
    
*   neuro-something learning -- to store information about the user session

*   what kind of search is it using? -- to use stored information to match to a disease
"""

import random

STARTUP_PROMPT = "COMMANDS:\n[h]elp [q]uit [s]ymptomlist\nHello, I am a chatbot."
DIAGNOSIS_PROMPT = "It appears you may be showing signs of {diagnosis}. Does that sound correct?"
NEXTPATIENT_PROMPT = "Next session; say \'hello\' to start:"
HELP_STRING = "If the chatbot has trouble understanding you, try using simpler sentences like \'I feel ____.\'\nUse \'s\' to show what symptoms the chatbot has gathered from your input."

COMMON_TOPICS = ["death", "family", "mother", "brother", "brothers", "sister", "sisters", "pet", "dog", "school", "college", "class", "classes", "grades", "boyfriend", "girlfriend", "dead", "died"]

QUESTION_KEYWORDS = ["who","what","when","where","why"]
NEGATION_KEYWORDS = ["not", "n\'t"]
COMMON_VERBS = ["am","feel","feeling","want","wanting","have","having","go","going"]
POSITIVE_KEYWORDS = ["happy", "okay"]
NEGATIVE_KEYWORDS = ["sad", "stressed", "low", "upset", "tired"] 
SUICIDE_KEYWORDS = ["suicide", "suicidal", "kill myself"]
THANKS_KEYWORDS = ["thanks", "thank you"]
YES_KEYWORDS = ["yes","yeah", "yep","I think so"]
NO_KEYWORDS = ["no", "nope", "I don\'t think so"]

#question flag = name
NAME_RESPONSE = "It is nice to meet you, {name}."

#question flag = age
AGE_CHILD_RESPONSE = "Often, depression in youths go unnoticed. Even though you are young, it\'s important to take your mental health seriously."
AGE_ADULT_RESPONSE = "Often, the stresses of adult life can bring on symptoms of depression. It\'s important not to neglect your mental health."

#question flag = physical/emotional
NEGATIVE_FEELING_RESPONSES = "I\'m sorry that {emotion}."
FEELING_CONFIRMATION = "So your general emotion is {emotion}?"

DEFAULT_RESPONSES = ["I\'m sorry, could you rephrase that?", "I don\'t understand what you said."]
CONFUSED_RESPONSE = "I\'m not sure what you said. Is there another word to describe it?"
SUICIDE_RESPONSE = "Don\'t be afraid to reach out for help.\nThe National Suicide Prevention Hotline is available at 1-800-273-8255, if you would like to speak to someone."
THANKS_RESPONSE = ["No problem.","I will do anything I can to help.","I hope this helps you in some way."] #keywords need to be written/implemented
APOLOGY_RESPONSE = "Oh, my apologies. I will keep this in my files and we can revisit this in a new session."
TWOWEEKS_RESPONSE = "For your symptoms to have persisted as long as they have may indicate a persistent condition."
TWOWEEKSNO_RESPONSE = "Everyone goes through slumps, but sometimes its a sign of a more persistent condition."

NAME_QUESTION = "What is your name?"
AGE_QUESTION = "How old are you?"
FEELING_QUESTION = "How are you feeling?"
TIME_QUESTION = "Have the symptoms you are about to describe been present for longer than several weeks?"
WHY_QUESTION = "Can you think of anything in your life that may be a factor in feeling {emotion}?"
HOW_QUESTION = "How do you feel about {thing}?"
FOLLOWUP_QUESTION = "How are you feeling now?"

DIAGNOSIS = "Name: {name}\nAge: {age}\nDuration: {time}\nGeneral Emotion: {emotion}\nGeneral Feeling: {energy}"

QUESTIONS = [NAME_QUESTION, AGE_QUESTION, TIME_QUESTION, FEELING_QUESTION]
question_flag = None
question_list = ["name", "age", "time", "feeling", "energy"]
patient_info = [None, None, None, None, None] # name, age, duration > 2 weeks, general emotion, energy level, final diagnosis.

#----------------------------------------------------------

def split_at(words, verb):
    """
    splits sentence in half at the given verb
    """
    if verb in words:
        i = words.index(verb)
        first_half = words[0:i]
        second_half = words[i+1:]
        return [first_half, second_half]
    else:
        return -1

def punctuation_remover(words):
    words = words.replace('?','')
    words = words.replace('!','')
    words = words.replace('.','')
    return words 

def pronoun_switch(words):
    for x in words:
        if x == "you":
            x = "I"
        elif x == "I":
            x = "you"
        elif x == "am":
            x = "are"
        elif x == "my":
            x = "your"
        elif x == "we":
            x = "you"
        elif x == "our":
            x = "your"
        elif x == "us":
            x = "you"
    return words 

def diagnosis_reply():
    """
    gives list of patient info
    """
    return DIAGNOSIS.format(**{'name':patient_info[0], 'age': patient_info[1], 'time':patient_info[2], 'emotion': patient_info[3], 'energy': patient_info[4]})

def default_reply():
    """
    If no keywords can be found, chatbot will express confusion.
    """
    return random.choice(DEFAULT_RESPONSES)
    
def suicide_reply():
    """
    If SUICIDE_KEYWORDS is detected, offer SUICIDE_RESPONSE
    """
    return random.choice(SUICIDE_RESPONSE)

def find_verbs(words):
    pass

def find_negation(words):
    pass

def is_firstperson(words):
    if words[0].lower() == "I".lower() or words[0].lower() == "I\'m".lower(): #first person
        return True
    else:
        return False

def name_reply(sentence):
    wordsarray = sentence.split()
    if "my name is" in sentence:
        sent_chunks = split_at(wordsarray,"is")
        patient_info[0] = sent_chunks[1]
    elif "i'm" in sentence:
        sent_chunks = split_at(wordsarray, "i'm")
        patient_info[0] = sent_chunks[1]
    elif "i am" in sentence:
        sent_chunks = split_at(wordsarray, "am")
        patient_info[0] = sent_chunks[1]
    else:
        patient_info[0] = sentence
    return NAME_RESPONSE.format(**{'name':patient_info[0]})
    
def age_reply(sentence):
    patient_info[1] = int(sentence)
    if patient_info[1] < 18:
        return AGE_CHILD_RESPONSE
    else:
        return AGE_ADULT_RESPONSE
    
def feeling_reply(sentence):
    pass
    
def why_reply(sentence):
    sent = pronoun_switch(sentence)
    patient_info[3] = sent
    return WHY_QUESTION.format(**{'emotion':sent})
    
def time_reply(sentence):
    time = None
    reply = default_reply()
    for k in YES_KEYWORDS:
        if k in sentence:
            reply = TWOWEEKS_RESPONSE
            time = "yes"
    for k in NO_KEYWORDS:
        if k in sentence:
            reply = TWOWEEKSNO_RESPONSE
            if time != "yes" or time != "maybe":
                time = "no"
            else:
                time = "maybe"
    patient_info[2] = time
    return reply
    
def question_reply(sentence):
    """replies to user input"""
    global question_flag # records question asked by bot
    if len(sentence) < 1:
        return default_reply() # default reply if input cannot be comprehended
    sentence = punctuation_remover(sentence)
    sentence = sentence.lower()
    if question_flag == question_list[0]: 
        return name_reply(sentence) # hello, <name>
    elif question_flag == question_list[1]:
        return age_reply(sentence) # reply depending on how old the user is
    elif question_flag == question_list[2]:
        return time_reply(sentence) # how long has the user's symptoms persisted?
    elif question_flag == question_list[3]:
        return why_reply(sentence) # does the user know why they may feel this way? 
                                    # bot may offer simple advice based on detected keywords
        
def find_reply(sentence):
    """
    """
    if question_flag != None:
        return question_reply(sentence)
    else:
        if sentence[0].lower() == "I".lower() or sentence[0].lower() == "I'm".lower(): #might be obselete
            return find_negation(sentence[1:]);
        else:
            return default_reply()

def reply(sentence):
    """ 
    """
    if sentence.lower() == 'q':
        return 'Goodbye.'
    elif sentence.lower() == 'h':
        return HELP_STRING
    elif sentence.lower() == 's':
        return diagnosis_reply()
    else:
        return find_reply(sentence)
        
def ask_question():
    sentence = ''
    global question_flag 
    for x in range(len(patient_info)-1):
        question_flag = question_list[x]
        while patient_info[x] is None and sentence != 'q':
            print QUESTIONS[x]
            sentence = raw_input('Say: ')
#            print "%s" % sentence
            print reply(sentence)

if __name__ == '__main__':
    sentence = ''
    print STARTUP_PROMPT
    while sentence != 'q' and None in patient_info[0:4]:
        ask_question()
    if sentence == 'q':
        print 'Shutting off...'         
        
        
#-------------------

