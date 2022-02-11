#!/usr/bin/python3
import csv
import sys
import argparse
import re
from docx import Document
from docx.shared import Inches
import pandas as pandasForSortingCSV

document = Document()

def main(args):
	#Pre-requisites -> sort CSV file based on Description
	filename = args['file']
	
	
	misconfig = ''
	i=1
	with open(filename) as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			if row['Risk'] != 'FAILED':
				continue
			if misconfig[0:20] != row['Description'][0:20]:
				misconfig = row['Description']
				table = document.add_table(rows=6, cols=2)
				name = row['Description']
				name = name[:name.index(": [FAILED]")]
				Desc = row['Description']
				Desc = Desc[Desc.index("]")+3:Desc.index("Rationale:")]
				Rat = row['Description']
				Rat = Rat[Rat.index("Rationale")+12:Rat.index("Impact:")]
				Sol = row['Description']
				Sol = Sol[Sol.index("Solution:")+10:Sol.index("Default Value")-5]
				finding = row['Description']
				finding = finding[finding.index("Default Value"):finding.index('See Also')-2]
				#first row
				cols0 = table.rows[0].cells
				cols0[0].text = 'Name'
				cols0[1].text = name
				#second row
				cols1 = table.rows[1].cells
				cols1[0].text = 'Description'
				cleaneddesc = re.sub(r'^Note.*\n?|^NOTE.*\n?|^Reference.*\n?|\n\s{2,10}\n', '', Desc, flags=re.MULTILINE)  #regex to clean notes
				cols1[1].text = cleaneddesc
				#third row
				cols2 = table.rows[2].cells
				cols2[0].text = 'Rationale'
				cols2[1].text = Rat
				#fourth row
				cols3 = table.rows[3].cells
				cols3[0].text = 'Solution'
				cols3[1].text = Sol
				#Fifth Row
				cols4 = table.rows[4].cells
				cols4[0].text = 'Finding'
				cols4[1].text = finding
				#Sixth row
				cols5 = table.rows[5].cells
				cols5[0].text = 'IP Addresses Affected'
				cols5[1].text = row['Host'] + ' [-] '
				
				document.add_page_break()

			else:
				cols5[1].text = cols5[1].text + row['Host'] + ' [-] '
	document.save('/home/troll/Desktop/demo.docx')
		
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Parse Nessus CIS benchmark results")
	parser.add_argument("-f", "--file", help="Full path to file", required=True)

	args = parser.parse_args()

	main(vars(args))

