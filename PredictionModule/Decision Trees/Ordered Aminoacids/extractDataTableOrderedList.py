import linecache
import time
import csv


start_time = time.time()
generateTestInput = True
#generate test or train dataset

aa = dict()
genes = dict()
aa["TTT"] = 1 #"phe"
aa["TTC"] = 1 #"phe"
genes["phe"] = 0
aa["TTA"] = 2 #"leu"
aa["TTG"] = 2 #"leu"
aa["CTT"] = 2 #"leu"
aa["CTC"] = 2 #"leu"
aa["CTA"] = 2 #"leu"
aa["CTG"] = 2 #"leu"
genes["leu"] = 0
aa["TCT"] = 3 #"ser"
aa["TCC"] = 3 #"ser"
aa["TCA"] = 3 #"ser"
aa["TCG"] = 3 #"ser"
aa["AGT"] = 3 #"ser"
aa["AGC"] = 3 #"ser"
genes["ser"] = 0
aa["TAT"] = 4 #"tyr"
aa["TAC"] = 3 #"tyr"
genes["tyr"] = 0
aa["TGT"] = 5 #"cys"
aa["TGC"] = 5 #"cys"
genes["cys"] = 0
aa["TGG"] = 6 #"trp"
genes["trp"] = 0
aa["CCT"] = 7 #"pro"
aa["CCC"] = 7 #"pro"
aa["CCA"] = 7 #"pro"
aa["CCG"] = 7 #"pro"
genes["pro"] = 0
aa["CAT"] = 8 #"his"
aa["CAC"] = 8 #"his"
genes["his"] = 0
aa["CAA"] = 9 #"gln"
aa["CAG"] = 9 #"gln"
genes["gln"] = 0
aa["CGT"] = 10 #"arg"
aa["CGC"] = 10 #"arg"
aa["CGA"] = 10 #"arg"
aa["CGG"] = 10 #"arg"
aa["AGA"] = 10 #"arg"
aa["AGG"] = 10 #"arg"
genes["arg"] = 0
aa["ATT"] = 11 #"ile"
aa["ATC"] = 11 #"ile"
aa["ATA"] = 11 #"ile"
genes["ile"] = 0
aa["ACT"] = 12 #"thr"
aa["ACC"] = 12 #"thr"
aa["ACA"] = 12 #"thr"
aa["ACG"] = 12 #"thr"
genes["thr"] = 0
aa["AAT"] = 13 #"asn"
aa["AAC"] = 13 #"asn"
genes["asn"] = 0
aa["AAA"] = 14 #"lys"
aa["AAG"] = 14 #"lys"
genes["lys"] = 0
aa["GTT"] = 15 #"val"
aa["GTC"] = 15 #"val"
aa["GTA"] = 15 #"val"
aa["GTG"] = 15 #"val"
genes["val"] = 0
aa["GCT"] = 16 #"ala"
aa["GCC"] = 16 #"ala"
aa["GCA"] = 16 #"ala"
aa["GCG"] = 16 #"ala"
genes["ala"] = 0
aa["GAT"] = 17 #"asp"
aa["GAC"] = 17 #"asp"
genes["asp"] = 0
aa["GAA"] = 18 #"glu"
aa["GAG"] = 18 #"glu"
genes["glu"] = 0
aa["GGT"] = 19 #"gly"
aa["GGC"] = 19 #"gly"
aa["GGA"] = 19 #"gly"
aa["GGG"] = 19 #"gly"
genes["gly"] = 0
aa["ATG"] = 20 #"met"
genes["met"] = 0
aa["TAA"] = "stop"
aa["TAG"] = "stop"
aa["TGA"] = "stop"
genes["stop"] = 0
orderedGenes = list()

def main():

    file_input = open("input12.txt", "r")
    file_output = open("out.txt","w")
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
                    file_output.write("\"" + protein[str(line.split(' ', 1)[0][1:])] + "\"")
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