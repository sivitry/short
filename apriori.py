from apyori import apriori

data = [['r', 'z', 'h', 'j', 'p'],
       ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
       ['z'],
       ['r', 'x', 'n', 'o', 's'],
       ['y', 'r', 'x', 'z', 'q', 't', 'p'],
       ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']]

association_rules = apriori(data, min_support=0.16, min_confidence=0.2, min_lift=3, max_length=2) 
association_results = list(association_rules)

for item in association_results:
   pair = item[0] 
   items = [x for x in pair]
   print("Rule: " + items[0] + " -> " + items[1])
   print("Support: " + str(item[1]))
   print("Confidence: " + str(item[2][0][2]))
   print("Lift: " + str(item[2][0][3]))
   print("=====================================")
