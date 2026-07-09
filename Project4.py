import random
science=[
    {"q":"Which planet is known as the Red Planet?","o":['A. Earth', 'B. Mars', 'C. Venus', 'D. Jupiter'],"a":"B"},
    {"q":"What gas do plants absorb?","o":['A. Oxygen', 'B. Nitrogen', 'C. Carbon Dioxide', 'D. Hydrogen'],"a":"C"},
    {"q":"How many bones in an adult body?","o":['A.206', 'B.201', 'C.208', 'D.210'],"a":"A"},
    {"q":"H2O is?","o":['A.Salt', 'B.Water', 'C.Oxygen', 'D.Hydrogen'],"a":"B"},
    {"q":"Largest organ?","o":['A.Heart', 'B.Liver', 'C.Skin', 'D.Lungs'],"a":"C"},
    {"q":"Center of solar system?","o":['A.Earth', 'B.Moon', 'C.Sun', 'D.Mars'],"a":"C"},
    {"q":"Force pulling objects?","o":['A.Magnetism', 'B.Gravity', 'C.Friction', 'D.Motion'],"a":"B"},
    {"q":"Human heart chambers?","o":['A.2', 'B.3', 'C.4', 'D.5'],"a":"C"},
    {"q":"Boiling point water C?","o":['A.90', 'B.95', 'C.100', 'D.110'],"a":"C"},
    {"q":"Fastest land animal?","o":['A.Lion', 'B.Cheetah', 'C.Tiger', 'D.Horse'],"a":"B"},
    {"q":"Vitamin from sunlight?","o":['A.A', 'B.B', 'C.C', 'D.D'],"a":"D"},
    {"q":"Gas most in air?","o":['A.Oxygen', 'B.Nitrogen', 'C.CO2', 'D.Helium'],"a":"B"},
    {"q":"Blood color due to?","o":['A.Chlorophyll', 'B.Hemoglobin', 'C.Plasma', 'D.Calcium'],"a":"B"},
    {"q":"Largest mammal?","o":['A.Elephant', 'B.Blue Whale', 'C.Giraffe', 'D.Shark'],"a":"B"},
    {"q":"Nearest star to Earth?","o":['A.Sirius', 'B.Polaris', 'C.Sun', 'D.Venus'],"a":"C"},
]
geography=[
    {"q":"Capital of France?","o":['A.Rome', 'B.Berlin', 'C.Paris', 'D.Madrid'],"a":"C"},
    {"q":"Capital of India?","o":['A.Delhi', 'B.Mumbai', 'C.Kolkata', 'D.Chennai'],"a":"A"},
    {"q":"Largest ocean?","o":['A.Atlantic', 'B.Indian', 'C.Pacific', 'D.Arctic'],"a":"C"},
    {"q":"Land of Rising Sun?","o":['A.China', 'B.Japan', 'C.Korea', 'D.Thailand'],"a":"B"},
    {"q":"Highest mountain?","o":['A.K2', 'B.Kilimanjaro', 'C.Everest', 'D.Elbrus'],"a":"C"},
    {"q":"Longest river?","o":['A.Nile', 'B.Amazon', 'C.Yangtze', 'D.Ganga'],"a":"A"},
    {"q":"Capital of Australia?","o":['A.Sydney', 'B.Melbourne', 'C.Canberra', 'D.Perth'],"a":"C"},
    {"q":"Sahara is a?","o":['A.Forest', 'B.Desert', 'C.River', 'D.Lake'],"a":"B"},
    {"q":"Smallest continent?","o":['A.Europe', 'B.Australia', 'C.Antarctica', 'D.S America'],"a":"B"},
    {"q":"Country with most population?","o":['A.India', 'B.USA', 'C.Brazil', 'D.Russia'],"a":"A"},
    {"q":"Great Pyramid country?","o":['A.Peru', 'B.Egypt', 'C.India', 'D.Greece'],"a":"B"},
    {"q":"Currency of Japan?","o":['A.Yuan', 'B.Won', 'C.Yen', 'D.Baht'],"a":"C"},
    {"q":"Capital of Canada?","o":['A.Toronto', 'B.Ottawa', 'C.Vancouver', 'D.Montreal'],"a":"B"},
    {"q":"Which ocean borders India south?","o":['A.Arctic', 'B.Pacific', 'C.Indian', 'D.Atlantic'],"a":"C"},
    {"q":"Largest continent?","o":['A.Africa', 'B.Asia', 'C.Europe', 'D.N America'],"a":"B"},
]
computer=[
    {"q":"CPU stands for?","o":['A.Central Processing Unit', 'B.Control Program Unit', 'C.Central Power Unit', 'D.None'],"a":"A"},
    {"q":"RAM stands for?","o":['A.Random Access Memory', 'B.Read Access Memory', 'C.Rapid Access Module', 'D.None'],"a":"A"},
    {"q":"Python is a?","o":['A.OS', 'B.Language', 'C.Browser', 'D.Game'],"a":"B"},
    {"q":"Brain of computer?","o":['A.Mouse', 'B.CPU', 'C.Keyboard', 'D.Monitor'],"a":"B"},
    {"q":"WWW means?","o":['A.World Wide Web', 'B.World Web Window', 'C.Web World Wide', 'D.None'],"a":"A"},
    {"q":"Input device?","o":['A.Printer', 'B.Monitor', 'C.Keyboard', 'D.Speaker'],"a":"C"},
    {"q":"Output device?","o":['A.Mouse', 'B.Scanner', 'C.Microphone', 'D.Monitor'],"a":"D"},
    {"q":"HTML used for?","o":['A.Web pages', 'B.Games', 'C.OS', 'D.Database'],"a":"A"},
    {"q":"Binary digits are?","o":['A.0 and1', 'B.1 and2', 'C.2 and3', 'D.3 and4'],"a":"A"},
    {"q":"Shortcut copy?","o":['A.Ctrl+V', 'B.Ctrl+C', 'C.Ctrl+X', 'D.Ctrl+Z'],"a":"B"},
    {"q":"Shortcut paste?","o":['A.Ctrl+V', 'B.Ctrl+C', 'C.Ctrl+P', 'D.Ctrl+A'],"a":"A"},
    {"q":"Which stores files permanently?","o":['A.RAM', 'B.Cache', 'C.Hard Disk', 'D.Register'],"a":"C"},
    {"q":"Extension of Python file?","o":['A..java', 'B..py', 'C..txt', 'D..cpp'],"a":"B"},
    {"q":"Google Chrome is?","o":['A.Browser', 'B.OS', 'C.Editor', 'D.Antivirus'],"a":"A"},
    {"q":"AI stands for?","o":['A.Automatic Input', 'B.Artificial Intelligence', 'C.Advanced Internet', 'D.None'],"a":"B"},
]

categories={"1":("Science",science),"2":("Geography",geography),"3":("Computer",computer)}
while True:
    print("\n1. Science\n2. Geography\n3. Computer")
    ch=input("Choose a category: ")
    if ch not in categories:
        print("Invalid choice."); continue
    name,data=categories[ch]
    score=0
    print("\nYou selected",name)
    for i,q in enumerate(random.sample(data,3),1):
        print(f"\nQuestion {i}: {q['q']}")
        for o in q["o"]: print(o)
        ans=input("Enter A/B/C/D: ").upper()
        if ans==q["a"]:
            print("Correct!"); score+=1
        else:
            print("Wrong! Correct answer:",q["a"])
    print(f"\nFinal Score: {score}/3")
    ag=input("Play again? (Y/N): ").upper()
    if ag!="Y": break
