#! python
# mclip.py - paste multiple phrases into clipboard

TEXT = {'agree': 'Yes I agree. That sounds fine to me.',
        'busy': 'Sorry, can we do this later this week or next week?',
        'upsell': 'Would you consider maknig this a monthly donation?'}

import sys, pyperclip
if len(sys.argv) < 2:
    print('To copy phrase text, enter: python mclip.py [keyphrase]')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print("Text for " + keyphrase + " copied to clipboard.")
else:
    print("There is no text for " + keyphrase)
