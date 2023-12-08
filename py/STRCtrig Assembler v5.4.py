from eudplib import *
from eudx import *
import math
import os

PRT_SetInliningRate(0)

NSQCASM = EUDVariable()
EUDRegisterObjectToNamespace("NSQCASM", NSQCASM)

def f_maskread_epdZ(targetplayer, mask, _readerdict={}):

	if mask in _readerdict:
		readerf = _readerdict[mask]
	else:
		def bits(n):
			while n:
				b = n & (~n+1)
				yield b
				n ^= b

		@EUDFunc
		def readerf(targetplayer):

			f_setcurpl(targetplayer)

			ret = EUDVariable()
			ret << -1452249

			# Fill flags
			for i in bits(mask):
				RawTrigger(
					conditions=[
						DeathsX(CurrentPlayer, Exactly, i, 0, i)
					],
					actions=[
						ret.AddNumber(i//4)
					]
				)

			return ret

		_readerdict[mask] = readerf

	return readerf(targetplayer)

def f_maskread_epdY(targetplayer, mask, _readerdict={}):

	if mask in _readerdict:
		readerf = _readerdict[mask]
	else:
		def bits(n):
			while n:
				b = n & (~n+1)
				yield b
				n ^= b

		@EUDFunc
		def readerf(targetplayer):

			f_setcurpl(targetplayer)

			ret = EUDVariable()
			ret << 0

			# Fill flags
			for i in bits(mask):
				RawTrigger(
					conditions=[
						DeathsX(CurrentPlayer, Exactly, i, 0, i)
					],
					actions=[
						ret.AddNumber(i)
					]
				)

			return ret

		_readerdict[mask] = readerf

	return readerf(targetplayer)


def f_maskread_epdX(mask, _readerdict={}):

	if mask in _readerdict:
		readerf = _readerdict[mask]
	else:
		def bits(n):
			while n:
				b = n & (~n+1)
				yield b
				n ^= b

		@EUDFunc
		def readerf():

			ret = EUDVariable()
			ret << 0

			# Fill flags
			for i in bits(mask):
				RawTrigger(
					conditions=[
						DeathsX(CurrentPlayer, Exactly, i, 0, i)
					],
					actions=[
						ret.AddNumber(i)
					]
				)

			return ret

		_readerdict[mask] = readerf

	return readerf()

def bits(n):
	while n:
		b = n & (~n+1)
		yield b
		n ^= b

file1 = 'TRIGP1.chk'
file2 = 'TRIGP2.chk'
file3 = 'TRIGP3.chk'
file4 = 'TRIGP4.chk'
file5 = 'TRIGP5.chk'
file6 = 'TRIGP6.chk'
file7 = 'TRIGP7.chk'
file8 = 'TRIGP8.chk'
batpath = ""
batname = ""
batcheck = 0
for k, v in settings.items():
	if k.lower() == "path":
		file1 = v + file1
		file2 = v + file2
		file3 = v + file3
		file4 = v + file4
		file5 = v + file5
		file6 = v + file6
		file7 = v + file7
		file8 = v + file8
		batpath = v
	elif k.lower() == "bat":
		batcheck = 1
		batname = v + batname #맵이름.bat

if batcheck == 1:
	os.system(batpath+batname+".bat")
	LoadMap(batpath+batname+"_out.scx")

from os.path import getsize
file_size1 = getsize(file1)
file_size2 = getsize(file2)
file_size3 = getsize(file3)
file_size4 = getsize(file4)
file_size5 = getsize(file5)
file_size6 = getsize(file6)
file_size7 = getsize(file7)
file_size8 = getsize(file8)


def onPluginStart(): # Ctrig Assembler v5.4 for Tep Made by Ninfia
	

	global NSQCASM, file_size1, file_size2, file_size3, file_size4, file_size5, file_size6, file_size7, file_size8, file1, file2, file3, file4, file5, file6, file7, file8
	SizeP1 = EUDVariable()
	SizeP2 = EUDVariable()
	SizeP3 = EUDVariable()
	SizeP4 = EUDVariable()
	SizeP5 = EUDVariable()
	SizeP6 = EUDVariable()
	SizeP7 = EUDVariable()
	SizeP8 = EUDVariable()
	SizeP1 << file_size1
	SizeP2 << file_size2
	SizeP3 << file_size3
	SizeP4 << file_size4
	SizeP5 << file_size5
	SizeP6 << file_size6
	SizeP7 << file_size7
	SizeP8 << file_size8

	TRIGP1chk = Db(open(file1, 'rb').read())
	TRIGP2chk = Db(open(file2, 'rb').read())
	TRIGP3chk = Db(open(file3, 'rb').read())
	TRIGP4chk = Db(open(file4, 'rb').read())
	TRIGP5chk = Db(open(file5, 'rb').read())
	TRIGP6chk = Db(open(file6, 'rb').read())
	TRIGP7chk = Db(open(file7, 'rb').read())
	TRIGP8chk = Db(open(file8, 'rb').read())
	TRIGP1chkEPD = EUDVariable()
	TRIGP2chkEPD = EUDVariable()
	TRIGP3chkEPD = EUDVariable()
	TRIGP4chkEPD = EUDVariable()
	TRIGP5chkEPD = EUDVariable()
	TRIGP6chkEPD = EUDVariable()
	TRIGP7chkEPD = EUDVariable()
	TRIGP8chkEPD = EUDVariable()
	TRIGP1chkEPD << TRIGP1chk//4
	TRIGP2chkEPD << TRIGP2chk//4
	TRIGP3chkEPD << TRIGP3chk//4
	TRIGP4chkEPD << TRIGP4chk//4
	TRIGP5chkEPD << TRIGP5chk//4
	TRIGP6chkEPD << TRIGP6chk//4
	TRIGP7chkEPD << TRIGP7chk//4
	TRIGP8chkEPD << TRIGP8chk//4

	P1START = EUDVariable()
	P2START = EUDVariable()
	P3START = EUDVariable()
	P4START = EUDVariable()
	P5START = EUDVariable()
	P6START = EUDVariable()
	P7START = EUDVariable()
	P8START = EUDVariable()
	P1STARTEPD = EUDVariable()
	P2STARTEPD = EUDVariable()
	P3STARTEPD = EUDVariable()
	P4STARTEPD = EUDVariable()
	P5STARTEPD = EUDVariable()
	P6STARTEPD = EUDVariable()
	P7STARTEPD = EUDVariable()
	P8STARTEPD = EUDVariable()
	P1END = EUDVariable()
	P2END = EUDVariable()
	P3END = EUDVariable()
	P4END = EUDVariable()
	P5END = EUDVariable()
	P6END = EUDVariable()
	P7END = EUDVariable()
	P8END = EUDVariable()
	P1ENDEPD = EUDVariable()
	P2ENDEPD = EUDVariable()
	P3ENDEPD = EUDVariable()
	P4ENDEPD = EUDVariable()
	P5ENDEPD = EUDVariable()
	P6ENDEPD = EUDVariable()
	P7ENDEPD = EUDVariable()
	P8ENDEPD = EUDVariable()

	global Prohibited_Label 
	Prohibited_Label = 0xFFE0
	CtrigLoop = EUDVariable()
	CurrentTrig_0 = EUDVariable()
	CurrentTrig_0EPD = EUDVariable()
	CurrentTrig_0Index = EUDVariable()
	CurrentTrig_0Next = EUDVariable()
	ptr_0 = EUDVariable()
	ptrloopend_0 = EUDVariable()
	CurrentTrig_0EPD5 = EUDVariable()

	# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
	if EUDWhile()((CtrigLoop <= 7)): 

		if EUDIf()((f_playerexist(0) == 0,f_playerexist(1) == 1,CtrigLoop == 0)): # Remove Error
			CtrigLoop << 1
		EUDEndIf()

		if EUDIf()((f_playerexist(0) == 0,f_playerexist(1) == 0,f_playerexist(2) == 1,CtrigLoop == 0)): # Remove Error
			CtrigLoop << 2
		EUDEndIf()

		if EUDIf()((f_playerexist(0) == 0,f_playerexist(1) == 0,f_playerexist(2) == 0,f_playerexist(3) == 1,CtrigLoop == 0)): # Remove Error
			CtrigLoop << 3
		EUDEndIf()

		if EUDIf()((f_playerexist(0) == 0,f_playerexist(1) == 0,f_playerexist(2) == 0,f_playerexist(3) == 0,f_playerexist(4) == 1,CtrigLoop == 0)): # Remove Error
			CtrigLoop << 4
		EUDEndIf()

		if EUDIf()((f_playerexist(0) == 0,f_playerexist(1) == 0,f_playerexist(2) == 0,f_playerexist(3) == 0,f_playerexist(4) == 0,f_playerexist(5) == 1,CtrigLoop == 0)): # Remove Error
			CtrigLoop << 5
		EUDEndIf()

		if EUDIf()((f_playerexist(0) == 0,f_playerexist(1) == 0,f_playerexist(2) == 0,f_playerexist(3) == 0,f_playerexist(4) == 0,f_playerexist(5) == 0,f_playerexist(6) == 1,CtrigLoop == 0)): # Remove Error
			CtrigLoop << 6
		EUDEndIf()

		if EUDIf()((f_playerexist(0) == 0,f_playerexist(1) == 0,f_playerexist(2) == 0,f_playerexist(3) == 0,f_playerexist(4) == 0,f_playerexist(5) == 0,f_playerexist(6) == 0,f_playerexist(7) == 1,CtrigLoop == 0)): # Remove Error
			CtrigLoop << 7
		EUDEndIf()

		CurrentTrig_0 << f_maskread_epd(EPD(0x51A280 + 0x8 + 0xC * CtrigLoop), 0xFFFFFFFF)

		if EUDWhile()((CurrentTrig_0Index != 0xFFFF)): # 0st Loop -- Load TRIG Section

			DoActions(ptr_0.AddNumber(1))

			if EUDIf()((ptr_0 <= 3)): # Check Label
				CurrentTrig_0 << f_maskread_epd(EPD(CurrentTrig_0 + 0x4),0xFFFFFFFF)
				CurrentTrig_0EPD << EPD(CurrentTrig_0)
			if EUDElse()():
				DoActions([CurrentTrig_0.AddNumber(0x970),CurrentTrig_0EPD.AddNumber(0x970//4)])
			EUDEndIf()

			CurrentTrig_0EPD5 << CurrentTrig_0EPD+5

			if EUDIf()((CtrigLoop == 0,DeathsX(CurrentTrig_0EPD5,Exactly,0xFD*16777216,0,0xFF000000))): # Check Label
				P1START << CurrentTrig_0
				P1STARTEPD << CurrentTrig_0EPD
				DoActions([SetDeaths(P1STARTEPD,SetTo,0,0)])
			EUDEndIf()
			if EUDIf()((CtrigLoop == 0,DeathsX(CurrentTrig_0EPD5,Exactly,0xFC*16777216,0,0xFF000000))): # Check Label
				P1END << CurrentTrig_0
				P1ENDEPD << CurrentTrig_0EPD
				CurrentTrig_0Index << 0xFFFF
				DoActions([SetDeaths(P1ENDEPD,SetTo,0,0)])
			EUDEndIf()
			if EUDIf()((CtrigLoop == 1,DeathsX(CurrentTrig_0EPD5,Exactly,0xFD*16777216,0,0xFF000000))): # Check Label
				P2START << CurrentTrig_0
				P2STARTEPD << CurrentTrig_0EPD
				DoActions([SetDeaths(P2STARTEPD,SetTo,0,0)])
			EUDEndIf()
			if EUDIf()((CtrigLoop == 1,DeathsX(CurrentTrig_0EPD5,Exactly,0xFC*16777216,0,0xFF000000))): # Check Label
				P2END << CurrentTrig_0
				P2ENDEPD << CurrentTrig_0EPD
				CurrentTrig_0Index << 0xFFFF
				DoActions([SetDeaths(P2ENDEPD,SetTo,0,0)])
			EUDEndIf()
			if EUDIf()((CtrigLoop == 2,DeathsX(CurrentTrig_0EPD5,Exactly,0xFD*16777216,0,0xFF000000))): # Check Label
				P3START << CurrentTrig_0
				P3STARTEPD << CurrentTrig_0EPD
				DoActions([SetDeaths(P3STARTEPD,SetTo,0,0)])
			EUDEndIf()
			if EUDIf()((CtrigLoop == 2,DeathsX(CurrentTrig_0EPD5,Exactly,0xFC*16777216,0,0xFF000000))): # Check Label
				P3END << CurrentTrig_0
				P3ENDEPD << CurrentTrig_0EPD
				CurrentTrig_0Index << 0xFFFF
				DoActions([SetDeaths(P3ENDEPD,SetTo,0,0)])
			EUDEndIf()
			if EUDIf()((CtrigLoop == 3,DeathsX(CurrentTrig_0EPD5,Exactly,0xFD*16777216,0,0xFF000000))): # Check Label
				P4START << CurrentTrig_0
				P4STARTEPD << CurrentTrig_0EPD
				DoActions([SetDeaths(P4STARTEPD,SetTo,0,0)])
			EUDEndIf()
			if EUDIf()((CtrigLoop == 3,DeathsX(CurrentTrig_0EPD5,Exactly,0xFC*16777216,0,0xFF000000))): # Check Label
				P4END << CurrentTrig_0
				P4ENDEPD << CurrentTrig_0EPD
				CurrentTrig_0Index << 0xFFFF
				DoActions([SetDeaths(P4ENDEPD,SetTo,0,0)])
			EUDEndIf()
			if EUDIf()((CtrigLoop == 4,DeathsX(CurrentTrig_0EPD5,Exactly,0xFD*16777216,0,0xFF000000))): # Check Label
				P5START << CurrentTrig_0
				P5STARTEPD << CurrentTrig_0EPD
				DoActions([SetDeaths(P5STARTEPD,SetTo,0,0)])
			EUDEndIf()
			if EUDIf()((CtrigLoop == 4,DeathsX(CurrentTrig_0EPD5,Exactly,0xFC*16777216,0,0xFF000000))): # Check Label
				P5END << CurrentTrig_0
				P5ENDEPD << CurrentTrig_0EPD
				CurrentTrig_0Index << 0xFFFF
				DoActions([SetDeaths(P5ENDEPD,SetTo,0,0)])
			EUDEndIf()
			if EUDIf()((CtrigLoop == 5,DeathsX(CurrentTrig_0EPD5,Exactly,0xFD*16777216,0,0xFF000000))): # Check Label
				P6START << CurrentTrig_0
				P6STARTEPD << CurrentTrig_0EPD
				DoActions([SetDeaths(P6STARTEPD,SetTo,0,0)])
			EUDEndIf()
			if EUDIf()((CtrigLoop == 5,DeathsX(CurrentTrig_0EPD5,Exactly,0xFC*16777216,0,0xFF000000))): # Check Label
				P6END << CurrentTrig_0
				P6ENDEPD << CurrentTrig_0EPD
				CurrentTrig_0Index << 0xFFFF
				DoActions([SetDeaths(P6ENDEPD,SetTo,0,0)])
			EUDEndIf()
			if EUDIf()((CtrigLoop == 6,DeathsX(CurrentTrig_0EPD5,Exactly,0xFD*16777216,0,0xFF000000))): # Check Label
				P7START << CurrentTrig_0
				P7STARTEPD << CurrentTrig_0EPD
				DoActions([SetDeaths(P7STARTEPD,SetTo,0,0)])
			EUDEndIf()
			if EUDIf()((CtrigLoop == 6,DeathsX(CurrentTrig_0EPD5,Exactly,0xFC*16777216,0,0xFF000000))): # Check Label
				P7END << CurrentTrig_0
				P7ENDEPD << CurrentTrig_0EPD
				CurrentTrig_0Index << 0xFFFF
				DoActions([SetDeaths(P7ENDEPD,SetTo,0,0)])
			EUDEndIf()
			if EUDIf()((CtrigLoop == 7,DeathsX(CurrentTrig_0EPD5,Exactly,0xFD*16777216,0,0xFF000000))): # Check Label
				P8START << CurrentTrig_0
				P8STARTEPD << CurrentTrig_0EPD
				DoActions([SetDeaths(P8STARTEPD,SetTo,0,0)])
			EUDEndIf()
			if EUDIf()((CtrigLoop == 7,DeathsX(CurrentTrig_0EPD5,Exactly,0xFC*16777216,0,0xFF000000))): # Check Label
				P8END << CurrentTrig_0
				P8ENDEPD << CurrentTrig_0EPD
				CurrentTrig_0Index << 0xFFFF
				DoActions([SetDeaths(P8ENDEPD,SetTo,0,0)])
			EUDEndIf()

		EUDEndWhile()

		CtrigLoop << CtrigLoop + 1
		ptr_0 << 0
		ptrloopend_0 << 0
		CurrentTrig_0Index << 0

		if EUDIf()((f_playerexist(1) == 0,CtrigLoop == 1)): # Remove Error
			CtrigLoop << 2
		EUDEndIf()

		if EUDIf()((f_playerexist(2) == 0,CtrigLoop == 2)): # Remove Error
			CtrigLoop << 3
		EUDEndIf()

		if EUDIf()((f_playerexist(3) == 0,CtrigLoop == 3)): # Remove Error
			CtrigLoop << 4
		EUDEndIf()

		if EUDIf()((f_playerexist(4) == 0,CtrigLoop == 4)): # Remove Error
			CtrigLoop << 5
		EUDEndIf()

		if EUDIf()((f_playerexist(5) == 0,CtrigLoop == 5)): # Remove Error
			CtrigLoop << 6
		EUDEndIf()

		if EUDIf()((f_playerexist(6) == 0,CtrigLoop == 6)): # Remove Error
			CtrigLoop << 7
		EUDEndIf()

		if EUDIf()((f_playerexist(7) == 0,CtrigLoop == 7)): # Remove Error
			CtrigLoop << 8
		EUDEndIf()

	EUDEndWhile() 

	CtrigLoop << 0
	# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

	Count = EUDVariable()
	CurEPD = EUDVariable()
	Temp = EUDVariable()

	PrevCp = EUDVariable()
	PrevCp << f_getcurpl()

	SizePX = [SizeP1,SizeP2,SizeP3,SizeP4,SizeP5,SizeP6,SizeP7,SizeP8]
	TRIGPXchk = [TRIGP1chk,TRIGP2chk,TRIGP3chk,TRIGP4chk,TRIGP5chk,TRIGP6chk,TRIGP7chk,TRIGP8chk]
	file_sizeX = [file_size1//0x970,file_size2//0x970,file_size3//0x970,file_size4//0x970,file_size5//0x970,file_size6//0x970,file_size7//0x970,file_size8//0x970]
	Call0OX = [Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()]
	Call1PX = [[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()]]
	Call2PX = [[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()]]
	Call3PX = [[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()]]
	Call4PX = [[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()]]
	Call5PX = [[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()]]
	Call6PX = [[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()]]
	Call7PX = [[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()]]
	Call8PX = [[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()],[Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()]]
	CondEND = [Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()]
	ActEND = [Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()]
	StartIndex1 = [Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()]
	StartIndex2 = [Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward(),Forward()]

	DoActions([
		SetMemory(Call0OX[0]+0x15C,SetTo,TRIGP1chk),
		SetMemory(Call0OX[1]+0x15C,SetTo,TRIGP2chk),
		SetMemory(Call0OX[2]+0x15C,SetTo,TRIGP3chk),
		SetMemory(Call0OX[3]+0x15C,SetTo,TRIGP4chk),
		SetMemory(Call0OX[4]+0x15C,SetTo,TRIGP5chk),
		SetMemory(Call0OX[5]+0x15C,SetTo,TRIGP6chk),
		SetMemory(Call0OX[6]+0x15C,SetTo,TRIGP7chk),
		SetMemory(Call0OX[7]+0x15C,SetTo,TRIGP8chk),

		SetMemory(Call1PX[0][0]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[0][1]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[0][2]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[0][3]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[0][4]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[0][5]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[0][6]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[0][7]+0x19C,SetTo,TRIGP1chkEPD),

		SetMemory(Call2PX[0][0]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[0][1]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[0][2]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[0][3]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[0][4]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[0][5]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[0][6]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[0][7]+0x19C,SetTo,TRIGP2chkEPD),

		SetMemory(Call3PX[0][0]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[0][1]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[0][2]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[0][3]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[0][4]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[0][5]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[0][6]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[0][7]+0x19C,SetTo,TRIGP3chkEPD),

		SetMemory(Call4PX[0][0]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[0][1]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[0][2]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[0][3]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[0][4]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[0][5]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[0][6]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[0][7]+0x19C,SetTo,TRIGP4chkEPD),

		SetMemory(Call5PX[0][0]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[0][1]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[0][2]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[0][3]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[0][4]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[0][5]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[0][6]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[0][7]+0x19C,SetTo,TRIGP5chkEPD),

		SetMemory(Call6PX[0][0]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[0][1]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[0][2]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[0][3]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[0][4]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[0][5]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[0][6]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[0][7]+0x19C,SetTo,TRIGP6chkEPD),

		SetMemory(Call7PX[0][0]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[0][1]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[0][2]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[0][3]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[0][4]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[0][5]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[0][6]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[0][7]+0x19C,SetTo,TRIGP7chkEPD),

		SetMemory(Call8PX[0][0]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[0][1]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[0][2]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[0][3]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[0][4]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[0][5]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[0][6]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[0][7]+0x19C,SetTo,TRIGP8chkEPD),

		SetMemory(Call1PX[1][0]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[1][1]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[1][2]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[1][3]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[1][4]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[1][5]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[1][6]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[1][7]+0x19C,SetTo,TRIGP1chkEPD),

		SetMemory(Call2PX[1][0]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[1][1]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[1][2]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[1][3]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[1][4]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[1][5]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[1][6]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[1][7]+0x19C,SetTo,TRIGP2chkEPD),

		SetMemory(Call3PX[1][0]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[1][1]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[1][2]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[1][3]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[1][4]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[1][5]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[1][6]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[1][7]+0x19C,SetTo,TRIGP3chkEPD),

		SetMemory(Call4PX[1][0]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[1][1]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[1][2]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[1][3]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[1][4]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[1][5]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[1][6]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[1][7]+0x19C,SetTo,TRIGP4chkEPD),

		SetMemory(Call5PX[1][0]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[1][1]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[1][2]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[1][3]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[1][4]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[1][5]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[1][6]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[1][7]+0x19C,SetTo,TRIGP5chkEPD),

		SetMemory(Call6PX[1][0]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[1][1]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[1][2]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[1][3]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[1][4]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[1][5]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[1][6]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[1][7]+0x19C,SetTo,TRIGP6chkEPD),

		SetMemory(Call7PX[1][0]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[1][1]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[1][2]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[1][3]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[1][4]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[1][5]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[1][6]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[1][7]+0x19C,SetTo,TRIGP7chkEPD),

		SetMemory(Call8PX[1][0]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[1][1]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[1][2]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[1][3]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[1][4]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[1][5]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[1][6]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[1][7]+0x19C,SetTo,TRIGP8chkEPD),

		SetMemory(Call1PX[2][0]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[2][1]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[2][2]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[2][3]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[2][4]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[2][5]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[2][6]+0x19C,SetTo,TRIGP1chkEPD),
		SetMemory(Call1PX[2][7]+0x19C,SetTo,TRIGP1chkEPD),

		SetMemory(Call2PX[2][0]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[2][1]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[2][2]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[2][3]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[2][4]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[2][5]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[2][6]+0x19C,SetTo,TRIGP2chkEPD),
		SetMemory(Call2PX[2][7]+0x19C,SetTo,TRIGP2chkEPD),

		SetMemory(Call3PX[2][0]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[2][1]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[2][2]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[2][3]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[2][4]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[2][5]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[2][6]+0x19C,SetTo,TRIGP3chkEPD),
		SetMemory(Call3PX[2][7]+0x19C,SetTo,TRIGP3chkEPD),

		SetMemory(Call4PX[2][0]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[2][1]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[2][2]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[2][3]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[2][4]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[2][5]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[2][6]+0x19C,SetTo,TRIGP4chkEPD),
		SetMemory(Call4PX[2][7]+0x19C,SetTo,TRIGP4chkEPD),

		SetMemory(Call5PX[2][0]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[2][1]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[2][2]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[2][3]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[2][4]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[2][5]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[2][6]+0x19C,SetTo,TRIGP5chkEPD),
		SetMemory(Call5PX[2][7]+0x19C,SetTo,TRIGP5chkEPD),

		SetMemory(Call6PX[2][0]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[2][1]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[2][2]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[2][3]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[2][4]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[2][5]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[2][6]+0x19C,SetTo,TRIGP6chkEPD),
		SetMemory(Call6PX[2][7]+0x19C,SetTo,TRIGP6chkEPD),

		SetMemory(Call7PX[2][0]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[2][1]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[2][2]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[2][3]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[2][4]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[2][5]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[2][6]+0x19C,SetTo,TRIGP7chkEPD),
		SetMemory(Call7PX[2][7]+0x19C,SetTo,TRIGP7chkEPD),

		SetMemory(Call8PX[2][0]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[2][1]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[2][2]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[2][3]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[2][4]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[2][5]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[2][6]+0x19C,SetTo,TRIGP8chkEPD),
		SetMemory(Call8PX[2][7]+0x19C,SetTo,TRIGP8chkEPD),

		SetMemory(Call1PX[3][0]+0x19C,SetTo,TRIGP1chk),
		SetMemory(Call1PX[3][1]+0x19C,SetTo,TRIGP1chk),
		SetMemory(Call1PX[3][2]+0x19C,SetTo,TRIGP1chk),
		SetMemory(Call1PX[3][3]+0x19C,SetTo,TRIGP1chk),
		SetMemory(Call1PX[3][4]+0x19C,SetTo,TRIGP1chk),
		SetMemory(Call1PX[3][5]+0x19C,SetTo,TRIGP1chk),
		SetMemory(Call1PX[3][6]+0x19C,SetTo,TRIGP1chk),
		SetMemory(Call1PX[3][7]+0x19C,SetTo,TRIGP1chk),

		SetMemory(Call2PX[3][0]+0x19C,SetTo,TRIGP2chk),
		SetMemory(Call2PX[3][1]+0x19C,SetTo,TRIGP2chk),
		SetMemory(Call2PX[3][2]+0x19C,SetTo,TRIGP2chk),
		SetMemory(Call2PX[3][3]+0x19C,SetTo,TRIGP2chk),
		SetMemory(Call2PX[3][4]+0x19C,SetTo,TRIGP2chk),
		SetMemory(Call2PX[3][5]+0x19C,SetTo,TRIGP2chk),
		SetMemory(Call2PX[3][6]+0x19C,SetTo,TRIGP2chk),
		SetMemory(Call2PX[3][7]+0x19C,SetTo,TRIGP2chk),

		SetMemory(Call3PX[3][0]+0x19C,SetTo,TRIGP3chk),
		SetMemory(Call3PX[3][1]+0x19C,SetTo,TRIGP3chk),
		SetMemory(Call3PX[3][2]+0x19C,SetTo,TRIGP3chk),
		SetMemory(Call3PX[3][3]+0x19C,SetTo,TRIGP3chk),
		SetMemory(Call3PX[3][4]+0x19C,SetTo,TRIGP3chk),
		SetMemory(Call3PX[3][5]+0x19C,SetTo,TRIGP3chk),
		SetMemory(Call3PX[3][6]+0x19C,SetTo,TRIGP3chk),
		SetMemory(Call3PX[3][7]+0x19C,SetTo,TRIGP3chk),

		SetMemory(Call4PX[3][0]+0x19C,SetTo,TRIGP4chk),
		SetMemory(Call4PX[3][1]+0x19C,SetTo,TRIGP4chk),
		SetMemory(Call4PX[3][2]+0x19C,SetTo,TRIGP4chk),
		SetMemory(Call4PX[3][3]+0x19C,SetTo,TRIGP4chk),
		SetMemory(Call4PX[3][4]+0x19C,SetTo,TRIGP4chk),
		SetMemory(Call4PX[3][5]+0x19C,SetTo,TRIGP4chk),
		SetMemory(Call4PX[3][6]+0x19C,SetTo,TRIGP4chk),
		SetMemory(Call4PX[3][7]+0x19C,SetTo,TRIGP4chk),

		SetMemory(Call5PX[3][0]+0x19C,SetTo,TRIGP5chk),
		SetMemory(Call5PX[3][1]+0x19C,SetTo,TRIGP5chk),
		SetMemory(Call5PX[3][2]+0x19C,SetTo,TRIGP5chk),
		SetMemory(Call5PX[3][3]+0x19C,SetTo,TRIGP5chk),
		SetMemory(Call5PX[3][4]+0x19C,SetTo,TRIGP5chk),
		SetMemory(Call5PX[3][5]+0x19C,SetTo,TRIGP5chk),
		SetMemory(Call5PX[3][6]+0x19C,SetTo,TRIGP5chk),
		SetMemory(Call5PX[3][7]+0x19C,SetTo,TRIGP5chk),

		SetMemory(Call6PX[3][0]+0x19C,SetTo,TRIGP6chk),
		SetMemory(Call6PX[3][1]+0x19C,SetTo,TRIGP6chk),
		SetMemory(Call6PX[3][2]+0x19C,SetTo,TRIGP6chk),
		SetMemory(Call6PX[3][3]+0x19C,SetTo,TRIGP6chk),
		SetMemory(Call6PX[3][4]+0x19C,SetTo,TRIGP6chk),
		SetMemory(Call6PX[3][5]+0x19C,SetTo,TRIGP6chk),
		SetMemory(Call6PX[3][6]+0x19C,SetTo,TRIGP6chk),
		SetMemory(Call6PX[3][7]+0x19C,SetTo,TRIGP6chk),

		SetMemory(Call7PX[3][0]+0x19C,SetTo,TRIGP7chk),
		SetMemory(Call7PX[3][1]+0x19C,SetTo,TRIGP7chk),
		SetMemory(Call7PX[3][2]+0x19C,SetTo,TRIGP7chk),
		SetMemory(Call7PX[3][3]+0x19C,SetTo,TRIGP7chk),
		SetMemory(Call7PX[3][4]+0x19C,SetTo,TRIGP7chk),
		SetMemory(Call7PX[3][5]+0x19C,SetTo,TRIGP7chk),
		SetMemory(Call7PX[3][6]+0x19C,SetTo,TRIGP7chk),
		SetMemory(Call7PX[3][7]+0x19C,SetTo,TRIGP7chk),

		SetMemory(Call8PX[3][0]+0x19C,SetTo,TRIGP8chk),
		SetMemory(Call8PX[3][1]+0x19C,SetTo,TRIGP8chk),
		SetMemory(Call8PX[3][2]+0x19C,SetTo,TRIGP8chk),
		SetMemory(Call8PX[3][3]+0x19C,SetTo,TRIGP8chk),
		SetMemory(Call8PX[3][4]+0x19C,SetTo,TRIGP8chk),
		SetMemory(Call8PX[3][5]+0x19C,SetTo,TRIGP8chk),
		SetMemory(Call8PX[3][6]+0x19C,SetTo,TRIGP8chk),
		SetMemory(Call8PX[3][7]+0x19C,SetTo,TRIGP8chk),
	])

	for i in range (0,8):
		if EUDIf()((SizePX[i] > 0)):
			Count << 1
			CurEPD << EPD(TRIGPXchk[i])
			f_setcurpl(CurEPD+1)

			if EUDWhile()((Count <= file_sizeX[i])): 

				Call0OX[i] << RawTrigger(actions=[SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,4)]) # Connect Next

				if EUDIf()((DeathsX(CurrentPlayer,Exactly,0xFE000000,0,0xFF000000))): # Check Label
					StartIndex1[i] << RawTrigger(actions=[SetMemory(0x6509B0,Add,5)])

					RawTrigger(actions=[SetMemory(0x6509B0,Add,-6)])
					if EUDIf()((Deaths(CurrentPlayer,Exactly,0xFFFB,0))):
						RawTrigger(actions=[SetMemory(0x6509B0,Add,8)])
						Trigger(conditions=[Deaths(CurrentPlayer,Exactly,i,0)],actions=[NSQCASM.SetNumber(CurEPD+87-604*7),SetDeaths(EPD(StartIndex1[i])+1,SetTo,StartIndex2[i],0),SetMemory(0x6509B0,Subtract,8)])
					EUDEndIf()
					RawTrigger(actions=[SetMemory(0x6509B0,Add,6)]) 
					StartIndex2[i] << NextTrigger()
					
					if EUDLoopN()(15):
						if EUDIf()((DeathsX(CurrentPlayer,Exactly,0xF0000000,0,0xF0000000))): # Check Label
							Call1PX[0][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x01000000,0,0x0F000000)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0F000000,0,0xFF000000),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call2PX[0][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x02000000,0,0x0F000000)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0F000000,0,0xFF000000),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call3PX[0][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x03000000,0,0x0F000000)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0F000000,0,0xFF000000),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call4PX[0][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x04000000,0,0x0F000000)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0F000000,0,0xFF000000),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call5PX[0][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x05000000,0,0x0F000000)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0F000000,0,0xFF000000),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call6PX[0][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x06000000,0,0x0F000000)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0F000000,0,0xFF000000),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call7PX[0][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x07000000,0,0x0F000000)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0F000000,0,0xFF000000),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call8PX[0][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x08000000,0,0x0F000000)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0F000000,0,0xFF000000),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
						if EUDElseIf()((DeathsX(CurrentPlayer,Exactly,0x00000000,0,0xFF000000))):
							EUDJump(CondEND[i])
						EUDEndIf()
						RawTrigger(actions=[SetMemory(0x6509B0,Add,5)])
					EUDEndLoopN()
					CondEND[i] << NextTrigger()
					f_setcurpl(CurEPD+88)

					if EUDLoopN()(64):
						if EUDIf()((DeathsX(CurrentPlayer,Exactly,0xF00000,0,0xF00000))): # EPD
							Call1PX[1][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x010000,0,0x0F0000)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x2D0000,0,0xFF0000),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call2PX[1][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x020000,0,0x0F0000)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x2D0000,0,0xFF0000),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call3PX[1][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x030000,0,0x0F0000)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x2D0000,0,0xFF0000),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call4PX[1][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x040000,0,0x0F0000)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x2D0000,0,0xFF0000),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call5PX[1][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x050000,0,0x0F0000)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x2D0000,0,0xFF0000),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call6PX[1][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x060000,0,0x0F0000)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x2D0000,0,0xFF0000),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call7PX[1][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x070000,0,0x0F0000)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x2D0000,0,0xFF0000),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call8PX[1][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x080000,0,0x0F0000)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x2D0000,0,0xFF0000),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
						EUDEndIf()
						
						RawTrigger(actions=[SetMemory(0x6509B0,Add,1)])
						if EUDIf()((DeathsX(CurrentPlayer,Exactly,0xF000,0,0xF000))): # Value EPD
							Call1PX[2][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x0100,0,0x0F00)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0000,0,0xFF00),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call2PX[2][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x0200,0,0x0F00)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0000,0,0xFF00),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call3PX[2][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x0300,0,0x0F00)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0000,0,0xFF00),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call4PX[2][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x0400,0,0x0F00)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0000,0,0xFF00),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call5PX[2][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x0500,0,0x0F00)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0000,0,0xFF00),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call6PX[2][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x0600,0,0x0F00)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0000,0,0xFF00),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call7PX[2][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x0700,0,0x0F00)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0000,0,0xFF00),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call8PX[2][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x0800,0,0x0F00)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0000,0,0xFF00),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
						if EUDElseIf()((DeathsX(CurrentPlayer,Exactly,0xE000,0,0xF000))): #Value PTR
							Call1PX[3][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x0100,0,0x0F00)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0000,0,0xFF00),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call2PX[3][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x0200,0,0x0F00)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0000,0,0xFF00),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call3PX[3][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x0300,0,0x0F00)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0000,0,0xFF00),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call4PX[3][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x0400,0,0x0F00)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0000,0,0xFF00),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call5PX[3][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x0500,0,0x0F00)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0000,0,0xFF00),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call6PX[3][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x0600,0,0x0F00)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0000,0,0xFF00),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call7PX[3][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x0700,0,0x0F00)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0000,0,0xFF00),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
							Call8PX[3][i] << RawTrigger(conditions=[DeathsX(CurrentPlayer,Exactly,0x0800,0,0x0F00)],actions=[SetDeathsX(CurrentPlayer,SetTo,0x0000,0,0xFF00),SetMemory(0x6509B0,Subtract,2),SetDeaths(CurrentPlayer,Add,0,0),SetMemory(0x6509B0,Add,2)])
						EUDEndIf()
						RawTrigger(actions=[SetMemory(0x6509B0,Subtract,1)])

						EUDJumpIf([DeathsX(CurrentPlayer,Exactly,0x000000,0,0xFF0000)],ActEND[i])
						RawTrigger(actions=[SetMemory(0x6509B0,Add,8)])
					EUDEndLoopN()
					ActEND[i] << NextTrigger()
					f_setcurpl(CurEPD+5)
				EUDEndIf()
				
				RawTrigger(actions=[SetMemory(0x6509B0,Subtract,5)])
				if EUDIf()((Deaths(CurrentPlayer,AtLeast,1,0))): # Check Skip
					Temp << f_maskread_epdX(0xFFFFF)
					Count << Count + Temp
					Temp << Temp * 604
					DoActions([CurEPD.AddNumber(Temp),SetMemory(0x6509B0,Add,Temp)])
				EUDEndIf()

				RawTrigger(actions=[Count.AddNumber(1),CurEPD.AddNumber(604),SetMemory(0x6509B0,Add,605)])
			EUDEndWhile()
		EUDEndIf()

	if EUDIf()((f_playerexist(0) == 1,SizeP1 != 0)):
		DoActions([SetDeaths(P1STARTEPD+1,SetTo,TRIGP1chk,0),SetMemory(TRIGP1chk+(SizeP1-0x96C),SetTo,P1END)])
	EUDEndIf()
	if EUDIf()((f_playerexist(1) == 1,SizeP2 != 0)):
		DoActions([SetDeaths(P2STARTEPD+1,SetTo,TRIGP2chk,0),SetMemory(TRIGP2chk+(SizeP2-0x96C),SetTo,P2END)])
	EUDEndIf()
	if EUDIf()((f_playerexist(2) == 1,SizeP3 != 0)):
		DoActions([SetDeaths(P3STARTEPD+1,SetTo,TRIGP3chk,0),SetMemory(TRIGP3chk+(SizeP3-0x96C),SetTo,P3END)])
	EUDEndIf()
	if EUDIf()((f_playerexist(3) == 1,SizeP4 != 0)):
		DoActions([SetDeaths(P4STARTEPD+1,SetTo,TRIGP4chk,0),SetMemory(TRIGP4chk+(SizeP4-0x96C),SetTo,P4END)])
	EUDEndIf()
	if EUDIf()((f_playerexist(4) == 1,SizeP5 != 0)):
		DoActions([SetDeaths(P5STARTEPD+1,SetTo,TRIGP5chk,0),SetMemory(TRIGP5chk+(SizeP5-0x96C),SetTo,P5END)])
	EUDEndIf()
	if EUDIf()((f_playerexist(5) == 1,SizeP6 != 0)):
		DoActions([SetDeaths(P6STARTEPD+1,SetTo,TRIGP6chk,0),SetMemory(TRIGP6chk+(SizeP6-0x96C),SetTo,P6END)])
	EUDEndIf()
	if EUDIf()((f_playerexist(6) == 1,SizeP7 != 0)):
		DoActions([SetDeaths(P7STARTEPD+1,SetTo,TRIGP7chk,0),SetMemory(TRIGP7chk+(SizeP7-0x96C),SetTo,P7END)])
	EUDEndIf()
	if EUDIf()((f_playerexist(7) == 1,SizeP8 != 0)):
		DoActions([SetDeaths(P8STARTEPD+1,SetTo,TRIGP8chk,0),SetMemory(TRIGP8chk+(SizeP8-0x96C),SetTo,P8END)])
	EUDEndIf()

	f_setcurpl(PrevCp)
