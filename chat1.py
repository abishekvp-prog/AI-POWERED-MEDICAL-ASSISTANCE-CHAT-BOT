
import openai
import speech_recognition as sr
import pyttsx3

openai.api_key = "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 "

# Initialize speech recognizer
r= sr.Recognizer()
def record_text():
# Loop in case of errors
    while(1):
        try:

            with sr.Microphone() as source:

                r.adjust_for_ambient_noise(source, duration = 4)

                SpeakText("i'm listening")
                print("i'm listening")


                audio2 = r.listen(source,timeout=5)

                MyText = r.recognize_google(audio2)

                if "thank you doctor" in MyText.lower():
                    MyText1 ="say thank you and end the conversation"
                    return MyText1  # Returning None to indicate termination
                    
                else:
                    return MyText
                
        except sr.WaitTimeoutError:
            # Timeout occurred, indicating no speech input within 5 seconds
            SpeakText("Timeout: No speech detected. Please speak again by pressing the button.")
            return None

            
        except sr.RequestError as e:
            print("could not request results;{0}".format(e))

        except sr.UnknownValueError :
            print("unknown error occurred")
            
        

def main():
    while True:
        
        message=record_text()
        if message == "say thank you and end the conversation":
            SpeakText("thank you for assisting me !!dont visit me again lol")
            break
        elif message == None:
            break
        
        else:

#message.append({"role":"user","content":"please act like a jarvis from iron man"})
           #message1 = "i dont need the introductory statements that you say and you act like a doctor"
            model_engine = "gpt-3.5-turbo-instruct"
#prompt1 = "about abdul kalam sir"
            #prompt= message1 + message
            prompt = "hey chat your a med bot that works exact like a doctor and you can answer like a doctor , you dont need to introduce about yourself , just answer the questions by the user and you can also prescribe medicines if required dont introduce about you untill requested by the user "+ message 
           # prompt5 = prompt + "suggest some medicines for it"
            completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    temperature=0.5,
    max_tokens=100,
    n=1,
    stop=None,
    
)

            response = completion.choices[0].text
            SpeakText(response)



def SpeakText(command):
# Initialize the engine
    engine = pyttsx3.init()

    voices = engine.getProperty('voices')
    for voice in voices:
        if "female" in voice.name.lower():
            engine.setProperty('voice', voice.id)
            break


    engine.setProperty('rate',150)
    engine.say (command)
    engine.runAndWait()

if __name__ == "__main__":
    SpeakText("hii , im doctor med an ai powered medical assistant developed by med botz . im here to answer about all your medical queries and prescribe you the required medicinal information")
    main()