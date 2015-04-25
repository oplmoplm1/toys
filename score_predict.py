
scores={'person1':{'math1':90,'math2':92,'math3':88,'math4':99,'math5':100},
'person2':{'math1':70,'math3':80,'math9':50,'math5':77},
'person3':{'math1':66,'math4':88, 'math9':99, 'math6':78, 'math7':79},
'person4':{'math2':55, 'math4':79, 'math5':66, 'math7':66,'math9':99},
'person5':{'math3':33, 'math4':44, 'math6':55, 'math8':66},
'person6':{'math1':77, 'math8':67, 'math4':99, 'math7':75}
}
#Pearson correlation score
import math
def similarity(scores,person1, person2):
	sim={}
	for item in scores[person1]:
		if item in scores[person2]:
			sim[item]=1
	
	n = len(sim)
	if n==0: return n
	
	sum1 = sum([scores[person1][item] for item in sim])
	sum2 = sum([scores[person2][item] for item in sim])
	
	sum1_square = sum([pow(scores[person1][item],2) for item in sim])
	sum2_square = sum([pow(scores[person2][item],2) for item in sim])
	
	score_sum = sum([scores[person1][item]*scores[person2][item] for item in sim])
	
	numerator = score_sum -(sum1*sum2)/n
	denominator = math.sqrt((sum1_square - pow(sum1,2)/n)*(sum2_square -pow(sum2,2)/n))
	
	result = numerator/denominator
	return result
	
def getPredicts(scores, person):
	totals={}
	sum_similarity={}
	for other in scores:
		if other == person: continue
		sim = similarity(scores,person,other)
		if sim<=0:continue
		for item in scores[other]:
			if item not in scores[person] or scores[person][item]==0:
				totals.setdefault(item,0)
				totals[item]+=scores[other][item]*sim
				sum_similarity.setdefault(item,0)
				sum_similarity[item]+=sim
		
	rank = [(total/sum_similarity[item],item) for item, total in totals.items()]
	rank.sort()
	rank.reverse()
	return rank

def tonimoto(scores,person1,person2):
	intersection = 0
	union = len(scores[person1])+len(scores[person2])
	if union ==0: return 0
	for score in scores[person1]:
		if score in scores[person2]:
			intersection = intersection +1	
	return intersection/union