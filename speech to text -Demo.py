import speech_recognition as sr

# Initialize the recognizer
r = sr.Recognizer()

# Loop infinitely for user to speak
while True:
    # Exception handling to handle exceptions at the runtime
    try:
        # use the microphone as source for input.
        with sr.Microphone(device_index=0) as source:
            # wait for a second to let the recognizer adjust the energy threshold based on the surrounding noise level
            r.adjust_for_ambient_noise(source, duration=0.2)

            # listens for the user's input
            audio = r.listen(source)

            # Using google to recognize audio
            MyText = r.recognize_google(audio,language='vi-VN')
            MyText = MyText.lower()

            print("Did you say : ", MyText)


    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

    except sr.UnknownValueError:
        print("unknown error occurred")
print()