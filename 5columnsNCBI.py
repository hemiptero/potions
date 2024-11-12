#!/usr/bin/python3
import sys

nombre_archivo = sys.argv[1]
inicio = ''
fin = ''

with open(nombre_archivo, 'r') as archivo:
    for linea in archivo:
        campos = linea.split('\t')
        if len(campos) >= 5: # Checar que la fila tenga al menos 5 campos
            ty = campos[2]  #Type of feature
            gene = campos[8].split(';') #Partir campo 8 para extraer informacion
            product =''
            name = ''
            inicio = ''
            fin = ''
            note = ''
            seqid = ''
            if campos[2] == 'region':
                seqid = campos[0]
            if campos[6] == '+': #Determinar polaridad de la lectura
                inicio = campos[3]
                fin = campos[4]
            elif campos[6] == '-':
                inicio = campos[4]
                fin = campos[3]
            for items in gene: #Extraer gene, product, name y note
                if items.startswith('gene='):
                    gene = (items.split('=')[1])
                if items.startswith('product='):
                    product = (items.split('=')[1])
                if items.startswith('Name='):
                    name = (items.split('=')[1])
                if items.startswith('note='):
                    note = (items.split('=')[1])
            if "region" in campos[2]:
                print('>Feature '+seqid)
            if "gene" in campos[2]:
                print(inicio+'\t'+fin+'\t'+ty+'\n'+'\t'+'\t'+'\t'+'gene'+'\t'+gene) #Gene
                print(inicio+'\t'+fin+'\t'+'CDS'+'\n'+'\t'+'\t'+'\t'+'product'+'\t'+product) #CDS
                print('\t'+'\t'+'\t'+'transl_table'+'\t'+'5')
                if note != '':
                    print('\t'+'\t'+'\t'+'note'+'\t'+'TAA stop codon is completed by the addition of 3')
            elif campos[2] in ("rRNA", "tRNA"):
                print(inicio+'\t'+fin+'\t'+ty+'\t'+'\n'+'\t'+'\t'+'\t'+'product'+'\t'+name) #tRNA or rRNA
                if note != '':
                    print('\t'+'\t'+'\t'+'note'+'\t'+note)
