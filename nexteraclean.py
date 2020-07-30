#!/usr/bin/python3
import sys
import gzip
#Nextera Trans2_rc adapter CTGTCTCTTATACACATCTCCGAGCCCACGAGAC
#This script removes nextera adapter containing sequences from from a fastq file
adapter = 'CTCTTATACACATCTCCGAGCCCA'
seq_file =gzip.open(sys.argv[1],'rt').readlines()
basefile = sys.argv[1].split('\.'[1])
print(basefile[0]+'.fastq.gz')
f = gzip.open(basefile[0]+'.nexteraclean.fastq.gz','wt')
nline = 0
for line in seq_file:
    nline += 1
print(round(nline/4),' sequences')
removed = 0
for i in range(1,nline,4):
    if i+4 < nline:
        if (not seq_file[i].find(adapter) != -1):
            f.write(seq_file[i-1])
            f.write(seq_file[i])
            f.write(seq_file[i+1])
            f.write(seq_file[i+2])
        else:
            removed = removed+1
f.close()
percentage = round(removed/nline*100,2)
print(removed,'sequences','(',percentage,"%"')','were removed!')
        
