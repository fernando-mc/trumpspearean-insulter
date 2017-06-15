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

def insulter(ins_type):
    """
    Creates an insult based on the insult type
    Insult types are: 
    Trumpian
    Shakespearean
    Trumspearean
    """
    if ins_type == 'Trumspearean':
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
            [(' ' + random.choice(trump_words[3])),'']
        )
    elif ins_type == 'Shakespearean':
        insult = (
            random.choice(shakespear_words[0]) + ' ' +
            random.choice(shakespear_words[0]) + ' ' + 
            random.choice(shakespear_words[0])
        )
    elif ins_type == 'Trumpian':
        insult = (
            random.choice(trump_words[0]) + ' ' +
            random.choice(trump_words[1]) + ' ' + 
            random.choice(trump_words[2]) + ' ' + 
            random.choice(trump_words[3])
        )
    else:
        print 'insult_type options are: \nTrumpian\nShakespearean\nTrumspearean'
        print 'Please check your config.ini file to make sure you have one of'
        print ' these set in the [settings] section'
    return insult

def load_config(config_file):
    """Read and load settings and credentials from config.ini"""
    Config = ConfigParser.ConfigParser()
    Config.read('./config.ini')
    return {
        'insult_type': Config.get('settings', 'insult_type'),
        'run_type': Config.get('settings', 'run_type'),
        'consumer_key': Config.get('credentials', 'consumer_key'),
        'consumer_secret': Config.get('credentials', 'consumer_secret'),
        'access_token_key': Config.get('credentials', 'access_token_key'),
        'access_token_secret': Config.get('credentials', 'access_token_secret')
    }

def streaming_insulter():
    

def periodic_insulter():
    insulter()


acceptable_run_types = ['streaming', 'periodic']
if run_type not in acceptable_run_types:






