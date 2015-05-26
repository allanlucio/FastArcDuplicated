#coding:utf-8

import os
import pyPdf  

def getPDFContent(path):
    content = ""
    num_pages = 2
    p = file(path, "rb")
    pdf = pyPdf.PdfFileReader(p)
    
    content += pdf.getPage(2).extractText() + "\n"
    content = " ".join(content.replace(u"\xa0", " ").strip().split())     
    return content
    
    

def getListaArquivos(diretorio):
	lista=os.walk(diretorio)
	for root, dirs, files in lista:
		l1=files
	
	return l1
	

def getIndexPdf(diretorio):
	lista=getListaArquivos(diretorio)
	indices=[]
	erros=[]
	for b1 in lista:
		
		try:
			
			index=getPDFContent("%s%s"%(diretorio,b1))[0:100]
			
			indice=IndexPaper(b1,diretorio,index)
			indices.append(indice)
			
			
		except:
			indice=IndexPaper(b1,diretorio,'')
			erros.append(indice)

	return indices,erros

class IndexPaper(object):
	def __init__(self,arquivo,pasta,indice):
		self.arquivo=arquivo
		self.pasta=pasta
		self.indice=indice


def compararArquivos(diretorio1,diretorio2):
	elemento1=getIndexPdf(diretorio1)
	elemento2=getIndexPdf(diretorio2)
	
	for elemen in elemento1[0]:
		
		for elemen2 in elemento2[0]:
			if elemen.indice == elemen2.indice and len(elemen.indice)>0 :
				print elemen.arquivo



dir1='/home/allan/sbie/ieee/'
dir2='/home/allan/sbie/scopus/'


compararArquivos(dir1,dir2)
















