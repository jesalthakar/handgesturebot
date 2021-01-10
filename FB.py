from firebase import firebase

b= firebase.FirebaseApplication('https://hand-gesture-bot.firebaseio.com/')#database url

ID='1'#tag

detected = '0'#data



while True :

    with open('demo.txt','r') as f:
        for line in f:
            pass
        last_line = line
        print(last_line)
        result = b.put('/data','FINGERS',last_line)
        print(result)
