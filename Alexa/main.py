import  speech_recognition as sr
import pyttsx3
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate',120)

def talk(text):
    engine.say((text))
    engine.runAndWait()


















import json
import wikipedia
import pywhatkit
from  difflib import  get_close_matches

def load_knowledge_base(file_path: str) -> dict:
    with open(file_path,'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str,data: dict):
    with open(file_path,'w') as file:
        json.dump(data,file,indent=2)


def find_best_match(user_question: str,questions: list[str]) -> str | None:
    matches: list  = get_close_matches(user_question,questions , n=1 , cutoff=0.9)
    return matches[0] if matches else None




def get_answer_for_question(question: str,knowledge_base: dict) -> str | None :
    for q in knowledge_base["questions"]:
       if q["question"] == question:
          return q["answer"]


user_input = ""
def chat():
    str = input('talk or text? : ')

    knowledge_base: dict = load_knowledge_base('knowledge_base.json')


    while True:


        if str=="text":
            user_input = input('You:')
            user_input= user_input.replace(' ','')
        else:
            with sr.Microphone() as source:
                print("listening")
                voice = listener.listen(source)
                user_input = listener.recognize_google(voice)
                user_input = user_input.lower()
                user_input = user_input.replace(' ', '')




        print(user_input)
        if user_input.lower()=='quit':
            break;


        best_match:str | None = find_best_match(user_input,[q["question"]for q in knowledge_base["questions"]])



        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot:{answer}')
            talk(answer)
        elif 'poy' in user_input:
            song = user_input.replace('poy', '')
            pywhatkit.playonyt(song)
        elif 'sog' in user_input:
            name = user_input.replace('sog', '')
            pywhatkit.search(name)
        #  print("name")

        elif 'sow' in user_input:
            name= user_input.replace('sow','')



            best_match: str | None = find_best_match(name,
                                                     [q["question"] for q in knowledge_base["questions"]])
            if best_match:
                answer: str = get_answer_for_question(best_match, knowledge_base)
                print(f'Bot:{answer}')
                talk(answer)
            else:
                new_answer = wikipedia.summary(name, sentences=3)
                print(new_answer)
                talk(new_answer)
                knowledge_base["questions"].append({"question":name,"answer" : new_answer})
                save_knowledge_base('knowledge_base.json',knowledge_base)



        else:
            print(('Bot: I don\'t know the answer . Can you teach me ? '))
            new_answer: str = input('Type the answer or "sp"  to skip :')


            if new_answer.lower() != 'sp':
                knowledge_base["questions"].append({"question":user_input,"answer" : new_answer})
                save_knowledge_base('knowledge_base.json',knowledge_base)
                print('Bot : Thank You ! I learned a new response!')





if __name__ == '__main__':
    chat()
