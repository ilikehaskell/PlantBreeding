import json 
import re
import time

start_time = time.time()
in_path = "lista_gene.txt"  #path to gene file
out_path = "out.json"  #path to output file

# START = "ATG"
# STOP = ["TGA", "TAA", "TAG"]

aa_names  = ["phe", "leu", "ser", "tyr", "cys", "trp", "pro", "his", "gln", "arg",
             "ile", "thr", "asn", "lys", "val", "ala", "asp", "glu", "gly", "met",
             "stop"]

aa = dict()
aa["TTT"] = "phe"
aa["TTC"] = "phe"

aa["TTA"] = "leu"
aa["TTG"] = "leu"
aa["CTT"] = "leu"
aa["CTC"] = "leu"
aa["CTA"] = "leu"
aa["CTG"] = "leu"

aa["TCT"] = "ser"
aa["TCC"] = "ser"
aa["TCA"] = "ser"
aa["TCG"] = "ser"
aa["AGT"] = "ser"
aa["AGC"] = "ser"

aa["TAT"] = "tyr"
aa["TAC"] = "tyr"

aa["TGT"] = "cys"
aa["TGC"] = "cys"

aa["TGG"] = "trp"

aa["CCT"] = "pro"
aa["CCC"] = "pro"
aa["CCA"] = "pro"
aa["CCG"] = "pro"

aa["CAT"] = "his"
aa["CAC"] = "his"

aa["CAA"] = "gln"
aa["CAG"] = "gln"

aa["CGT"] = "arg"
aa["CGC"] = "arg"
aa["CGA"] = "arg"
aa["CGG"] = "arg"
aa["AGA"] = "arg"
aa["AGG"] = "arg"

aa["ATT"] = "ile"
aa["ATC"] = "ile"
aa["ATA"] = "ile"

aa["ACT"] = "thr"
aa["ACC"] = "thr"
aa["ACA"] = "thr"
aa["ACG"] = "thr"

aa["AAT"] = "asn"
aa["AAC"] = "asn"

aa["AAA"] = "lys"
aa["AAG"] = "lys"

aa["GTT"] = "val"
aa["GTC"] = "val"
aa["GTA"] = "val"
aa["GTG"] = "val"

aa["GCT"] = "ala"
aa["GCC"] = "ala"
aa["GCA"] = "ala"
aa["GCG"] = "ala"

aa["GAT"] = "asp"
aa["GAC"] = "asp"

aa["GAA"] = "glu"
aa["GAG"] = "glu"

aa["GGT"] = "gly"
aa["GGC"] = "gly"
aa["GGA"] = "gly"
aa["GGG"] = "gly"

aa["ATG"] = "met"

aa["TAA"] = "stop"
aa["TAG"] = "stop"
aa["TGA"] = "stop"

genes = dict()
with open(in_path, 'r') as f:
    ''' do stuff'''
    gene = list()
    gene.append(f.readline())
    for line in f:
        if line[0] == '>':
            #do stuff with the gene 
            gene_str = "".join(gene[1:]).replace("\n", "")
            # print(gene_str)
            # input()
            gene_name = gene[0].split(" ")[0]
            genes[gene_name] = dict()
            aacid_list = [gene_str[i:i+3] for i in range (0, len(gene_str), 3)]
            for aacid in aacid_list:
                if aacid not in aa.keys():
                    if "undef" not in genes[gene_name].keys():
                        genes[gene_name]["undef"] = 0
                    genes[gene_name]["undef"] += 1
                    continue
                if aa[aacid] not in genes[gene_name]:
                    genes[gene_name][aa[aacid]] = 0
                genes[gene_name][aa[aacid]] += 1
            gene.clear()
        gene.append(line)

with open(out_path, 'w') as f:
    f.write(json.dumps(genes))

print("--- %s seconds ---" % (time.time() - start_time))