def CompressedString(s):
	d ={}
	l=list()
	for i in range(len(s)):
		if s[i] in d:
			d[s[i]]=d[s[i]]+1
		else:
			d[s[i]]=1
	for i in d:
		l.append(i)
		l.append(d[i])
	s1=''.join(map(str,l))

	if(len(s)==len(s1)):
		return s
	elif(len(s1)>len(s)):
		return s
	else:
		return s1


def main():
	s=str(input().strip())
	print(CompressedString(s))
main()
		
