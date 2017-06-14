import ConfigParser
import insults
import random

trump_words = [
    insults.FIRST_TRUMPIAN_WORDS, 
    insults.SECOND_TRUMPIAN_WORDS, 
    insults.THIRD_TRUMPIAN_WORDS, 
    insults.FORTH_TRUMPIAN_ADDITIONS
]

shakespear_words = [
    insults.FIRST_SHAKESPEAREAN_WORDS,
    insults.SECOND_SHAKESPEAREAN_WORDS,
    insults.THIRD_SHAKESPEAREAN_WORDS
]

word_types = [trump_words, shakespear_words]
# Setup the Trumpian and Shakespearean insult words we're using
# Combinations have three parts with a potential Trumpian addition. 
# "first_word second_word third_word [forth_word]"

# The setup is affected by the config options in config.ini
# Options are:
# Trumpian, Shakespearean and Trumspearean
# The default is Trumpian

# Load config
# Config = ConfigParser.ConfigParser()
# Config.read('config.ini')

# insult_type = load_config.get(insult_type)

def insulter(ins_type):
    """Sends an insult to Donald Trump"""
    if ins_type = 'Trumpian':
        insult = (
            random.choice(trump_words[0]) + ' ' +
            random.choice(trump_words[1]) + ' ' + 
            random.choice(trump_words[2]) + ' ' + 
            random.choice(trump_words[3])
        )
    elif ins_type = 'Shakespearean':
        insult = (
            random.choice(shakespear_words[0]) + ' ' +
            random.choice(shakespear_words[0]) + ' ' + 
            random.choice(shakespear_words[0])
        )
    elif ins_type = 'Trumspearean':
        # Generate structure
        structure = []
        for i in range(0,3):
            structure.append(random.randint(0,1))

        # Generate base insult with randomized structure
        insult = ''
        for position, item in enumerate(structure):
            insult += (random.choice(word_types[item][position - 1]) + ' ')
        insult = insult[:-1]
        # Potentailly add optional Trump addition
        insult += random.choice(
            random.choice(
                (' ' + trump_words[3]), 
                ''
            )
        )




def streaming_handler():
    

else:
    print 'insult_type options are: \nTrumpian\nShakespearean\nTrumspearean'
    print 'Please check your config.ini file to make sure you have one of'
    print ' these set in the [settings] section'

random.choice()






