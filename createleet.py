#!/usr/bin/python
# -*- coding: utf-8 -*-



# Denne tar som input en regexfil på formen:
#
# a=[aA4]
# b=(morestuff|yeh)
# ..
# 
# og en annen fil som inneholder en mengde ord,
# og erstatter bokstanvene i ordene med de over. 
# f.eks
#
# ape
# apekatt
#
# vil da outputte:
# [aA4]k[aA4]tt
#
# Dette kan da igjen brukes til rexgen for å generere leetspeek passord.
#
#
# for each line in regexfil:
#  
import os, sys,re,argparse

parser = argparse.ArgumentParser()
parser.add_argument("--rf", help="file containing regexes to use. If not supplied, default will be used")
parser.add_argument("--wlf", help="file containing words you want to leettransform")
parser.add_argument("--capstart", help="capitalize only the initial character in the line",action="store_true")
parser.add_argument("--addexclandone", help="for each password, create a version containing a trailing 1 and another version containing a trailing !",action="store_true")
parser.add_argument("--years",help="also add the years 2016, 2017 and 2018",action="store_true")
args = parser.parse_args()

if not args.wlf:
	print("Usage:")
	print("./createleet.py --wlf muligepassord")
	print("example of builtin rf:")
	print("a=[aA4@]")
	print("b=[bB8]")
	print("c=[c(C]")
	print("d=[dD]")
	print("e=[eE3]")
	print("f=[fF]")
	print("g=[gG9]")
	print("h=[hH]")
	print("i=[iI!1]")
	print("j=[jJ]")
	print("k=[kK]")
	print("l=[lL1]")
	print("m=[mM]")
	print("n=[nN]")
	print("o=[oO0]")
	print("p=[pP]")
	print("q=[qQ]")
	print("r=[rR]")
	print("s=[sS$5]")
	print("t=[tT+7]")
	print("u=[uU]")
	print("v=[vV]")
	print("w=[wW]")
	print("x=[xX]")
	print("y=[yY]")
	print("z=[zZ]")
	exit(1)
elif (not args.rf):
	regexes={'a': '[aA4@]', 'b': '[bB8]', 'c': '[cC]', 'd': '[dD]', 'e': '[eE3]', 'f': '[fF]', 'g': '[gG9]', 'h': '[hH]', 'i': '[iI!]', 'j': '[jJ]', 'k': '[kK]', 'l': '[lL1]', 'm': '[mM]', 'n': '[nN]', 'o': '[oO0]', 'p': '[pP]', 'q': '[qQ]', 'r': '[rR]', 's': '[sS$5]', 't': '[tT+7]', 'u': '[uU]', 'v': '[vV]', 'w': '[wW]', 'x': '[xX]', 'y': '[yY]', 'z': '[zZ]'}
	wlf=args.wlf
else:
	regexes=dict()
	#print(sys.argv[1])
	with open(args.rf) as f:
		for line in f:
			regexes[line.split("=")[0]]=line.split("=")[1].strip()
	f.close()
	wlf=args.wlf


if (args.capstart):
	for i in regexes.keys():
		# Removes the upper character
		regexes[i]=regexes[i].replace(i.upper(),'')


with open(wlf) as f:
	for line in f:
		l=line.strip()
		checkcapstart='nowaythiscancomeup'
		mystring="rexgen '"
		for x in l:
			if (args.capstart and len(checkcapstart)==1):
				regexes[checkcapstart]=regexes[checkcapstart].replace(checkcapstart.upper(),'')
				checkcapstart='shitisreversed'
			if (args.capstart and checkcapstart=='nowaythiscancomeup'):
				if (x in regexes):
					regexes[x]=regexes[x].replace(x.lower(),str(x.lower()+x.upper()))
					checkcapstart=x



			if (x in regexes):
				mystring+=regexes[x]
			else:
				mystring+=x
		if (args.addexclandone):
			print(mystring+"'")
			print(mystring+"[1!]'")
		else:
			print(mystring+"'")
#print(regexes)
