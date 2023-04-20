# Program coding:
one_sequence='actgatcgattgatcgatcgatcg'
another_sequence='tttagatcgatctttgatc'
def score_match(subject,query,subject_start,query_start,length):
    score=0
    for i in range(0,length):
        subject_base=subject[subject_start+i]
        query_base=query[query_start+i]
        if subject_base==query_base:
            score=score+1
        else:
            score=score-1
    return score
print(score_match(one_sequence,another_sequence,7,4,8))
print(score_match(one_sequence,another_sequence,7,4,4))
print(score_match(one_sequence,another_sequence,7,4,12))
print(score_match(one_sequence,another_sequence,10,1,5))

# Output:	
# 6
# 2
# 4
# -1
