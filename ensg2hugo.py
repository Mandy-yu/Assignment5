#!/usr/bin/python
import fileinput
import re
import sys
my_file=sys.argv[2]
Lookup_geneID={}
for line in fileinput.input(['Homo_sapiens.GRCh37.75.gtf']):
    gene_id_matches = re.findall('gene_id \"(.*?)\";',line)
    gene_name_matches = re.findall('gene_name \"(.*?)\";',line)
    text_in_columns = re.split('\t',line)
    if len(text_in_columns)>3:
       if gene_id_matches:
          if gene_name_matches:
             Lookup_geneID[gene_id_matches[0]] = gene_name_matches[0]
print '"","gene_id","gene_type","logFC","AveExpr"'
for line in fileinput.input(my_file):
    text_in_columns = re.split('\t',line)
    match = re.search('ENSG\d*',text_in_columns[1])
    if match.grou() in Lookup_geneID:
        text_in_columns[4]=re.sub('\n','',text_in_columns[4].rstrip());
        print text_in_columns[0] + ",\"" + Lookup_geneID[text_in_columns[1]] + "\"," + text_in_columns[2] + "," + text_in_columns[3] + "," + text_in_columns[3] + "," + text_in_columns[4]
