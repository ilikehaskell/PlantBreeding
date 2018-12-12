import linecache
import time
import csv


start_time = time.time()
generateTestInput = True
#generate test or train dataset

aa = dict()
genes = dict()
aa["TTT"] = "phe"
aa["TTC"] = "phe"
genes["phe"] = 0
aa["TTA"] = "leu"
aa["TTG"] = "leu"
aa["CTT"] = "leu"
aa["CTC"] = "leu"
aa["CTA"] = "leu"
aa["CTG"] = "leu"
genes["leu"] = 0
aa["TCT"] = "ser"
aa["TCC"] = "ser"
aa["TCA"] = "ser"
aa["TCG"] = "ser"
aa["AGT"] = "ser"
aa["AGC"] = "ser"
genes["ser"] = 0
aa["TAT"] = "tyr"
aa["TAC"] = "tyr"
genes["tyr"] = 0
aa["TGT"] = "cys"
aa["TGC"] = "cys"
genes["cys"] = 0
aa["TGG"] = "trp"
genes["trp"] = 0
aa["CCT"] = "pro"
aa["CCC"] = "pro"
aa["CCA"] = "pro"
aa["CCG"] = "pro"
genes["pro"] = 0
aa["CAT"] = "his"
aa["CAC"] = "his"
genes["his"] = 0
aa["CAA"] = "gln"
aa["CAG"] = "gln"
genes["gln"] = 0
aa["CGT"] = "arg"
aa["CGC"] = "arg"
aa["CGA"] = "arg"
aa["CGG"] = "arg"
aa["AGA"] = "arg"
aa["AGG"] = "arg"
genes["arg"] = 0
aa["ATT"] = "ile"
aa["ATC"] = "ile"
aa["ATA"] = "ile"
genes["ile"] = 0
aa["ACT"] = "thr"
aa["ACC"] = "thr"
aa["ACA"] = "thr"
aa["ACG"] = "thr"
genes["thr"] = 0
aa["AAT"] = "asn"
aa["AAC"] = "asn"
genes["asn"] = 0
aa["AAA"] = "lys"
aa["AAG"] = "lys"
genes["lys"] = 0
aa["GTT"] = "val"
aa["GTC"] = "val"
aa["GTA"] = "val"
aa["GTG"] = "val"
genes["val"] = 0
aa["GCT"] = "ala"
aa["GCC"] = "ala"
aa["GCA"] = "ala"
aa["GCG"] = "ala"
genes["ala"] = 0
aa["GAT"] = "asp"
aa["GAC"] = "asp"
genes["asp"] = 0
aa["GAA"] = "glu"
aa["GAG"] = "glu"
genes["glu"] = 0
aa["GGT"] = "gly"
aa["GGC"] = "gly"
aa["GGA"] = "gly"
aa["GGG"] = "gly"
genes["gly"] = 0
aa["ATG"] = "met"
genes["met"] = 0
aa["TAA"] = "stop"
aa["TAG"] = "stop"
aa["TGA"] = "stop"
genes["stop"] = 0
orderedGenes = list()

def main():

    file_input = open("input12.txt", "r")
    file_output = open("output.txt","w")
    protein = dict()
    if generateTestInput:
        with open('input.csv') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            reader = sorted(reader, key=lambda row: (row['\ufeffGeneID']))
            for row in reader:
                protein[row['\ufeffGeneID']] = row['Descriere proteina']
    first_line = 0
    #for each line
    for line in file_input:
        if line[0] == ">":
            if(len(protein[str(line.split(' ', 1)[0][1:])]) < 11):
                continue

            if first_line > 0:
                cnt = 1
                
                for value in orderedGenes:
                    file_output.write(str(value) + ' ')
                    cnt+=1
                if generateTestInput:
                    file_output.write(protein[str(line.split(' ', 1)[0][1:])])
                file_output.write('\n')
            
            #
            first_line += 1
            file_output.write(line.split(' ', 1)[0][1:] + ' ')

            orderedGenes.clear()
        else:
            result_list = [line[i:i + 3] for i in range(0, len(line), 3)]
            for i in range(0, len(result_list)):
                if result_list[i] in aa:
                    orderedGenes.append(aa[result_list[i]])
                    #genes[aa[result_list[i]]] += 1

    #add last dictonary to txt
    for value in orderedGenes:
        file_output.write(str(value) + ' ')

    print("--- %s seconds ---" % (time.time() - start_time))

    file_input.close()
    file_output.close()
main()