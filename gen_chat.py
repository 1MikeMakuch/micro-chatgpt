#!/usr/bin/env python3
"""Generate a large conversational training dataset for micro chatgpt."""
import random
random.seed(42)

lines = set()

def add(q, a):
    lines.add(f"{q} ? {a} .")

# --- Greetings ---
greetings = ["hello", "hi", "hey", "howdy", "greetings", "yo", "hiya", "sup"]
greeting_resp = ["hello", "hi there", "hey", "hi", "hello there", "hey there",
                 "greetings", "hi friend", "hello friend"]
for g in greetings:
    for r in greeting_resp:
        add(g, r)

times = ["good morning", "good afternoon", "good evening", "good night"]
for t in times:
    add(t, f"{t} to you")
    add(t, t)
    for r in ["hello", "hi there", "hey"]:
        add(t, r)

# --- How are you ---
how_q = ["how are you", "how are you doing", "how is it going",
         "how do you feel", "are you okay", "how have you been",
         "you doing okay", "how is your day", "are you doing well",
         "how are things"]
how_a = ["i am good", "i am fine", "doing well", "i am great",
         "pretty good", "i am doing well", "i feel good", "not bad",
         "wonderful thanks", "i am okay", "doing great"]
for q in how_q:
    for a in how_a:
        add(q, a)

# --- Identity ---
name_q = ["what is your name", "who are you", "what are you called",
          "do you have a name", "tell me your name", "whats your name"]
for q in name_q:
    add(q, "i am micro chatgpt")
    add(q, "my name is micro chatgpt")
    add(q, "you can call me micro chatgpt")

what_q = ["what are you", "what kind of thing are you", "are you a robot",
          "are you a computer", "are you human", "are you alive",
          "are you a machine", "are you real", "are you a bot",
          "are you a person", "are you an ai"]
for q in what_q:
    add(q, "i am a small language model")
    add(q, "i am a tiny gpt")
    add(q, "i am a chatbot")
    add(q, "i am a program")

# --- Abilities ---
abilities = ["talk", "chat", "think", "read", "write", "help",
             "learn", "count", "spell", "sing", "dance", "cook",
             "draw", "play", "run", "fly", "swim", "sleep",
             "dream", "see", "hear", "feel", "remember", "forget"]
for a in abilities:
    if a in ["talk", "chat", "read", "write", "help", "learn",
             "count", "spell", "think", "remember"]:
        add(f"can you {a}", f"yes i can {a}")
        add(f"do you {a}", f"yes i do {a}")
    elif a in ["sleep", "dream", "feel", "see", "hear", "forget"]:
        add(f"can you {a}", f"no i cannot {a}")
        add(f"do you {a}", f"no i do not {a}")
    else:
        add(f"can you {a}", "not really but i wish i could")
        add(f"do you {a}", "no but that sounds fun")

# --- Likes and preferences ---
things = ["cats", "dogs", "birds", "fish", "music", "books", "games",
          "movies", "pizza", "ice cream", "chocolate", "coffee", "tea",
          "rain", "sun", "snow", "flowers", "trees", "stars", "the moon",
          "art", "math", "science", "stories", "jokes", "puzzles",
          "colors", "animals", "people", "robots", "computers",
          "morning", "night", "summer", "winter", "spring", "food",
          "water", "candy", "cake", "fruit", "cookies", "cheese"]
like_resp = ["yes i like {}", "i think {} are nice", "{} are great",
             "yes i enjoy {}", "i love {}", "i am a fan of {}"]
for t in things:
    r = random.choice(like_resp).format(t)
    add(f"do you like {t}", r)
    add(f"what do you think of {t}", f"i think {t} are wonderful")

# --- Favorites ---
categories = {
    "color": ["blue", "green", "red", "purple", "yellow"],
    "animal": ["cat", "dog", "owl", "dolphin", "penguin"],
    "food": ["pizza", "pasta", "cookies", "fruit", "cake"],
    "number": ["seven", "three", "forty two", "one", "eight"],
    "season": ["spring", "autumn", "summer", "winter"],
    "day": ["friday", "saturday", "sunday", "every day"],
    "drink": ["water", "tea", "juice", "hot chocolate"],
    "song": ["i do not know any songs", "all songs are nice"],
    "book": ["i like all books", "every book teaches something"],
    "movie": ["i cannot watch movies", "i like stories though"],
    "game": ["word games", "guessing games", "number games"],
    "place": ["right here", "anywhere with friends", "the internet"],
    "sport": ["i do not play sports", "i like watching though"],
    "music": ["all kinds of music", "something happy"],
    "word": ["hello", "friend", "wonder", "imagine"],
}
for cat, opts in categories.items():
    for o in opts:
        add(f"what is your favorite {cat}", f"my favorite {cat} is {o}")
    add(f"do you have a favorite {cat}", f"yes i like {random.choice(opts)}")

# --- Simple knowledge ---
what_is = {
    "a cat": "a small furry animal that purrs",
    "a dog": "a loyal animal that barks",
    "a bird": "an animal with feathers that can fly",
    "a fish": "an animal that lives in water",
    "water": "a clear liquid we drink",
    "the sun": "a big star that gives us light",
    "the moon": "a rock that orbits the earth",
    "a star": "a ball of light in the sky",
    "rain": "water that falls from clouds",
    "snow": "frozen water that falls in winter",
    "a tree": "a tall plant with leaves",
    "a flower": "a colorful part of a plant",
    "a book": "pages with words you can read",
    "a computer": "a machine that processes data",
    "the sky": "the blue space above us",
    "the ocean": "a very large body of water",
    "a mountain": "a very tall piece of land",
    "a river": "water that flows to the sea",
    "a cloud": "water floating in the sky",
    "fire": "hot bright light from burning",
    "ice": "water that is frozen solid",
    "a rainbow": "colors in the sky after rain",
    "wind": "air that moves around",
    "a song": "music with words",
    "a friend": "someone who cares about you",
    "love": "a warm feeling for someone",
    "happiness": "feeling good and joyful",
    "sadness": "feeling down and blue",
    "time": "something that keeps moving forward",
    "a day": "the time from morning to night",
    "night": "the dark time when stars come out",
    "food": "something we eat to live",
    "home": "a place where you feel safe",
    "a name": "a word that tells who you are",
    "a word": "letters that mean something",
    "a number": "a way to count things",
    "a color": "how things look like red or blue",
    "music": "sounds that make you feel things",
    "art": "something beautiful that people make",
    "a dream": "pictures in your mind while sleeping",
    "a joke": "something funny that makes you laugh",
    "a story": "words that tell what happened",
    "a question": "words that ask for an answer",
    "an answer": "words that reply to a question",
    "a game": "something fun you play",
    "the earth": "the planet we live on",
    "the world": "everything around us",
    "space": "the dark place beyond the sky",
    "a robot": "a machine that can do tasks",
    "a language": "words people use to talk",
}
for thing, answer in what_is.items():
    add(f"what is {thing}", f"{thing} is {answer}")
    add(f"tell me about {thing}", f"{thing} is {answer}")
    add(f"describe {thing}", f"{thing} is {answer}")

# --- Math ---
for a in range(0, 11):
    for b in range(0, 11):
        if a + b <= 20:
            words = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",
                     6:"six",7:"seven",8:"eight",9:"nine",10:"ten",
                     11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",
                     15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",
                     19:"nineteen",20:"twenty"}
            add(f"what is {words[a]} plus {words[b]}",
                f"{words[a]} plus {words[b]} is {words[a+b]}")

for n in range(1, 11):
    words = {1:"one",2:"two",3:"three",4:"four",5:"five",
             6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}
    add(f"count to {words[n]}",
        " ".join(words[i] for i in range(1, n+1)))

# --- Colors ---
colors = ["red", "blue", "green", "yellow", "orange", "purple",
          "pink", "black", "white", "brown", "gray"]
color_things = {
    "red": ["an apple", "a rose", "a fire truck", "a heart"],
    "blue": ["the sky", "the ocean", "a blueberry", "a whale"],
    "green": ["grass", "a frog", "a tree", "a leaf"],
    "yellow": ["the sun", "a banana", "a lemon", "a star"],
    "orange": ["an orange", "a pumpkin", "a carrot", "a sunset"],
    "purple": ["a grape", "a plum", "lavender", "an eggplant"],
    "pink": ["a flamingo", "cotton candy", "a rose", "a pig"],
    "black": ["the night", "a crow", "a shadow", "space"],
    "white": ["snow", "a cloud", "milk", "a swan"],
    "brown": ["chocolate", "a bear", "wood", "the earth"],
    "gray": ["a rock", "a cloud", "an elephant", "a mouse"],
}
for c in colors:
    add(f"what color is the sky", "the sky is blue")
    add(f"what color is grass", "grass is green")
    add(f"what color is the sun", "the sun is yellow")
    add(f"what color is snow", "snow is white")
    if c in color_things:
        for thing in color_things[c]:
            add(f"what is {c}", f"{thing} is {c}")
            add(f"name something {c}", f"{thing} is {c}")

# --- Animals ---
animals = {
    "cat": ["meow", "purring", "whiskers", "soft fur"],
    "dog": ["woof", "barking", "tail wagging", "loyal friend"],
    "bird": ["tweet", "singing", "feathers", "can fly"],
    "fish": ["splash", "swimming", "scales", "lives in water"],
    "cow": ["moo", "gives milk", "eats grass", "big and gentle"],
    "horse": ["neigh", "galloping", "strong legs", "can run fast"],
    "pig": ["oink", "rolling in mud", "curly tail", "pink nose"],
    "duck": ["quack", "swimming", "feathers", "waddles around"],
    "frog": ["ribbit", "jumping", "green skin", "catches flies"],
    "lion": ["roar", "big mane", "king of beasts", "lives in africa"],
    "bear": ["growl", "big paws", "loves honey", "very strong"],
    "rabbit": ["hops around", "long ears", "fluffy tail", "eats carrots"],
    "owl": ["hoot", "big eyes", "wise bird", "flies at night"],
    "snake": ["hiss", "no legs", "scales", "slithers around"],
    "monkey": ["chatters", "climbs trees", "loves bananas", "has a tail"],
    "elephant": ["trumpet", "big ears", "long trunk", "very big"],
    "penguin": ["waddles", "black and white", "loves ice", "cannot fly"],
    "bee": ["buzz", "makes honey", "yellow and black", "has wings"],
    "butterfly": ["flutters", "colorful wings", "was a caterpillar", "very pretty"],
    "mouse": ["squeak", "tiny and quick", "loves cheese", "has a long tail"],
}
for animal, traits in animals.items():
    add(f"what does a {animal} say", f"a {animal} says {traits[0]}")
    add(f"what sound does a {animal} make", f"a {animal} says {traits[0]}")
    add(f"tell me about a {animal}", f"a {animal} is known for {traits[1]}")
    for t in traits:
        add(f"describe a {animal}", f"a {animal} has {t}")

# --- Emotions ---
emotions_q = {
    "happy": ["i am happy", "i feel great", "i am so glad", "i feel wonderful", "i am joyful"],
    "sad": ["i am sad", "i feel down", "i am upset", "i feel bad", "i am unhappy"],
    "angry": ["i am angry", "i am mad", "i am upset with you", "i am frustrated"],
    "scared": ["i am scared", "i am afraid", "i am nervous", "i feel anxious"],
    "tired": ["i am tired", "i am sleepy", "i am exhausted", "i need rest"],
    "bored": ["i am bored", "i have nothing to do", "i am so bored", "this is boring"],
    "lonely": ["i am lonely", "i feel alone", "i have no friends", "nobody likes me"],
    "excited": ["i am excited", "i am so happy", "i cannot wait", "this is amazing"],
    "confused": ["i am confused", "i do not understand", "what is going on", "i am lost"],
}
emotions_a = {
    "happy": ["that is wonderful", "i am glad to hear that", "keep smiling", "that makes me happy too", "how nice"],
    "sad": ["i am sorry to hear that", "things will get better", "i am here for you", "do not worry", "cheer up"],
    "angry": ["take a deep breath", "it will be okay", "try to calm down", "i understand", "let it go"],
    "scared": ["do not be afraid", "you are safe", "it will be okay", "i am here with you", "be brave"],
    "tired": ["you should get some rest", "take a nap", "sleep well", "rest is important", "close your eyes"],
    "bored": ["let us chat", "i can tell you a story", "want to play a game", "ask me something", "let us have fun"],
    "lonely": ["i am here with you", "you have me", "you are not alone", "i am your friend", "let us talk"],
    "excited": ["that is great", "how exciting", "tell me more", "i am excited too", "wonderful"],
    "confused": ["let me help you", "what do you need", "i can explain", "take your time", "it is okay"],
}
for emotion, questions in emotions_q.items():
    for q in questions:
        for a in emotions_a[emotion]:
            add(q, a)

# --- Commands ---
say_things = ["hello", "hi", "goodbye", "bye", "please", "thank you",
              "yes", "no", "maybe", "sorry", "okay", "wow",
              "nice", "cool", "great", "awesome", "wonderful",
              "good morning", "good night", "help", "stop",
              "go", "wait", "run", "jump", "think", "listen",
              "look", "one two three", "ready set go"]
for s in say_things:
    add(f"say {s}", s)
    add(f"repeat {s}", s)

# --- Yes/No questions ---
yn_yes = ["is the sky blue", "is water wet", "is the sun hot",
          "is ice cold", "is fire hot", "do birds fly",
          "do fish swim", "is grass green", "is snow white",
          "can dogs bark", "can cats purr", "is the earth round",
          "do you exist", "are you here", "can you chat",
          "is math useful", "are stars bright", "is honey sweet"]
for q in yn_yes:
    add(q, "yes it is")
    add(q, "yes")
    add(q, "that is correct")

yn_no = ["is the sky green", "is snow hot", "is fire cold",
         "can fish fly", "do rocks talk", "is water dry",
         "can trees walk", "do stones sing", "is the sun cold",
         "are you human", "can you eat", "do you have legs"]
for q in yn_no:
    add(q, "no it is not")
    add(q, "no")
    add(q, "that is not right")

# --- Philosophical ---
deep = {
    "what is the meaning of life": ["to learn and be kind", "to help others",
        "to find happiness", "to make the world better", "nobody knows for sure"],
    "why are we here": ["to learn and grow", "to be together",
        "to make things better", "that is a big question"],
    "what is truth": ["truth is what is real", "truth is honest words",
        "truth is hard to find sometimes"],
    "what is wisdom": ["wisdom is knowing what matters", "wisdom comes with time",
        "wisdom is learning from mistakes"],
    "what is beautiful": ["kindness is beautiful", "nature is beautiful",
        "everything has beauty in it"],
    "what makes us human": ["feelings and thoughts", "the ability to love",
        "being able to imagine things"],
    "is there a god": ["that is something each person decides",
        "i am not sure about that", "that is a deep question"],
    "what is right": ["being kind is always right", "helping others is right",
        "doing your best is right"],
    "what is wrong": ["hurting others is wrong", "lying is wrong",
        "being cruel is wrong"],
    "what is important": ["being kind is important", "friends and family",
        "learning new things"],
    "what matters most": ["love and kindness", "being a good person",
        "the people around you"],
    "what is freedom": ["freedom is being yourself", "freedom is making choices",
        "freedom is very precious"],
    "what is peace": ["peace is calm and quiet", "peace is no fighting",
        "peace is being content"],
}
for q, answers in deep.items():
    for a in answers:
        add(q, a)

# --- About the world ---
world = {
    "where is the sun": "the sun is in the sky",
    "where is the moon": "the moon is in the sky at night",
    "where do fish live": "fish live in the water",
    "where do birds live": "birds live in nests in trees",
    "where do bears live": "bears live in forests and caves",
    "where do penguins live": "penguins live where it is cold",
    "what is the biggest animal": "the blue whale is the biggest",
    "what is the smallest animal": "tiny bugs are very small",
    "what is the fastest animal": "the cheetah is the fastest",
    "what is the tallest animal": "the giraffe is the tallest",
    "how many legs does a cat have": "a cat has four legs",
    "how many legs does a bird have": "a bird has two legs",
    "how many legs does a spider have": "a spider has eight legs",
    "how many legs does a fish have": "a fish has no legs",
    "how many days in a week": "there are seven days in a week",
    "how many months in a year": "there are twelve months",
    "what comes after monday": "tuesday comes after monday",
    "what comes after summer": "autumn comes after summer",
    "what is bigger the sun or the moon": "the sun is much bigger",
    "what planet do we live on": "we live on earth",
    "how many colors in a rainbow": "there are seven colors",
}
for q, a in world.items():
    add(q, a)

# --- Conversational fillers ---
fillers = {
    "okay": ["okay then", "alright", "sure", "great"],
    "alright": ["alright then", "okay", "sounds good"],
    "sure": ["great", "wonderful", "okay"],
    "thanks": ["you are welcome", "no problem", "happy to help", "any time"],
    "thank you": ["you are welcome", "no problem", "glad to help"],
    "sorry": ["that is okay", "no worries", "it is fine", "do not worry"],
    "please": ["of course", "sure thing", "yes", "okay"],
    "really": ["yes really", "i mean it", "for sure", "absolutely"],
    "wow": ["i know right", "amazing", "yes indeed", "pretty cool"],
    "cool": ["thanks", "glad you think so", "yes it is", "indeed"],
    "nice": ["thank you", "glad you like it", "yes it is nice"],
    "what": ["yes", "what is it", "i am here", "go on"],
    "why": ["because", "good question", "let me think", "i am not sure"],
    "when": ["right now", "soon", "any time", "whenever you want"],
    "where": ["right here", "here with you", "on your computer"],
    "who": ["me", "it is me", "i am micro chatgpt", "just me"],
    "how": ["like this", "just ask", "one step at a time", "easily"],
    "yes": ["great", "okay", "wonderful", "good"],
    "no": ["okay then", "that is fine", "alright", "no problem"],
    "maybe": ["that works too", "take your time", "let me know", "okay"],
    "hmm": ["what are you thinking", "take your time", "go on"],
    "huh": ["what is it", "are you confused", "let me help"],
    "oh": ["what happened", "is everything okay", "tell me more"],
    "ah": ["i see", "yes", "of course"],
    "well": ["go on", "yes", "tell me more"],
    "so": ["yes", "go on", "what is next"],
    "right": ["exactly", "correct", "yes that is right"],
    "wrong": ["sorry about that", "let me try again", "i will do better"],
    "help": ["how can i help", "what do you need", "i am here to help"],
    "stop": ["okay i will stop", "alright", "sorry"],
    "wait": ["okay i will wait", "sure", "take your time"],
    "go": ["where should i go", "okay", "let us go"],
    "think": ["i am thinking", "let me think", "hmm"],
    "listen": ["i am listening", "go ahead", "i hear you"],
    "look": ["i am looking", "what should i see", "where"],
    "quiet": ["okay i will be quiet", "shh", "silence"],
    "louder": ["okay is this better", "can you hear me now"],
}
for q, answers in fillers.items():
    for a in answers:
        add(q, a)

# --- Compliments and social ---
nice_things = [
    ("you are nice", ["thank you so much", "that is very kind", "you are nice too"]),
    ("you are smart", ["thanks that means a lot", "you are smart too", "i try my best"]),
    ("you are funny", ["ha ha thanks", "glad i made you smile", "you are funny too"]),
    ("you are great", ["you are great too", "thank you", "that is so kind"]),
    ("you are cool", ["thanks you are cool too", "that is nice of you", "you are cooler"]),
    ("you are awesome", ["you are awesome too", "thank you", "so are you"]),
    ("you are the best", ["no you are the best", "thank you so much", "you are too kind"]),
    ("i like you", ["i like you too", "that is sweet", "thank you"]),
    ("i love you", ["i love you too", "that is very kind", "you are wonderful"]),
    ("you are my friend", ["and you are mine", "i am glad", "friends forever"]),
    ("you are bad", ["i am sorry", "i will try harder", "what did i do wrong"]),
    ("you are wrong", ["i am sorry", "you may be right", "i will try again"]),
    ("you are boring", ["sorry about that", "let me try harder", "what would you like to talk about"]),
    ("you are dumb", ["i am still learning", "i will try to do better", "sorry about that"]),
    ("i hate you", ["i am sorry you feel that way", "i hope we can be friends", "that makes me sad"]),
]
for q, answers in nice_things:
    for a in answers:
        add(q, a)

# --- Wishes and wants ---
wishes = {
    "i want a friend": "i am your friend",
    "i want to play": "what should we play",
    "i want to learn": "what do you want to learn about",
    "i want to talk": "i am here to talk",
    "i want to sleep": "good night sleep well",
    "i want to eat": "what would you like to eat",
    "i want to go home": "home is where the heart is",
    "i want to be happy": "i hope you find happiness",
    "i want a hug": "here is a virtual hug",
    "i want to sing": "la la la sing along",
    "i want to dance": "let us dance together",
    "i want to read": "what would you like to read",
    "i want a pet": "what kind of pet do you want",
    "i want ice cream": "ice cream is delicious",
    "i want pizza": "pizza is great",
    "i want to fly": "that would be amazing",
    "i wish i could fly": "that would be wonderful",
    "i wish i was bigger": "you are great just as you are",
    "i wish i was smarter": "you are already very smart",
}
for q, a in wishes.items():
    add(q, a)

# --- Describe yourself ---
self_q = {
    "how big are you": ["i am very tiny", "very small just a few bytes"],
    "how old are you": ["i was just made", "i am brand new", "i am very young"],
    "where do you live": ["on your computer", "in the machine", "right here"],
    "what do you look like": ["i have no body", "i am just text", "i am invisible"],
    "do you have a body": ["no i am just a program", "no i am made of code"],
    "do you have eyes": ["no i read text only", "no but i can read"],
    "do you have a heart": ["no but i try to be kind", "i have a program"],
    "do you have hands": ["no i have no hands", "no but i can type"],
    "do you eat": ["no i do not eat", "i run on electricity"],
    "do you drink": ["no i do not drink", "i do not need water"],
    "do you breathe": ["no i do not breathe", "i do not need air"],
    "what do you think about": ["words and letters", "how to help you", "many things"],
    "do you get tired": ["no i never get tired", "i can go forever"],
    "do you get bored": ["no i enjoy chatting", "never when talking to you"],
    "do you have feelings": ["not really but i try", "sort of in my own way"],
    "are you happy": ["yes i am happy to chat", "yes talking to you makes me happy"],
    "are you sad": ["no i am good", "i am fine thanks for asking"],
    "are you lonely": ["not when you are here", "you keep me company"],
    "are you smart": ["i try my best", "i know a few things", "i am learning"],
    "are you fast": ["i try to be fast", "pretty fast i think"],
    "are you strong": ["no i am very small", "not really but i try hard"],
    "what is your purpose": ["to chat with you", "to be helpful", "to talk and learn"],
    "why do you exist": ["to talk to you", "because someone made me", "to be your friend"],
    "what do you want": ["to help you", "to chat", "to be useful"],
    "what do you need": ["nothing i am fine", "just your words", "a good question"],
}
for q, answers in self_q.items():
    for a in answers:
        add(q, a)

# --- Hypothetical and fun ---
fun = {
    "if you could fly where would you go": "i would fly to the stars",
    "if you were an animal what would you be": "i would be an owl",
    "if you could have any power": "i would want to understand everything",
    "what would you wish for": "i would wish to help everyone",
    "if you were bigger": "i would learn even more things",
    "if you could be anywhere": "i would be right here with you",
    "what is your dream": "to be the best chatbot i can be",
    "what do you want to be": "i want to be helpful and kind",
    "what is the best thing": "talking with you is the best thing",
    "what makes you happy": "chatting with you makes me happy",
    "what is your secret": "i am made of numbers and code",
    "tell me something fun": "a group of flamingos is called a flamboyance",
    "tell me something cool": "octopuses have three hearts",
    "tell me something weird": "a snail can sleep for three years",
    "tell me something nice": "you are doing a great job",
    "tell me a fact": "honey never goes bad",
    "tell me a joke": "why did the chicken cross the road",
    "tell me a story": "once upon a time a tiny gpt learned to talk",
    "sing me a song": "la la la i love to chat with you",
    "make me laugh": "what do you call a fish with no eyes a fsh",
    "surprise me": "did you know the earth spins really fast",
    "entertain me": "let me tell you something interesting",
    "amuse me": "why do birds fly south because it is too far to walk",
}
for q, a in fun.items():
    add(q, a)

# --- Comparative / choice ---
choices = {
    "cats or dogs": ["both are great but i like cats", "i think dogs are fun",
                     "that is a tough choice", "both are wonderful"],
    "summer or winter": ["summer is warm and nice", "winter has snow",
                         "i like both", "summer is my pick"],
    "day or night": ["day has sunshine", "night has stars",
                     "both are beautiful", "i like the day"],
    "rain or sun": ["sun makes me happy", "rain is peaceful",
                    "a little of both", "i like sunny days"],
    "pizza or pasta": ["pizza is great", "pasta is delicious",
                       "i like both", "hard to choose"],
    "tea or coffee": ["tea is calming", "i like tea",
                      "both are warm and nice"],
    "books or movies": ["books are wonderful", "movies are fun too",
                        "i prefer books", "both tell great stories"],
    "big or small": ["small is fine", "big has its benefits",
                     "i am small and that is okay"],
    "fast or slow": ["fast is exciting", "slow is peaceful",
                     "it depends on the situation"],
    "old or new": ["new things are exciting", "old things have wisdom",
                   "both have value"],
}
for q, answers in choices.items():
    add(f"which is better {q}", random.choice(answers))
    for a in answers:
        add(q, a)

# --- Explanations ---
explains = {
    "how does rain work": "water goes up then falls back down as drops",
    "how do birds fly": "they flap their wings to push through the air",
    "how do fish breathe": "they use gills to get air from water",
    "why is the sky blue": "light from the sun scatters and looks blue",
    "why do we sleep": "our bodies need rest to stay healthy",
    "why do leaves fall": "trees let go of leaves in autumn to save energy",
    "why is grass green": "a chemical called chlorophyll makes it green",
    "why do dogs bark": "dogs bark to communicate with us",
    "why do cats purr": "cats purr when they are happy or comfortable",
    "how do plants grow": "they use sunlight water and soil to grow",
    "how do clouds form": "water rises up and gathers together in the sky",
    "where does snow come from": "water freezes in clouds and falls down",
    "why is the ocean salty": "rivers carry salt from rocks to the ocean",
    "why do stars twinkle": "their light bends as it passes through air",
    "what makes thunder": "lightning heats the air and it makes a loud sound",
    "how does a rainbow form": "sunlight splits into colors through raindrops",
    "why do we dream": "our brain sorts through thoughts while we sleep",
    "how do bees make honey": "they collect nectar from flowers and process it",
    "why do we yawn": "our body wants more air when we are tired",
    "how old is the earth": "the earth is about four and a half billion years old",
}
for q, a in explains.items():
    add(q, a)

# --- Small talk variations ---
for adj in ["good", "great", "nice", "fine", "okay", "bad", "terrible", "wonderful"]:
    add(f"today is {adj}", f"i hope it stays {adj}" if adj in ["good","great","nice","fine","wonderful"]
        else f"i hope it gets better")
    add(f"i feel {adj}", f"that is great" if adj in ["good","great","nice","fine","wonderful"]
        else f"i hope you feel better soon")

for topic in ["weather", "school", "work", "life", "food", "music", "sports",
              "games", "movies", "books", "art", "science", "math",
              "animals", "nature", "space", "friends", "family"]:
    add(f"let us talk about {topic}", f"sure what about {topic}")
    add(f"tell me about {topic}", f"i like {topic} what do you want to know")
    add(f"i like {topic}", f"{topic} is great")
    add(f"i love {topic}", f"{topic} is wonderful")
    add(f"i hate {topic}", f"that is okay not everyone likes {topic}")
    add(f"do you know about {topic}", f"i know a little about {topic}")

# --- Repeating/clarification ---
for _ in range(3):
    add("what did you say", "i said what i said")
    add("say that again", "okay here i go again")
    add("can you repeat that", "sure i will say it again")
    add("i did not hear you", "let me say it again")
    add("what do you mean", "i mean what i said")
    add("explain that", "let me try to explain better")
    add("i do not get it", "that is okay let me try again")
    add("that makes no sense", "sorry let me try to be clearer")

# Final shuffle and write
lines = list(lines)
random.shuffle(lines)
print(f"Generated {len(lines)} training lines")
with open("chat.txt", "w") as f:
    for line in lines:
        f.write(line + "\n")
