def oneAway(s1,s2):
	dict={}
	for i in range(0,len(s1)):
		if s1[i] in dict:
			dict[s1[i]]=dict[s1[i]]+1
		else:
			dict[s1[i]]=1
	if(abs(len(s1)-len(s2))>1):
		return "False"

	return check(dict,s1,s2)
def check(d,s1,s2):
	count=0
	if(len(s1)==len(s2)):
		for i in range(0,len(s2)):
			if s2[i] in d:
				pass
			else:
				count=count+1;
				if(count>1):
					return -1
		for i in d:
		  		if(d[i]>0):
		  			return "False"
		return "True"
	else:
		# for i in range(0,len(s2)):
		# 	if s2[i] in d:
		# 		if(d[s2[i]]==0):
		# 			return "False"
		# 		d[s2[i]]=d[s2[i]]-1
		# 		pass
		# 	else:
		# 		count=count+1
		# 		if(count>1):
		# 			return "False"
		# return "True"
		  	for i in range(0,len(s2)):
		  		if s2[i] in d:
		  			if(d[s2[i]]==0):
		  				return "False"
		  			d[s2[i]]=d[s2[i]]-1
		  		else:
		  			count=count+1
		  			if(count>1):
		  				return "False"
		  	for i in d:
		  		if(d[i]>0):
		  			return "False"
		  	return "True"



print(oneAway("supraja","supejaa"))


	


