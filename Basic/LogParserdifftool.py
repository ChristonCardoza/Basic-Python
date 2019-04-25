##############################################
##############################################
#####	Author:		Louis Kim			 #####
#####	EDITED:		Christon Cardoza	 #####
#####	CREATED:	03 September 2015	 #####
#####	UPDATED:	05 February 2019	 #####
##############################################
##############################################

import time, os, io, sys, re, itertools
import zipfile, difflib, urllib.request
import platform

def newcontentChanges(oldContent, newContent):
    seqm = difflib.SequenceMatcher(None, oldContent, newContent)
    output= []
    for opcode, a0, a1, b0, b1 in seqm.get_opcodes():
        if opcode == 'equal':
            output.append(seqm.a[a0:a1])
        elif opcode == 'insert':
            output.append("<span class=greenlight>" + seqm.b[b0:b1] + "</span>")
        elif opcode == 'delete':
            pass
            #output.append("<span class=redlight>" + seqm.a[a0:a1] + "</span>")
        elif opcode == 'replace':
            # seqm.a[a0:a1] -> seqm.b[b0:b1]
            output.append("<span class=greenlight>" + seqm.b[b0:b1] + "</span>")
        else:
            raise(RuntimeError, "unexpected opcode")
    return ''.join(output)
	
def oldcontentChanges(oldContent, newContent):
    seqm = difflib.SequenceMatcher(None, oldContent, newContent)
    output= []
    for opcode, a0, a1, b0, b1 in seqm.get_opcodes():
        if opcode == 'equal':
            output.append(seqm.a[a0:a1])
        elif opcode == 'insert':
            pass
            #output.append("<span class=greenlight>" + seqm.b[b0:b1] + "</span>")
        elif opcode == 'delete':
            output.append("<span class=redlight>" + seqm.a[a0:a1] + "</span>")
        elif opcode == 'replace':
            # seqm.a[a0:a1] -> seqm.b[b0:b1]
            output.append("<span class=redlight>" + seqm.a[a0:a1] + "</span>")
        else:
            raise(RuntimeError, "unexpected opcode")
    return ''.join(output)

def printTableSection(toPrint):
	if toPrint is True:
		global zeroUpdate
		zeroUpdate = False
		#report: print device section
		oldrevision = re.findall('<mappings.*?(revision="(.*?)")?>', oldXml, flags=re.DOTALL)
		newrevision = re.findall('<mappings.*?(revision="(.*?)")?>', newXml, flags=re.DOTALL)
		oldvrn = oldrevision[0][0]
		newvrn = newrevision[0][0]
		report.write("<br>\n<div class=\"info\">Old Revision:<span style=\"margin-left:5px;\">")
		report.write(oldvrn)
		report.write("</span>\n<br>\nNew Revision:<span style=\"margin-left:5px;\">")
		report.write(newvrn)
		report.write("</span>\n</div><br>\n")
		report.write("<div>\n<span style=\"margin-left: 40px;\"><b>table-map.xml</b></span>\n<br>\n<div class=\"layer1\">\n<span class=\"expand\"></span>")
		report.write("<span class=\"blue\">details</span>\n<br>\n<div class=\"layer2\">")
	return False

def printTagSection(name, toPrint):
	if toPrint is True:
		#report: print header or message section
		report.write(name)
		report.write(":\n<br>")
	return False

def determineUpdates(tagName, oldList, newList, oldConList, newConList, oldFncConList = '', newFncConList = ''):
	#determine the new headers, messages and table line
	tagNameToPrint = True
	setDiff = list(set(newList) - set(oldList))
	if setDiff:
		#report: print section if it has not been printed before
		if tagName is None:	#table-map
			tagNameToPrint = printTableSection(tagNameToPrint)
		else:	#msg.xml
			tagNameToPrint = printTagSection(tagName, tagNameToPrint)
		#report: print the new headers, messages and table line
		for i in setDiff:
			if tagName is None:	#table-map
				report.write("\nenvisionName=\"")
				report.write(i)
				report.write("\" \n<div class=\"layer3\">\n<span class=\"expand\"></span><span class=\"green\">new</span>\n<br>")
				report.write("\n<div class=\"layer4\">\n<span class=\"content\"><span class=\"green\">&#x2713;</span> &lt;")
				report.write(newConList[newList.index(i)])
				report.write("&gt;</span>\n</div></div><br>")
			elif tagName is "VALUEMAP":
				report.write("\n&emsp;name=\"")
				report.write(i)
				report.write("\" \n<div class=\"layer3\">\n<span class=\"expand\"></span><span class=\"green\">new</span>\n<br>")
				report.write("\n<div class=\"layer4\">\n<span class=\"content\"><span class=\"green\">&#x2713;</span> &nbspdefault=\"")
				report.write(newConList[newList.index(i)])
				report.write("<br><span class=\"green\">&#x2713;</span>&nbsp keyvaluepairs=")
				report.write(newFncConList[newList.index(i)])
				report.write("\"</span>\n</div></div>")
			elif tagName is "Messages":	#msg.xml
				report.write("\n&emsp;id1=\"")
				report.write(i)
				report.write("\" \n<div class=\"layer3\">\n<span class=\"expand\"></span><span class=\"green\">new</span>\n<br>")
				report.write("\n<div class=\"layer4\">\n<span class=\"content\">")
				if i in newFncConList and newFncConList[i] != '':
					report.write("<span class=\"green\">&#x2713;</span>&nbsp functions=")
					report.write(newFncConList[i])
					report.write("<br>")
				else:
					pass
				report.write("<span class=\"green\">&#x2713;</span>&nbsp content=\"")
				report.write(newConList[newList.index(i)])
				report.write("\"</span>\n</div></div>")
			else:
				report.write("\n&emsp;id1=\"")
				report.write(i)
				report.write("\" \n<div class=\"layer3\">\n<span class=\"expand\"></span><span class=\"green\">new</span>\n<br>")
				report.write("\n<div class=\"layer4\">\n<span class=\"content\"><span class=\"green\">&#x2713;</span> &nbspcontent=\"")
				report.write(newConList[newList.index(i)])
				report.write("\"</span>\n</div></div>")

	#determine the deleted headers, messages and table line
	setDiff = list(set(oldList) - set(newList))
	if setDiff:
		#report: print section if it has not been printed before
		if tagName is None:	#table-map
			tagNameToPrint = printTableSection(tagNameToPrint)
		else:	#msg.xml
			tagNameToPrint = printTagSection(tagName, tagNameToPrint)
		#report: print the deleted headers, messages and table line
		for i in setDiff:
			if tagName is None:	#table-map
				report.write("\nenvisionName=\"")
				report.write(i)
				report.write("\" \n<div class=\"layer3\">\n<span class=\"expand\"></span><span class=\"red\">deleted</span>\n<br>")
				report.write("\n<div class=\"layer4\">\n<span class=\"content\"><span class=\"red\">&#x2717;</span> &lt;")
				report.write(oldConList[oldList.index(i)])
				report.write("&gt;</span>\n</div></div>")
			elif tagName is "VALUEMAP":	#msg.xml
				report.write("\n&emsp;name=\"")
				report.write(i)
				report.write("\" \n<div class=\"layer3\">\n<span class=\"expand\"></span><span class=\"red\">deleted</span>\n<br>")
				report.write("\n<div class=\"layer4\">\n<span class=\"content\"><span class=\"red\">&#x2717;</span> &nbspdefault=\"")
				report.write(oldConList[oldList.index(i)])
				report.write("<br><span class=\"red\">&#x2717;</span>&nbsp keyvaluepairs=")
				report.write(oldFncConList[oldList.index(i)])
				report.write("\"</span>\n</div></div>")
			elif tagName is "Messages":
				report.write("\n&emsp;id1=\"")
				report.write(i)
				report.write("\" \n<div class=\"layer3\">\n<span class=\"expand\"></span><span class=\"red\">deleted</span><br>")
				report.write("\n<div class=\"layer4\">\n<span class=\"content\">")
				if i in oldFncConList and oldFncConList[i] != '':
					report.write("<span class=\"red\">&#x2717;</span>&nbsp functions=")
					report.write(oldFncConList[i])
					report.write("<br>")
				else:
					pass
				report.write("<span class=\"red\">&#x2717;</span>&nbsp content=\"")
				report.write(oldConList[oldList.index(i)])
				report.write("\"</span>\n</div></div>")
			else:
				report.write("\n&emsp;id1=\"")
				report.write(i)
				report.write("\" \n<div class=\"layer3\">\n<span class=\"expand\"></span><span class=\"red\">deleted</span>\n<br>")
				report.write("\n<div class=\"layer4\">\n<span class=\"content\"><span class=\"red\">&#x2717;</span> content=\"")
				report.write(oldConList[oldList.index(i)])
				report.write("\"</span>\n</div></div>")
	
	#determine the updated headers, messages and table line
	for i in newList:
		for j in oldList:
			if i==j:	#matched id
				if tagName is "VALUEMAP":
					defflag = False
					kvpflag = False
					olddefStr = oldConList[oldList.index(i)]
					newdefStr = newConList[newList.index(i)]
					oldkvpStr = oldFncConList[oldList.index(i)]
					newkvpStr = newFncConList[newList.index(i)]
					if olddefStr.replace(" ", "")==newdefStr.replace(" ", ""):  #content is the same
						pass
					else:
						defflag = True
					if oldkvpStr.replace(" ", "")==newkvpStr.replace(" ", ""): 
						pass
					else:
						kvpflag = True
					if not(defflag or kvpflag):
						break
					else:
						if defflag:
							newStr = newdefStr
							oldStr = olddefStr
							newdefStr = newcontentChanges(olddefStr, newdefStr)
							olddefStr = oldcontentChanges(olddefStr, newdefStr)
						if kvpflag:
							newStr = newkvpStr
							oldStr = oldkvpStr
							newkvpStr = newcontentChanges(oldkvpStr, newkvpStr)
							oldkvpStr = oldcontentChanges(oldkvpStr, newkvpStr)
						tagNameToPrint = printTagSection(tagName, tagNameToPrint)
						report.write("\n&emsp;name=\"")
						report.write(i)
						report.write("\" \n<div class=\"layer3\">\n<span class=\"expand\"></span><span class=\"green\">updated</span>\n<br>")
						report.write("\n<div class=\"layer4\">\n<span class=\"content\"><span class=\"green\">&#x2713;</span> &nbspdefault=\"")
						report.write(newdefStr)
						report.write("<br><span class=\"green\">&#x2713;</span>&nbsp keyvaluepairs=")
						report.write(newkvpStr)
						report.write("\"</span>\n<br><br>\n<span class=\"content\"><span class=\"red\">&#x2717;</span> ")
						report.write("default=\"")
						report.write(olddefStr)
						report.write("\"</span>\n<br>\n<span class=\"content\"><span class=\"red\">&#x2717;</span> ")
						report.write("keyvaluepairs=\"")
						report.write(oldkvpStr)
						report.write("\"</span>\n</div></div>")
				elif tagName is "Messages":
					conflag = False
					funflag = False
					oldContentStr = oldConList[oldList.index(i)]
					newContentStr = newConList[newList.index(i)]
					if i in oldFncConList:
						oldFncStr = oldFncConList[i]
					else:
						oldFncStr = ''
					if i in newFncConList:
						newFncStr = newFncConList[i]
					else:
						newFncStr = ''
					if oldContentStr.replace(" ", "")==newContentStr.replace(" ", ""): 
						pass
					else:
						conflag = True
					if oldFncStr.replace(" ", "")==newFncStr.replace(" ", ""):
						pass
					else:
						funflag = True
					if not(conflag or funflag):
						break
					else:
						if conflag:
							newStr = newContentStr
							oldStr = oldContentStr
							newContentStr = newcontentChanges(oldStr, newStr)
							oldContentStr = oldcontentChanges(oldStr, newStr)
						if funflag:
							newStr = newFncStr
							oldStr = oldFncStr
							newFncStr = newcontentChanges(oldStr, newStr)
							oldFncStr = oldcontentChanges(oldStr, newStr)
						tagNameToPrint = printTagSection(tagName, tagNameToPrint)
						report.write("\n&emsp;id1=\"")
						report.write(i)
						report.write("\" \n<div class=\"layer3\">\n<span class=\"expand\"></span><span class=\"green\">updated</span><br>")
						report.write("\n<div class=\"layer4\">\n<span class=\"content\">")
						if newFncStr != '':
							report.write("</span><span class=\"content\"><span class=\"green\">&#x2713;</span> ")
							report.write("functions=")
							report.write(newFncStr)
							report.write("<br>")
						else:
							pass
						#report.write("<span class=\"green\">&#x2713;</span>&nbsp functions=\"")
						#report.write(newFncStr)
						report.write("<span class=\"green\">&#x2713;</span>&nbsp content=\"")
						report.write(newContentStr)
						report.write("\"\n<br>")
						if oldFncStr != '':
							report.write("</span>\n<br>\n<span class=\"content\"><span class=\"red\">&#x2717;</span> ")
							report.write("functions=")
							report.write(oldFncStr)
							#report.write("\"")
						else:
							pass
						report.write("</span>\n<br>\n<span class=\"content\"><span class=\"red\">&#x2717;</span> ")
						report.write("content=\"")
						report.write(oldContentStr)
						report.write("\"</span>\n</div></div>")
				
				else:
					oldContentStr = oldConList[oldList.index(i)]
					newContentStr = newConList[newList.index(i)]
					if oldContentStr.replace(" ", "")==newContentStr.replace(" ", ""):  #content is the same
						break	#check the next id
					else:	#determine the changes in content
						newStr = newContentStr
						oldStr = oldContentStr
						newContentStr = newcontentChanges(oldStr, newStr)
						oldContentStr = oldcontentChanges(oldStr, newStr)
						#report: print section if it has not been printed before
						if tagName is None:	#table-map
							tagNameToPrint = printTableSection(tagNameToPrint)
						else:	#msg.xmls
							tagNameToPrint = printTagSection(tagName, tagNameToPrint)
						#report: print the updated headers, messages and table line
						report.write("\n&emsp;id1=\"")
						report.write(i)
						report.write("\" \n<div class=\"layer3\">\n<span class=\"expand\"></span><span class=\"green\">updated</span>\n<br>")
						report.write("\n<div class=\"layer4\">\n<span class=\"content\"><span class=\"green\">&#x2713;</span> content=\"")
						report.write(newContentStr)
						report.write("\"</span>\n<br><br>\n<span class=\"content\"><span class=\"red\">&#x2717;</span> ")
						report.write("content=\"")
						report.write(oldContentStr)
						report.write("\"</span>\n</div></div>")
	#report: close tags for table-map
	if tagName is None and tagNameToPrint is False:
		report.write("<br></div></div>\n<div><br></div>\n")

	if tagName and tagNameToPrint is True:	#no content changes
		return True
	else:
		return False

def fieldExtraction(oldXml, newXml, xmlPath):
	folder_path = os.path.dirname(xmlPath)
	path,folder_name = os.path.split(folder_path)
	oldChecksum = re.search('<VERSION.*?checksum="(.*?)"', oldXml, flags=re.DOTALL).group(1)
	newChecksum = re.search('<VERSION.*?checksum="(.*?)"', newXml, flags=re.DOTALL).group(1)

	if oldChecksum != newChecksum:
		global zeroUpdate, deviceCount
		zeroUpdate = False
		deviceCount+=1

		#regex expression declaration
		header_regex = '<HEADER.*?id1="(.*?)"'
		#message_regex = '<MESSAGE.*?id1="(.*?)"'
		hdrcontent_regex = '<HEADER.*?content="(.*?)"'
		#msgcontent_regex = '<MESSAGE.*?content="(.*?)"'
		version_regex1 = '<VERSION.*?xml="(.*?)"'
		version_regex2 = '<VERSION.*?revision="(.*?)"'
		#fnccontent_regex = '<MESSAGE.*?id1="(.*?)"(.*?)content="(.*?)"'
		valuemap_regex = '<VALUEMAP.*?name="(.*?)"'
		valuemapdef_regex = '<VALUEMAP.*?default="(.*?)"'
		valuemapKV_regex = '<VALUEMAP.*?keyvaluepairs="(.*?)"'

		#extract information from old xml
		oldHdrList = re.findall(header_regex, oldXml, flags=re.DOTALL)
		oldMsgList = re.findall(r'(?<!<!--)<MESSAGE.*?id1="(.*?)"', oldXml, flags=re.DOTALL)
		oldHdrConList = re.findall(hdrcontent_regex, oldXml, flags=re.DOTALL)
		oldMsgConList = re.findall(r'(?<!<!--)<MESSAGE.*?content="(.*?)"', oldXml, flags=re.DOTALL)
		oldVerList = re.findall(version_regex1, oldXml, flags=re.DOTALL)
		oldVerList = oldVerList + re.findall(version_regex2, oldXml, flags=re.DOTALL)
		oldFncCon = re.findall(r'(?<!<!--)<MESSAGE.*?id1="(.*?)"(.*?)content="(.*?)"', oldXml, flags=re.DOTALL)
		oldFncdict = [list(elem) for elem in oldFncCon]
		oldFunctionDict = {}
		for element in oldFncdict:
			oldelement = re.sub('\s+',' ', element[1])
			found = re.match('(.*?)(?:\((.*?)\))?functions=(.*)', oldelement, flags=re.DOTALL)
			if found:
				oldFunctionDict.update({element[0]:found.group(3)})
			else:
				oldFunctionDict.update({element[0]:''})
		oldVMList = re.findall(valuemap_regex, oldXml, flags=re.DOTALL)
		oldVMdefList = re.findall(valuemapdef_regex, oldXml, flags=re.DOTALL)
		oldVMKVList = re.findall(valuemapKV_regex, oldXml, flags=re.DOTALL)

		#extract information from new xml
		newHdrList = re.findall(header_regex, newXml, flags=re.DOTALL)
		newMsgList = re.findall(r'(?<!<!--)<MESSAGE.*?id1="(.*?)"', newXml, flags=re.DOTALL)
		newHdrConList = re.findall(hdrcontent_regex, newXml, flags=re.DOTALL)
		newMsgConList = re.findall(r'(?<!<!--)<MESSAGE.*?content="(.*?)"', newXml, flags=re.DOTALL)
		newVerList = re.findall(version_regex1, newXml, flags=re.DOTALL)
		newVerList = newVerList + re.findall(version_regex2, newXml, flags=re.DOTALL)
		newFncCon = re.findall(r'(?<!<!--)<MESSAGE.*?id1="(.*?)"(.*?)content="(.*?)"', newXml, flags=re.DOTALL)
		newFncdict = [list(elem) for elem in newFncCon]
		newFunctionDict = {}
		for element in newFncdict:
			newelement = re.sub('\s+',' ', element[1])
			found = re.match('(.*?)(?:\((.*?)\))?functions=(.*)', newelement, flags=re.DOTALL)
			if found:
				newFunctionDict.update({element[0]:found.group(3)})
			else:
				newFunctionDict.update({element[0]:''})
		newVMList = re.findall(valuemap_regex, newXml, flags=re.DOTALL)
		newVMdefList = re.findall(valuemapdef_regex, newXml, flags=re.DOTALL)
		newVMKVList = re.findall(valuemapKV_regex, newXml, flags=re.DOTALL)

		#report: print device section and version
		if deviceCount<10:
			report.write("<span style=\"margin-left:11px;\">")	#align single digit with double digit
			report.write(str(deviceCount))
			report.write("</span>.) <b>")
		else:
			report.write(str(deviceCount))
			report.write(".) <b>")
		if folder_name:
			report.write(folder_name)
		else:
			report.write(xmlPath)
		report.write("</b>\n<br>\n")
		if oldVerList:
			report.write("<span class=\"version\">Old Parser Version: ")
			report.write(oldVerList[0])
			report.write(", Old ESU: ")
			report.write(oldVerList[1])
			report.write("</span>\n<br>\n")
		report.write("<span class=\"version\">New Parser Version: ")
		report.write(newVerList[0])
		report.write(", New ESU: ")
		report.write(newVerList[1])
		report.write("</span>\n<br>\n<div class=\"layer1\">\n<span class=\"expand\"></span>")
		report.write("<span class=\"blue\">details</span>\n<br>\n<div class=\"layer2\">\n")

		#determine and print the changes in headers, messages
		if folder_name not in excludedDevices:	#update only devices that are not excluded
			noHeader = determineUpdates("Headers", oldHdrList, newHdrList, oldHdrConList, newHdrConList)
			noMessage = determineUpdates("Messages", oldMsgList, newMsgList, oldMsgConList, newMsgConList, oldFunctionDict, newFunctionDict)
			noValueMap = determineUpdates("VALUEMAP", oldVMList, newVMList, oldVMdefList, newVMdefList, oldVMKVList, newVMKVList)
			if noHeader and noMessage:	#there are no content changes in header or message
				report.write("<span class=\"info\">The changes made to this device are not content related.</span>\n<br>")
		else:
			report.write("<span class=\"info\">For this device, "
				"the changes made to the content are too numerous to display individually.</span>\n<br>")
		#report: close tags
		report.write("<br></div></div>\n<div><br></div>\n")
	#else:
	#	report.write("</span>\n<br>\nYou are editing the same file, please check the files <span style=\"margin-left:5px;\">")

def tableFieldExtraction(oldTable, newTable):
	oldNameList = re.findall('<mapping.*?envisionName="(.*?)"', oldTable)
	oldConList = re.findall('<(mapping.*?/)>', oldTable)
	newNameList = re.findall('<mapping.*?envisionName="(.*?)"', newTable)
	newConList = re.findall('<(mapping.*?/)>', newTable)
	determineUpdates(None, oldNameList, newNameList, oldConList, newConList)

def determinePath(path):
	for root, dirs, files in os.walk(path):	#walk through folder
		for i in files:
			if i.endswith(".envision"):
				return os.path.join(root, i)	#full path of the zip file
	return path

def compareXml(newXml, i, oldVersion):
	path = determinePath(oldVersion)	#determine if the input path is acceptable
	if path.endswith(".envision"):
		addDevice = True
		with zipfile.ZipFile(path) as zip:	#unpack the envision zip
			for j in zip.namelist():	#looping all the file paths within envision zip
				if j.endswith(".xml") and os.path.basename(i)==os.path.basename(j):	#found the same device in the previous build
					print(os.path.basename(j))
					addDevice = False
					oldXml = zip.read(j).decode('windows-1252')	#read file in zip as byte and decode to a string
					if j.endswith("table-map.xml"):
						tableFieldExtraction(oldXml, newXml)	#determine any changes
					else:
						fieldExtraction(oldXml, newXml, i)	#compare internal checksum and determine any changes
					break
			if addDevice is True:	#new device
				print(os.path.basename(i))
				fieldExtraction("<VERSION checksum=\"0\"", newXml, i)
	else:
		addDevice = True
		forLoop = True
		for root, dirs, files in os.walk(path):	#determine all the components within the folder
			for j in files:
				if j.endswith(".xml") and os.path.basename(i)==os.path.basename(j):	#found the same device in the previous build
					print(os.path.basename(i))
					addDevice = False
					forLoop = False
					if j.endswith("table-map.xml"):	#table-map.xml
						with open(os.path.join(root, j), "rb") as file:
							oldXml = file.read().decode('windows-1252')	#read file as byte and decode to a string
							tableFieldExtraction(oldXml, newXml)	#determine any changes
					else:	#msg.xml
						with open(os.path.join(root, j), "rb") as file:
							oldXml = file.read().decode('windows-1252')	#read file as byte and decode to a string
							fieldExtraction(oldXml, newXml, i)	#compare internal checksum and determine any changes
					break
			if forLoop is False:	#exit outer loop since device has been found
				break

		if addDevice is True and os.path.basename(i)!="table-map.xml":	#new device
			print(os.path.basename(i))
			fieldExtraction("<VERSION checksum=\"0\"", newXml, i)

##############################################
################### main() ###################
##############################################

try:

	start = time.time()
	print("Python Version:", sys.version)

	#global lists declaration
	diffReportList = []
	highlightOldList = []
	highlightNewList = []
	zeroUpdate = True
	deviceCount = 0
	outputName = "diffResult_" + time.strftime("%d%b%Y") + ".html"

	#determine if there should be excluded devices or not
	if sys.argv[len(sys.argv)-1]=="-all":
		excludedDevices = []
	else:
		excludedDevices = ['ciscoidsxml', 'dragonids', 'intrushield', 'iss', 'netscreenidp', 'snort', 'tippingpoint']

	if platform.system()=="Windows":
		pathDelimiter = "\\"
	else:
		pathDelimiter = "/"

	#use the folders indicated in arguments or download from the repository
	if len(sys.argv)>2:	#process the local inputs
		if os.path.exists(sys.argv[1]) and os.path.exists(sys.argv[2]):
			oldVersion = sys.argv[1]
			newVersion = sys.argv[2]
			print("\nOld Version:", oldVersion)
			print("New Version:", newVersion)
		else:
			sys.exit("\nTERMINATION REASON: Path Does Not Exist!")
	else:
		sys.exit("\nTERMINATION REASON: Provide the file path!")

	#report: create result.html file
	try:
		os.remove(outputName)	#delete existing file
	except OSError:
		pass
	with open(outputName, "w") as report:
		report.write("<html>\n<style type=\"text/css\">\nbody {\nfont-family: Verdana;\npadding: 0;\nmargin: 0; }\n\n"
			".info {\nfont-size: 12px;\nfont-style: italic; }\n\n.header {\nbackground-color: #197CB3;\npadding: 10px; }\n\n"
			".version {\ncolor: #808080;\nfont-size: 12px;\nmargin-left: 40px; }\n\n"
			".innerheader {\nmargin-left: 160px;\nmargin-right: 10px;\ntext-align: center;\ncolor: white;\nfont-size: 24px; }\n\n"
			".body {\nmargin-left: 20px; }\n\n.red {\ncolor: red;\nfont-style: italic;\ncursor:pointer;\nfont-size: 12px; }\n\n"
			".blue {\ncolor: blue;\nfont-style: italic;\ncursor:pointer;\nfont-size: 12px; }\n\n"
			".green {\ncolor: green;\nfont-style: italic;\ncursor:pointer;\nfont-size: 12px; }\n\n"
			".content {\nfont-size: 12px;}\n\n"
			".greenlight {\nbackground-color: #80C080 }\n\n.redlight {\nbackground-color: #FF8080 }\n\n"
			".crossline {\ntext-decoration: line-through; }\n\n.layer1 {\ndisplay: inline;\nmargin-left: 40px; }\n\n"
			".layer2 {\ndisplay: none; }\n\n.layer1.selected .layer2 {\ndisplay: block;\nmargin-left: 30px;\npadding: 10px; }\n\n"
			".layer3 {\ndisplay: inline; }\n\n.layer4 {\ndisplay: none; }\n\n"
			".layer3.selected .layer4 {\ndisplay: block;\nmargin-left: 20px;\nwhite-space: nowrap;\npadding: 9px; }\n\n"
			".layer1 > .expand:before,\n.layer3 > .expand:before {\ncontent: '\\025B8';\nfont-size: 12px;\nfont-weight: bold;"
			"\ncursor: pointer; }\n\n.layer1.selected > .expand:before,\n.layer3.selected > .expand:before {\ncontent: '\\025BE'; }"
			"\n</style>\n<body>\n<div class=\"header\"><div class=\"innerheader\">\nLog Parser Difference Report "
			"<span style=\"font-size:12px;color:black;\">v1.0</span>\n"
			"<span style=\"float:right;width:160px;\"><img src=\"data:image/jpeg;base64,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\"></span>\n</div></div><br>\n"
			"<div class=\"body\">\n<div class=\"info\">\nOld Version: <span style=\"margin-left:11px;\">")
		report.write(oldVersion)
		report.write("</span>\n<br>\nNew Version: <span style=\"margin-left:5px;\">")
		report.write(newVersion)
		report.write("</span>\n</div><br>\n")

	#determine file input format
	with open(outputName, "a") as report:
		if oldVersion.endswith(".xml") or newVersion.endswith(".xml"):	#xml inputs detected
			if oldVersion.endswith(".xml") and newVersion.endswith(".xml"):	#ensuring inputs are consistent
				print("Old version is ",oldVersion)
				print("New Version is ",newVersion)
				with open(oldVersion, "r") as file:
					oldXml = file.read()
				with open(newVersion, "r") as file:
					newXml = file.read()
				if bool(re.search('device\s*=\s*"2\.0"', oldXml)) and bool(re.search('device\s*=\s*"2\.0"', newXml)):	#device xml signature
					print(os.path.basename(newVersion))
					fieldExtraction(oldXml, newXml, os.path.basename(newVersion))
				elif bool(re.search('<mappings(\s)?(revision="\d")?>', oldXml)) and bool(re.search('<mappings(\s)?(revision="\d")?>', newXml)):	#table xml signature
					tableFieldExtraction(oldXml, newXml)
				else:
					sys.exit("\nTERMINATION REASON: The xml Content Format Is Incorrect!")
			else:
				sys.exit("\nTERMINATION REASON: Inputs Are Inconsistent!")
		else:	#proper directory expected
			path = determinePath(newVersion)	#determine if the input path is acceptable
			print("\nProcessing all the devices...")
			if path.endswith(".envision"):
				with zipfile.ZipFile(path) as zip:	#unpack the envision zip
					for i in zip.namelist():	#looping all the file paths within envision zip
						if i.endswith(".xml"):
							newXml = zip.read(i).decode('windows-1252')	#read file in zip as byte and decode to a string
							print(oldVersion)
							compareXml(newXml, i, oldVersion)	#look for the same xml in previous version
			else:	#etc\devices directory expected
				tablemapPath = False
				for root, dirs, files in os.walk(path):	#determine all the components within the folder
					for i in files:
						if i.endswith("table-map.xml"):	#ignore table-map first
							tablemapPath = os.path.join(root, i)
						elif i.endswith(".xml"):	#looping all the file within each directory
							with open(os.path.join(root, i), "rb") as file:
								newXml = file.read().decode('windows-1252')	#read file as byte and decode to a string
								compareXml(newXml, os.path.join(root, i), oldVersion)	#look for the same xml in previous version
							break	#there is only one xml file within each directory
				if tablemapPath:	#process table-map now
					with open(tablemapPath, "rb") as file:
						newXml = file.read().decode('windows-1252')	#read file as byte and decode to a string
						compareXml(newXml, tablemapPath, oldVersion)	#look for the same xml in previous version

		#report: empty report message
		if zeroUpdate is True:
			report.write("<span class=\"info\">\nThere are no changes found! If this should not be the case, "
				"ensure that the old and new device xml do not have the same checksum.</span>\n")

		#report: add javascript and append html closing tags
		report.write("</div>\n<script type=\"text/javascript\">\n"
			"var layer1 = document.getElementsByClassName(\"layer1\");\nfor(var i=0; i<layer1.length; i++)\n"
			"\tlayer1[i].addEventListener(\"click\", function(event){\n\t\tif(!this.classList.contains('selected')){\n"
			"\t\t\tfor(var j=0; j<layer1.length; j++) {\n\t\t\t\tlayer1[j].classList.remove(\"selected\");\n\t\t\t}\n\t\t}\n"
			"\t\tthis.classList.toggle(\"selected\");\n\t});\n"
			"var layer2 = document.getElementsByClassName(\"layer2\");\nfor(var i=0; i<layer2.length; i++)\n"
			"\tlayer2[i].addEventListener(\"click\", function(event){\n\t\tevent.stopPropagation();\n\t});\n"
			"var layer3 = document.getElementsByClassName(\"layer3\");\nfor(var i=0; i<layer3.length; i++)\n"
			"\tlayer3[i].addEventListener(\"click\", function(event){\n\t\tthis.classList.toggle(\"selected\");\n\t});\n"
			"var layer4 = document.getElementsByClassName(\"layer4\");\nfor(var i=0; i<layer4.length; i++)\n"
			"\tlayer4[i].addEventListener(\"click\", function(event){\n\t\tevent.stopPropagation();\n\t});\n"
			"</script>\n</body>\n</html>")

	#calculate the time taken to run script
	hrs, rem = divmod(time.time()-start, 3600)
	min, sec = divmod(rem, 60)
	if hrs!=0:
		print("\nCompleted! Time taken:", int(hrs), "hours", int(min), "minutes", round(sec), "seconds")
	elif min!=0:
		print("\nCompleted! Time taken:", int(min), "minutes", round(sec), "seconds")
	else:
		print("\nCompleted! Time taken:", sec, "seconds")

except KeyboardInterrupt:	#ctrl-c detection
	sys.exit("\nTERMINATION REASON: Program Stopped By The User.")