from __future__ import division
import sys

#get tpm_gene
gene_count={}
sum_gene=0

with open(sys.argv[1],'r') as in_gene:
    for i in in_gene:
        i=i.strip().split("\t")
        gene=i[0]
        count=int(i[1])
        gene_count[gene]=count
        sum_gene = sum_gene + count

out_gene=open(sys.argv[2],'w')

with open('/media/hobart/rash/Developmental/Species/Homo_sapiens/RNA_UMI/RNA_UMI/bin/GRCh38_gencode_genelist/genelist_lincRNA.txt','r') as list:
    for s in list:
        s=s.strip()
        if s in gene_count:
            tpm=gene_count[s]*10**6/sum_gene
        else:
            gene_count[s]=0
            tpm=0
        out_gene.write("%s\t%d\t%.2f\n" % (s,gene_count[s],tpm))

out_gene.close()
        
#get tpm_gene_ercc        
gene_ercc_count={}
sum_gene_ercc=0

with open(sys.argv[3],'r') as in_gene_ercc:
    for i in in_gene_ercc:
        i=i.strip().split("\t")
        gene=i[0]
        count=int(i[1])
        gene_ercc_count[gene]=count
        sum_gene_ercc = sum_gene_ercc + count
       
out_gene_ercc=open(sys.argv[4],'w')

with open('/media/hobart/rash/Developmental/Species/Homo_sapiens/RNA_UMI/RNA_UMI/bin/GRCh38_gencode_genelist/list_gene_ercc_lincRNA.txt','r') as list:
    for s in list:
        s=s.strip()
        if s in gene_ercc_count:
            tpm=gene_ercc_count[s]*10**6/sum_gene_ercc
        else:
            gene_ercc_count[s]=0
            tpm=0
        out_gene_ercc.write("%s\t%d\t%.2f\n" % (s,gene_ercc_count[s],tpm))

out_gene_ercc.close()
