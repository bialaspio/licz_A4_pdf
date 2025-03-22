import fitz  # PyMuPDF
import os,glob,math, time  

naz_csv = time.strftime('%Y%m%d-%H_%M_%S')
csv = open('.\\csv\\liczA4'+naz_csv+'.csv', 'w')
csv.write('plik;strona;szre_str;wys_str;ilosc_str_A4+5%\n')

csv_str = open('.\\csv\\liczA4_str'+naz_csv+'.csv', 'w')
csv_str.write('plik;ilosc_str_A4+5%;licz_str\n')

def count_a4_pages(pdf_path):
	licz_str_a4 = 0
	licz_str_a4_all = 0

	pdf_document = fitz.open(pdf_path)
	
	for page_number in range(pdf_document.page_count):
		page = pdf_document[page_number]
		page_width = page.rect.width
		page_height = page.rect.height
		
		# A4 size dimensions in points (72 points = 1 inch)
		#a4_width = 595.276
		#a4_height = 841.890
		
		a4_width = 2480
		a4_height = 3507

		#if page_width >= 550 and page_height >= 830:
		#	a4_page_count += 1
		
		if page_width<page_height:
			page_width_a = page_width
			page_height_a = page_height
		else:
			page_width_a = page_height
			page_height_a = page_width

			#szer_mmA4 = wys_mm
			#wys_mmA4 = szer_mm
		
		licz_w = page_width_a/(2604)
		licz_h = page_height_a/(3683)
		print (licz_w)
		print (licz_h)
		#licz_w_int = math.ceil(licz_w)
		#licz_h_int = math.ceil(licz_h) 
		print (str(licz_w)+"  ---  "+str(licz_h))
		licz_str_a4 = math.ceil(licz_w*licz_h)
		print ("licz_str_a4:" + str(licz_str_a4))
		licz_str_a4_all += licz_str_a4;
		csv.write(str(os.path.basename(pdf_path)) +";"+str(page_number+1) +";"+str(page_width_a)+";"+str(page_height_a)+";"+str(int(licz_str_a4))+'\n')
		
	pdf_document.close()
	#os.system("pause")

	return licz_str_a4_all



#pdf_file_path = "your_pdf_file.pdf"
main_dir = 'k:\\Bierunsko_Ledzinski_cz3\\07_wysylka\\operaty_pdf\\'

for (dirpath, dirnames, filenames) in os.walk(main_dir):	
	lista_pdf = glob.glob(dirpath+'\\*.pdf')
	for pdf_file in lista_pdf:
		print (pdf_file)
		pdf_document = fitz.open(pdf_file)
		licz_str = pdf_document.page_count
		pdf_document.close()
		a4_count = count_a4_pages(pdf_file)
		#print(f"Number of A4-sized pages: {a4_count}")
		csv_str.write(str(os.path.basename(pdf_file)) +";"+str(a4_count)+";"+str(licz_str)+"\n")
