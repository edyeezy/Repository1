# CH CH CH CHANGES DONT WANNA BLA BLA BLA
## Welcome to my code! I only worked through the first episode of season 6
# THis is the latest version, 248 monday

def main():
	#Alright so this is a python list, like an array of words. This is the girl's names in alphabetical order, only the first 3 letters
	alphlist = ['Ale','Ali','Aud','Dia','Gel','Jad','Key','Nic', 'Nur','Uch','Zoe']
	
	#I did not end up needing this list of guys for the equation, just used it for the end result graph asthetic. However, it's somewhat useful to know their names
	#in this order, as you'll see in a few lines
	boylist = ['Ant','Clint','Dim','Eth', 'Joe', 'Kar', 'Kei', 'Mal', 'Mic', 'Sha', 'Tyl']
	
	#This count number is gonna be incremented everytime a possible scenario is found
	count = 0
	
	#Here is the first matchup array for week 1, season 6. refer to the  boyslist to see who is sitting with who. for example,
	#Geles is with Antony, etc.  Below is the number of beams they got, in this case it was 3
	matchup1 = ['Gel', 'Uch', 'Dia', 'Jad', 'Zoe', 'Ali', 'Ale', 'Nur', 'Key', 'Aud', 'Nic']
	m1beamsreal = 3

	temp =[22]*11

	#just a fancy way of making a 11 by 11 matrix/2Dlist full of the number 0, which I will add to to make the percentages
	probmatrix = [[0]*11 for _ in range(11) ]

	#alright so I promise I'm not mysognist. but i got confused for what the variables meant (there are a lot) so I assigned them
	#based off of what guy chose what girl. Idk about matlab, but in python this is how you iterate through a list. so when it says
	# for antgirl in alphlist, I'm saying for every possible Antony match within the alphlist (list of girls). so it starts with Antony
	# matching with Ale, then runs though every scnenario following from that
	for antgirl in alphlist: #1
		#just put this print statment so I could see progress through all the potential ladiez
		print ("checking through every scenario where Antony's mate is " +antgirl) #0
		#Here is cligirl, AKA every possible Clint mate. So after antgirl starts with Ale, then this one also starts with Ale (unless Ant alread
		# y has Ale! That is why I put "if antgirl!=cligirl" on line 35 because they can't have the same girl. how sad
		for cligirl in alphlist: #2
			if antgirl != cligirl and antgirl!= 'Gel': #1
				for dimgirl in alphlist: #3
					#so look at this one, dim, cli, and ant cannot have the same girl
					if dimgirl!=cligirl and dimgirl!=antgirl: #2
						for ethgirl in alphlist: #4
							#whoah! we found our first confirmed NO match. Ethan's girl is not Keyana. So ethgirl != Key! woo!
							if ethgirl!=dimgirl and ethgirl!=cligirl and ethgirl!=antgirl and ethgirl!= 'Key': #wk1 ethan and key no match
								for joegirl in alphlist: #5
									if (joegirl!=ethgirl and joegirl!=dimgirl and joegirl!=cligirl and joegirl!=antgirl):  #4
										for kargirl in alphlist: #6
											if (kargirl!=joegirl and kargirl!=ethgirl and kargirl!=dimgirl and kargirl!=cligirl and kargirl!=antgirl): #5
												for keigirl in alphlist: #7
													if (keigirl!=kargirl and keigirl!=joegirl and keigirl!=ethgirl and keigirl!=dimgirl and keigirl!=cligirl and keigirl!=antgirl): #6
														for malgirl in alphlist: #8
															if (malgirl!=keigirl and malgirl!=kargirl and malgirl!=joegirl and malgirl!=ethgirl and malgirl!=dimgirl and malgirl!=cligirl and malgirl!=antgirl): #7
																for micgirl in alphlist: #9
																	if (micgirl!= malgirl and micgirl!=keigirl and micgirl!=kargirl and micgirl!=joegirl and micgirl!=ethgirl and micgirl!=dimgirl and micgirl!=cligirl and micgirl!=antgirl): #8
																		for shagirl in alphlist: #10
																			if (shagirl!= micgirl and shagirl!= malgirl and shagirl!=keigirl and shagirl!=kargirl and shagirl!=joegirl and shagirl!=ethgirl and shagirl!=dimgirl and shagirl!=cligirl and shagirl!=antgirl): #9
																				for tylgirl in alphlist: #11
																					if (tylgirl!=shagirl and tylgirl!= micgirl and tylgirl!= malgirl and tylgirl!=keigirl and tylgirl!=kargirl and tylgirl!=joegirl and tylgirl!=ethgirl and tylgirl!=dimgirl and tylgirl!=cligirl and tylgirl!=antgirl): #10
																						
																						#you'll see what this is for in a sec~
																						week1beamtest = 0

																						#this temp (temporary list) basically stores the current order of the girls in a given scenario
																						temp = [antgirl,cligirl,dimgirl,ethgirl,joegirl,kargirl,keigirl,malgirl,micgirl,shagirl,tylgirl]
																					
																						
																						#for each value in the temporary array of girls (which goes through every order btw)
																						for t in range(0, len(temp)):
																							#if specific matchup in the temporary scenarario matches up with the matchup scenario seating
																							#position, the value week1beems is incremented. Since their seating got them 3 beems,
																							#this only counts if it equals 3!
																							if (temp[t] == matchup1[t]):
																								week1beamtest+=1
							
																						#if the current scenario has 3 beems, it is a legit scenario. Let's update the possibility matrix here		
																						if week1beamtest == m1beamsreal:
																							for lmao in range(0, len(temp)):
																								if temp[lmao]=='Ale':
																									probmatrix[0][lmao]+=1
																								elif temp[lmao]=='Ali':
																									probmatrix[1][lmao]+=1
																								elif temp[lmao]=='Aud':
																									probmatrix[2][lmao]+=1
																								elif temp[lmao]=='Dia':
																									probmatrix[3][lmao]+=1
																								elif temp[lmao]=='Gel':
																									probmatrix[4][lmao]+=1
																								elif temp[lmao]=='Jad':
																									probmatrix[5][lmao]+=1
																								elif temp[lmao]=='Key':
																									probmatrix[6][lmao]+=1
																								elif temp[lmao]=='Nic':
																									probmatrix[7][lmao]+=1
																								elif temp[lmao]=='Nur':
																									probmatrix[8][lmao]+=1
																								elif temp[lmao]=='Uch':
																									probmatrix[9][lmao]+=1
																								elif temp[lmao]=='Zoe':
																									probmatrix[10][lmao]+=1
																							#valid scenario, so our valid scenario counter goes up
																							count+=1

	#spits out total match scenarios possible, useful for percentage sake								
	print(str(count) + ' total possible match schenarios')

	#This is just making the probability matrix look fresh, not a big deal

	print ('        ' + boylist[0] + '     ' + boylist[1] + '   ' + boylist[2] + '     ' + boylist[3] + '     ' + boylist[4] + '     ' + boylist[5] + '     ' + boylist[6] + '     ' + boylist[7] + '     ' + boylist[8] + '     ' + boylist[9] + '     ' + boylist[10] )
	whups = 0
	for okm in probmatrix:
		print(alphlist[whups] + '     '  + str(round(100*round(okm[0]/count,3),1)) +  '     ' + str(100*round(okm[1]/count,3)) +  '     ' + str(100*round(okm[2]/count,3)) +  '     ' + str(100*round(okm[3]/count,3)) +  '     ' + str(100*round(okm[4]/count,3)) +  '     ' + str(100*round(okm[5]/count,3)) +  '     ' + str(100*round(okm[6]/count,3)) + '     ' +  str(100*round(okm[7]/count,3)) +  '     ' +  str(round(100*round(okm[8]/count,3),1)) +  '     ' + str(round(100*round(okm[9]/count,3),1)) +  '     ' + str(100*round(okm[10]/count,3)) )
		whups+=1


if __name__ == "__main__":
	main()