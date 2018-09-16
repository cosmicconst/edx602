import random

articles = ['the','a','an']
subjects = ['cat','dog','man','woman']
verbs = ['sang','ran','jumped']
adverbs = ['loudly','quietly','well','badly']
#article, subject verb and adverb

# choose between article, subject, verb and adverb OR article , subject and verb.

for i in range(5):
    choose = random.randint(0,1)
    if choose == 0:
        print(random.choice(articles) + " " + random.choice(subjects) + " " + random.choice(verbs) + " " + random.choice(adverbs))
    else:
        print(random.choice(articles) + " " + random.choice(subjects) + " " + random.choice(verbs))

        
        
