import os
import sys
import json
import math
from collections import Counter
def calc_spam_ham_prob(final_dict,total_count,spam_count,ham_count,ham_file,spam_file):
    cond_ham_spam = {}
    #cond_spam = {}
    p_ham = math.log(ham_file/(ham_file+spam_file),2)
    p_spam = math.log(spam_file/(ham_file+spam_file),2)
    vocab_set = set()

    #Vocabulary size
    for word in final_dict.keys():
        vocab_set.add(word)
    '''for word in spam_dict.keys():
        vocab_set.add(word)'''
    #print(len(vocab_set))

    #Conditional probability
    for word in final_dict:
        p_word_ham = math.log((final_dict[word][0]+1)/(ham_count + len(vocab_set)),2)
        p_word_spam = math.log((final_dict[word][1]+1)/(spam_count + len(vocab_set)),2)
        final_dict[word] = (p_word_ham,p_word_spam)
    '''for word in spam_dict:
        p_word_spam = (spam_dict[word]+1)/(spam_count + len(vocab_set))
        cond_spam[word] = p_word_spam'''
    return p_ham,p_spam,final_dict


def create_spam_ham_dict():
    final_dict = {}
    #ham_dict = {}
    total_count = 0
    spam_count = 0
    ham_count = 0
    ham_file = 0
    spam_file = 0
    count = 0
    for root,dirs,files in os.walk(sys.argv[1],topdown=False):
        for name in files:
            file_path = os.path.join(root,name)
            file_reader = open(file_path,'r',encoding = "latin1")
            #splitting file path
            if '\\' in file_path:
                check_folder = file_path.split("\\")[-2]
            elif '/' in file_path:
                check_folder = file_path.split('/')[-2]

            #check spam or ham folder
            if check_folder == 'ham':
                ham_file += 1
                word_list = file_reader.read().lower().split()
                for word in word_list:
                    if word in final_dict:
                        ham_word_no = final_dict[word][0]
                        ham_word_no += 1
                        final_dict[word][0] = ham_word_no

                        total_count += 1
                    else:
                        final_dict[word] = [1,0]
                        total_count += 1
                    ham_count += 1
            elif check_folder == 'spam':
                spam_file += 1
                word_list = file_reader.read().lower().split()
                for word in word_list:
                    if word in final_dict:
                        spam_word_no = final_dict[word][1]
                        spam_word_no += 1
                        final_dict[word][1] = spam_word_no
                        #final_dict[word][1] += 1
                        total_count += 1
                    else:
                        final_dict[word] = [0,1]
                        total_count += 1
                    spam_count += 1
    #print(ham_count,spam_count,total_count,ham_file,spam_file)
    p_ham,p_spam,final_dict = calc_spam_ham_prob(final_dict,total_count,spam_count,ham_count,ham_file,spam_file)
    return p_ham,p_spam,final_dict

if __name__ == "__main__":
    p_ham, p_spam, final_dict = create_spam_ham_dict()
    with open('nbmodel.txt','w',encoding='latin1') as file_writer:
        json.dump({"Probability of ham":p_ham},file_writer)
        file_writer.write('\n')
        #file_writer.write("Probability of ham: "+str(p_ham)+'\n')
        #file_writer.write("Probability of spam: "+str(p_spam)+'\n')
        json.dump({"Probability of spam":p_spam},file_writer)
        file_writer.write('\n')
        json.dump(final_dict,file_writer)
        '''file_writer.write('\n')
        json.dump(cond_spam,file_writer)'''














