import os
import sys



def calc_metrics(tp,fp,tn,fn):
    precision_spam = tp/(tp+fp)
    recall_spam = tp/(tp+fn)
    precision_ham = tn/(tn+fn)
    recall_ham = tn/(tn+fp)
    f1_spam = (2*precision_spam*recall_spam)/(precision_spam+recall_spam)
    f1_ham = (2 * precision_ham * recall_ham) / (precision_ham + recall_ham)
    return precision_ham,recall_ham,f1_ham,precision_spam,recall_spam,f1_spam

def evaluate(label,true_label,tp,fp,tn,fn):
    if true_label == 'ham':
        if label == 'ham':
            tn += 1
        elif label == 'spam':
            fp += 1
    elif true_label == 'spam':
        if label == 'spam':
            tp += 1
        elif label == 'ham':
            fn += 1
    return tp,fp,tn,fn

def read_output_file(tp,fp,tn,fn):
    with open(sys.argv[1],'r') as evaluation_file:
        for line in evaluation_file.readlines():
            #print(line)
            label,path = line.split('\t')[0],line.split('\t')[1]
            if '\\' in path:
                check_folder = path.split("\\")[-2]
            elif '/' in path:
                check_folder = path.split('/')[-2]
            if check_folder == 'ham':
                tp,fp,tn,fn = evaluate(label,'ham',tp,fp,tn,fn)
            elif check_folder == 'spam':
                tp,fp,tn,fn = evaluate(label,'spam',tp,fp,tn,fn)
            else:
                continue
        return tp,fp,tn,fn

if __name__ == '__main__':
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    tp,fp,tn,fn = read_output_file(tp,fp,tn,fn)
    precision_ham,recall_ham,f1_ham,precision_spam,recall_spam,f1_spam = calc_metrics(tp,fp,tn,fn)
    print('Precision Ham: ',precision_ham)
    print('Recall Ham: ',recall_ham)
    print('F1 Score Ham ',f1_ham)
    print()
    print('Precision Spam: ', precision_spam)
    print('Recall Spam: ', recall_spam)
    print('F1 Score Spam ', f1_spam)

