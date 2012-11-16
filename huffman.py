def encode(string,tree):
	return encode0(string,tree,tree,"")
	
def encode0(s,node,tree,op):
	if s=='':
		return op
	elif node.left==None:
		return encode0(s[1:],tree,tree,op)
	elif s[0] in node.left.chars:
		return encode0(s,node.left,tree,op+'0')
	else:
		return encode0(s,node.right,tree,op+'1')

def decode(string,tree):
	return(decode0(string,tree,tree,""))

def decode0(s,node,tree,op):
	if s=="":
		return(op+node.chars)
	elif node.left==None:
		return(decode0(s,tree,tree,op+node.chars))
	elif s[0]=='0':
		return(decode0(s[1:],node.left,tree,op))
	else:	
		return(decode0(s[1:],node.right,tree,op))

def makeCodeTree(sample):
	nodes=sorted([fork(i,j) for (i,j) in freq(sample).items()],key=lambda x:x.weight)
	while len(nodes) > 1:
		nodes=sorted(([fork(nodes[0].chars+nodes[1].chars,nodes[0].weight+nodes[1].weight,nodes[0],nodes[1])]+nodes[2:]),key=lambda x:x.weight)
	return(nodes[0])
	
class fork:		
	def __init__(self, chars, weight, left=None, right=None):
		self.chars=chars
		self.weight=weight
		
		self.left=left
		self.right=right

def freq(s):
	frq={}
	for i in s :
		if i in frq:
			frq[i]=frq[i]+1
		else:
			frq[i]=1
	return(frq)

def makecodList(codeTree):	
	codList=makecodList0(codeTree)
	codList0={}
	for (i,j) in codList:
		codList0[i]=j
	return(codList0)

def makecodList0(tree):
	if tree.left == None :
		return [(tree.chars,'')]
	rTable=makecodList0(tree.right)
	lTable=makecodList0(tree.left)
	return [(i,'0'+j) for (i,j) in lTable]+[(i,'1'+j) for (i,j) in rTable]		
	
def quickEncode(string,codList):
	op=""
	for i in string:
		op=op+codList[i]
	return op
		
def test():
	print 'tree optimised for "qwertyuiopasdfghjklzxcvbnm" created'
	tree=makeCodeTree("qwertyuiopasdfghjklzxcvbnm")
	table=makecodList(tree)
	print "code table:" ,table
	print 'string: "asdf" code: ', encode("asdf",tree)
	print 'code: "11100111011001010011" string: ', decode("11100111011001010011",tree)
test()

