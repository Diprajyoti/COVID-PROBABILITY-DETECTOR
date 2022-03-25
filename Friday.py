''''Code Made by Diprajyoti Majumdar (IT)
#Jis College of Engineering'''



import pyttsx3
import datetime
import speech_recognition as sr


import pickle


engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        speak("Good morning sir!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon sir!")
    else:
        speak("Good evening sir!")
    print("this is friday 2.0 on duty. I am a covid-19 probability detector . If you think You have covid-19, then say that I have covid-19."
          " I will catch and analyze your data and you will get your probability for being affected. Now ask me")
    speak("this is friday 2.0 on duty. I am a covid-19 probability detector . If you think You have covid-19, then say that I have covid-19."
          " I will catch and analyze your data and you will get your probability for being affected. Now ask me")

def takecommand() :
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listenning...")
        r.pause_threshold=1
        r.phrase_threshold=0.2

        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said :{query}\n")

    except Exception as e:
        print("say that again please...")
        return "None"
    return query

if __name__=="__main__":
    bodyorjointpain=0
    sorethroat=0
    fever=0
    Drycough=0
    chestpain=0
    Headache=0
    Vomitting=0
    diffbreath=0
    tastesmellloss=0
    anxity=0
    infprob=0
    wish()

    Query=takecommand()
    if 'covid-19' in Query:
          speak("oh really? Do u want to have a test? a quick short test for your health ?  yes or no")
          print("oh really? Do u want to have a test? a quick short test for your health ?yes or no")
          select=takecommand()
          if 'yes'in select:
            speak("ok Here we go")
            speak("please type here your age ")
            print("Type here your age")
            Age= int(input())
            print(Age)



            speak("ok Do u have any body or joint pain? yes or no")
            print("ok Do u have any body or joint pain? yes or no")
            pain=takecommand()
            if 'yes'in pain:
                speak("How much ? normal or high ")
                print("How much ? normal or high ")
                bpain=takecommand()
                speak("ok got it")
                if 'normal'in bpain:
                    bodyorjointpain = 0
                else:
                    bodyorjointpain = 1
            else:
                speak("ok got it")
                bodyorjointpain =-1
            print("we got ur bodypain")
            print(bodyorjointpain)



            speak("ok Do u have any chest pain? yes or no")
            print("ok Do you have any chest pain? yes or no")
            chest=takecommand()
            if 'yes' in chest:
                speak("How much ? normal or high")
                print("how much? normal or high")
                cpain=takecommand()
                speak("ok got it")
                if 'normal'in cpain:
                    chestpain=0
                else:
                    chestpain=1
            else:
                speak("ok got it")
                chestpain=-1
            print("we got your chestpain")
            print(chestpain)



            speak("ok Do u have any sorethroat? yes or no")
            print("ok Do you have any sorethroat? yes or no")
            throat = takecommand()
            if 'yes' in throat:
                speak("How much ? little or so much")
                print("how much? little or so much")
                sore = takecommand()
                speak("ok got it")
                if 'little' in sore:
                    sorethroat = 0
                else:
                    sorethroat = 1
            else:
                speak("ok got it")
                sorethroat=-1
            print("we got your sorethroat")
            print(sorethroat)

            speak("ok Do u have a fever ? yes or no")
            print("ok Do you have a fever ? yes or no")
            fev = takecommand()
            if 'yes'in fev:
                speak("How much ? little means in between 100  or so much means more than 100")
                print("how much ? little(99-100) or so much(100+)")
                jor = takecommand()
                speak("ok got it")
                if 'little' in jor:
                    fever =0
                else:
                    fever = 1
            else:
                speak("ok got it")
                fever= -1
            print("we got your runnynose")
            print(fever)


            speak("ok Do u have drycough? yes or no")
            print("ok Do you have drycough? yes or no")
            dry=takecommand()
            if 'yes' in dry:
                speak("ok How much is it? normal or high")
                print("ok how much is it? normal or high")
                cough=takecommand()
                speak("ok got it")
                if 'normal'in cough:
                    Drycough=0
                else:
                    Drycough=1
            else:
                speak("ok got it")
                Drycough=-1
            print("we got your Drycough")
            print(Drycough)

            speak("ok Do u feel headache? yes or no")
            print("ok Do you feel headache? yes or no")
            head= takecommand()
            if 'yes'in head:
                speak("How much ? normal or high")
                print("how much? normal or high")
                ache = takecommand()
                speak("ok got it")
                if 'normal' in ache:
                    Headache = 0
                else:
                    Headache = 1
            else:
                speak("ok got it")
                Headache = -1
            print("we got your Headache")
            print(Headache)

            speak("ok Do u have any vommiting tendency? yes or no")
            print("ok Do you have any vomitting tendency? yes or no")
            nousea = takecommand()
            if  'yes'in nousea:
                speak("How much ? normal or high")
                print("how much? normal or high")
                vomit = takecommand()
                speak("ok got it")
                if 'normal' in vomit:
                    Vomitting = 0
                else:
                    Vomitting = 1
            else:
                speak("ok got it")
                Vomitting = -1
            print("we got your Vomitting")
            print(Vomitting)

            speak("ok Do u feel difficulty in breathing ? yes or no")
            print("ok Do you feel difficulty in breathing? yes or no")
            diff = takecommand()
            if 'yes' in diff:
                speak("How much ? normal or critical")
                print("how much? normal or critical")
                breath = takecommand()
                speak("ok got it")
                if 'normal' in breath:
                    diffbreath= 0
                else:
                    diffbreath = 1
            else:
                speak("ok got it")
                diffbreath = -1
            print("we got your diffbreath")
            print(diffbreath)

            speak("ok can you feel taste or smell ? yes or no")
            print("ok can you feel taste or smell? yes or no")
            taste = takecommand()
            if 'no' in taste:
                speak("ok when do you feel it ? sometimes or always")
                print("ok when do you feel it? sometimes or always")
                smell = takecommand()
                speak("ok got it")
                if 'sometimes' in smell:
                    tastesmellloss = 0
                else:
                    tastesmellloss = 1
            else:
                speak("ok got it")
                tastesmellloss = -1
            print("we got your tastesmellloss")
            print(tastesmellloss)

            speak("ok Do u have any anxity issues for past week? yes or no")
            print("ok Do you have any anxity issues for past week? yes or no")
            issue = takecommand()
            if  'yes'in issue:
                speak("How much is it? normal or intense")
                print("how much is it? normal or intense")
                anxity = takecommand()
                speak("ok got it")
                if 'normal' in anxity:
                    anxity = 0
                else:
                    anxity = 1
            else:
                speak("ok got it")
                anxity= -1
            print("we got your Anxity")
            print(anxity)

            speak("ok wait now, take rest, Let me analize your datas and give me a chance to help u")

            print("ok wait now, take rest, Let me analize your datas and give me a chance to help u")

            file = open('connect.pkl', 'rb')
            clf = pickle.load(file)
            file.close()
            inputfeatures = [bodyorjointpain, sorethroat, fever, Drycough, chestpain, Headache, Vomitting,
                             diffbreath, tastesmellloss, anxity]

            infprob = clf.predict_proba([inputfeatures])[0][1]
            Result=infprob * 100
            print(f'your probability for beeing affected by Corona Virus is={Result}%')
            speakresult=str(Result)
            speak("your probability for beeing affected by Corona Virus is"+speakresult+'%')

          elif "no"  in select:
            print("ok thank you . do u want to know about some precautions ?")
            speak("ok thank you . do u want to know about some precautions ?")
            say=takecommand()
            if 'yes' in say:
                print('ok here we go')
                speak('ok here we go')
                print("To prevent the spread of Covid-19 always clean your hands often .")
                print( " Use soap  and  water or an alcohol based hand rub")
                print( " Maintain a safe distance  from anyone who is coughing or sneezing .")
                print( " Wear a mask specially ")
                print( "N-95 masks or surgical masks when physical distancing is not possible.")
                print( " Dont touch your eyes and mouth.")
                print( "Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze.")
                print( "stay home if you feel unwell")
                print(  "if you have a high fever, cough and difficulty breathing , "
                      "always seek medical attention and consult with your physician")

                speak("To prevent , the spread of Covid-19 , always clean your hands often . Use soap  and  water , or an alcohol based"
                      "hand rub . Maintain a safe distance  from anyone  who is coughing or sneezing . Wear a mask  specially "
                      "N-95 masks or surgical masks when physical distancing is not possible. Dont touch your eyes and mouth."
                      "Cover your nose and mouth with your bent elbow or a tissue when you cough or sneeze. stay home if you feel unwell"
                      "if you have a high fever, cough and difficulty breathing , always seek medical attention and consult with your physician")
            else:
                print("Ok thank you , I am always here for you")
                speak("Ok thank you , I am always here for you")





