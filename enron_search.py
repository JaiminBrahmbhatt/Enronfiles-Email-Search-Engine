import mailbox
import re
import sys
import os

# Function to take input of the term to be searched using system argument
def input_term():
    term = ' '.join(sys.argv[1:])
    term = str(term) # Convert to string
    # Converting string to same case so that algorithm won't discard uppercase terms as different from lowercase terms
    term = term.lower() 
    term = unique_list(term.split())
    return term

# Function to get only unique values in search term
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    return ulist

# Function to search if the all search terms are present and print the results
def search(term, ENRON_FILE):
    input = term
    mbox_file = ENRON_FILE
    mbox = mailbox.mbox(mbox_file)
    count = 0 
    for i,message in enumerate(mbox):
        content=''
        if message.is_multipart():
            content = ''.join(msg.get_payload() for msg in message.get_payload())
        else:
            content = message.get_payload()
        content=str(content)
        containsstring=True
        for word in input:
            containsstring*=bool(re.search('\\b'+word+'\\b',content,re.IGNORECASE))
            if(not(containsstring)):
                break
        if(containsstring):
            print("{}. {} {} {}".format(count+1, message['x-from'], '<' + message['from'] + '>',message['date']))
            count = count + 1
    print ('Results found:', count)
        
def main():
    term = input_term()
    if os.environ.get('ENRON_FILE'):
        ENRON_FILE = os.environ.get('ENRON_FILE')
        search(term, ENRON_FILE)
    else: 
        ENRON_DIR = '/mnt/c/Users/jaimi/ComputerForensics/enron'
    # Looping over the given directory and making list of all the available files in the list
        filename = []
        for i in os.listdir(ENRON_DIR):
            name = ENRON_DIR + '/' + i
            filename.append(name)
        for names in filename:
            search(term, names)

if __name__ == "__main__":
    main()

#Jaimin Brahmbhatt