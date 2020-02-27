import os
import sys
import json

def classify(p_ham_dict,p_spam_dict,final_dict):
    vocab_set = set()
    nboutput_file = open('nboutput.txt','w',encoding='latin1')
    for word in final_dict.keys():
        vocab_set.add(word)
    '''for word in cond_spam_dict.keys():
        vocab_set.add(word)'''

    for root,dirs,files in os.walk(sys.argv[1],topdown=False):
        #count = 0
        for name in files:
            '''if count == 10:
                break'''
            if name.split('.')[-1] == 'txt':
                file_path = os.path.join(root,name)
            #print(file_path)
            with open(file_path,'r',encoding='latin1') as file_reader:
                doc = file_reader.read().lower().strip().split()
            p_word_ham = 0
            p_word_spam = 0
            for word in doc:
                #print(word)

                if word in vocab_set:
                    p_word_ham = p_word_ham + final_dict[word][0]
                    p_word_spam = p_word_spam + final_dict[word][1]
                    '''if word in final_dict:
                        p_word_ham = p_word_ham*final_dict[word][0]
                    else:
                        p_word_ham = p_word_ham*(1/len(vocab_set))
                    if word in cond_spam_dict:
                        p_word_spam = p_word_spam*cond_spam_dict[word]
                    else:
                        p_word_spam = p_word_spam*(1/len(vocab_set))'''
                else:
                    continue
            p_msg_ham = p_ham_dict['Probability of ham'] + p_word_ham
            p_msg_spam = p_spam_dict['Probability of spam'] + p_word_spam
            if p_msg_ham > p_msg_spam:
                '''print(p_msg_ham,end=' ')
                print(p_msg_spam,end = ' ')
                print(p_word_ham,end = ' ')
                print('ham')'''
                file_output = 'ham'+'\t'+file_path+'\n'
                nboutput_file.write(file_output)
            else:
                '''print(p_msg_ham, end=' ')
                print(p_msg_spam, end=' ')
                print(p_word_spam,end = ' ')
                print('spam')'''
                file_output = 'spam' + '\t' + file_path + '\n'
                nboutput_file.write(file_output)
            #count += 1
            #break
        #break



def read_nblearn():
    count = 0
    with open('nbmodel.txt','r') as file_reader:
        count = 0
        p_ham_dict = file_reader.readline()
        p_ham_dict = json.loads(p_ham_dict)
        #print(p_ham_dict['Probability of ham'])
        p_spam_dict = file_reader.readline()
        p_spam_dict = json.loads(p_spam_dict)
        final_dict = file_reader.readline()
        final_dict = json.loads(final_dict)
        #cond_spam_dict = file_reader.readline()
        #cond_spam_dict = json.loads(cond_spam_dict)
    classify(p_ham_dict,p_spam_dict,final_dict)




if __name__=="__main__":
    read_nblearn()
