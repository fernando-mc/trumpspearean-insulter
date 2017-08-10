import ConfigParser

def load_config(config_file):
    """Read and load settings and credentials from config.ini"""
    Config = ConfigParser.ConfigParser()
    Config.read('./config.ini')
    config = {
        'insult_type': Config.get('settings', 'insult_type').title(),
        'run_type': Config.get('settings', 'run_type').lower(),
        'consumer_key': Config.get('credentials', 'consumer_key'),
        'consumer_secret': Config.get('credentials', 'consumer_secret'),
        'access_token_key': Config.get('credentials', 'access_token_key'),
        'access_token_secret': Config.get('credentials', 'access_token_secret')
    }
    errors = []
    if not config['consumer_key']:
        errors.append(
            'Please check to make sure that your consumer_key is'
            'set in the config.ini file'
        )
    if not config['consumer_secret']:
        errors.append('Please check to make sure that your consumer_secret is'
        'set in the config.ini file'
        )
    if not config['access_token_key']:
        errors.append(
            'Please check to make sure that your access_token_key is'
            'set in the config.ini file'
        )
    if not config['access_token_secret']:
        errors.append('Please check to make sure that your access_token_secret is'
        print 'set in the config.ini file'
    if config['run_type'] not in ['streaming', 'periodic']:
        print "Run type not in acceptable run types. "
        print "Options are\n1. 'streaming'\n2. 'periodic'"
    return config