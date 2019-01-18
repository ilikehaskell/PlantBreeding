import com.opencsv.CSVParser;
import com.opencsv.CSVParserBuilder;
import com.opencsv.CSVReader;
import com.opencsv.CSVReaderBuilder;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

import static jdk.nashorn.internal.objects.NativeString.trim;

public class Parser {

    public HashMap<String, String> mapOF = new HashMap<>();
    public HashMap<String, String> codonsToAmino = new HashMap<>();
    public HashMap<String, Integer> indexOfAmino = new HashMap<String, Integer>();
    public Set<String> effects = new HashSet<>();
    int mxSz = 4141;
    Parser(){
            codonsToAmino.put("TTT", "phe");
            codonsToAmino.put("TTC", "phe");
            indexOfAmino.put("phe", 1);

            codonsToAmino.put("TTA", "leu");
            codonsToAmino.put("TTG", "leu");
            codonsToAmino.put("CTT", "leu");
            codonsToAmino.put("CTC", "leu");
            codonsToAmino.put("CTA", "leu");
            codonsToAmino.put("CTG", "leu");
            indexOfAmino.put("leu", 2);

            codonsToAmino.put("ATT", "ile");
            codonsToAmino.put("ATC", "ile");
            codonsToAmino.put("ATA", "ile");
            indexOfAmino.put("ile", 3);

            codonsToAmino.put("ATG", "met");
            indexOfAmino.put("met", 4);


            codonsToAmino.put("GTT", "val");
            codonsToAmino.put("GTC", "val");
            codonsToAmino.put("GTA", "val");
            codonsToAmino.put("GTG", "val");
            indexOfAmino.put("val", 5);

            codonsToAmino.put("TCT", "ser");
            codonsToAmino.put("TCC", "ser");
            codonsToAmino.put("TCA", "ser");
            codonsToAmino.put("TCG", "ser");
            codonsToAmino.put("AGT", "ser");
            codonsToAmino.put("AGC", "ser");
            indexOfAmino.put("ser", 6);

            codonsToAmino.put("CCT", "pro");
            codonsToAmino.put("CCC", "pro");
            codonsToAmino.put("CCA", "pro");
            codonsToAmino.put("CCG", "pro");
            indexOfAmino.put("pro", 7);

            codonsToAmino.put("ACT", "thr");
            codonsToAmino.put("ACC", "thr");
            codonsToAmino.put("ACA", "thr");
            codonsToAmino.put("ACG", "thr");
            indexOfAmino.put("thr", 8);

            codonsToAmino.put("GCT", "ala");
            codonsToAmino.put("GCC", "ala");
            codonsToAmino.put("GCA", "ala");
            codonsToAmino.put("GCG", "ala");
            indexOfAmino.put("ala", 9);

            codonsToAmino.put("TAT", "tyr");
            codonsToAmino.put("TAC", "tyr");
            indexOfAmino.put("tyr", 10);

            codonsToAmino.put("CAT", "his");
            codonsToAmino.put("CAC", "his");
            indexOfAmino.put("his", 11);

            codonsToAmino.put("CAA", "gln");
            codonsToAmino.put("CAG", "gln");
            indexOfAmino.put("gln", 12);

            codonsToAmino.put("AAT", "asn");
            codonsToAmino.put("AAC", "asn");
            indexOfAmino.put("asn", 13);

            codonsToAmino.put("AAA", "lys");
            codonsToAmino.put("AAG", "lys");
            indexOfAmino.put("lys", 14);

            codonsToAmino.put("GAT", "asp");
            codonsToAmino.put("GAC", "asp");
            indexOfAmino.put("asp", 15);

            codonsToAmino.put("GAA", "glu");
            codonsToAmino.put("GAG", "glu");
            indexOfAmino.put("glu", 16);

            codonsToAmino.put("TGT", "cys");
            codonsToAmino.put("TGC", "cys");
            indexOfAmino.put("cys", 17);

            codonsToAmino.put("TGG", "trp");
            indexOfAmino.put("trp", 18);

            codonsToAmino.put("CGT", "arg");
            codonsToAmino.put("CGC", "arg");
            codonsToAmino.put("CGA", "arg");
            codonsToAmino.put("CGG", "arg");
            codonsToAmino.put("AGA", "arg");
            codonsToAmino.put("AGG", "arg");
            indexOfAmino.put("arg", 19);

            codonsToAmino.put("GGT", "gly");
            codonsToAmino.put("GGC", "gly");
            codonsToAmino.put("GGA", "gly");
            codonsToAmino.put("GGG", "gly");
            indexOfAmino.put("gly", 20);

            codonsToAmino.put("TAA", "stop");
            codonsToAmino.put("TAG", "stop");
            codonsToAmino.put("TGA", "stop");
            indexOfAmino.put("0", 21);
    }

    void ParseCSV(){
        String fileName = "src/main/java/input.csv";
        Path myPath = Paths.get(fileName);
        HashMap<String, Integer> hashEff = new HashMap<>();
        CSVParser parser = new CSVParserBuilder().withSeparator(';').build();

        try (BufferedReader br = Files.newBufferedReader(myPath,
                StandardCharsets.UTF_8);
             CSVReader reader = new CSVReaderBuilder(br).withCSVParser(parser)
                     .build()) {

            List<String[]> rows = reader.readAll();


            for (String[] row : rows) {
                String[] eff = row[6].split(";");
                for(int i=0;i<eff.length; i++) {
                    eff[i] = trim(eff[i]);

                    if(hashEff.containsKey(eff[i]))
                        hashEff.put(eff[i], hashEff.get(eff[i]) + 1);
                    else {
                        hashEff.put(eff[i], 1);
                        //System.out.println(eff[i]);
                    }
                }
            }

            for (String[] row : rows) {
                String[] eff = row[6].split(";");
                String maxFreq = "unknown";
                for(int i=0;i<eff.length; i++) {
                    eff[i] = trim(eff[i]);

                    if(!maxFreq.equals("unknown")) {
                        Integer x = hashEff.get(maxFreq);
                        Integer y = hashEff.get(eff[i]);
                        if(x < y && eff[i].length() > 5){
                            maxFreq = eff[i];
                        }

                    } else {
                        if(eff[i].length() > 5)
                            maxFreq = eff[i];
                    }
                }
                maxFreq = maxFreq.replace(' ', '_');
                //maxFreq = maxFreq.replace(',', '_');

                mapOF.put(row[0], maxFreq);
                effects.add(maxFreq);
            }

            //System.out.println(hashEff.get("C:mitochondrial envelope"));
            //System.out.println(rows.size());
            //System.out.println(mapOF.size());

        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    void ParseGenes() throws IOException {
        BufferedWriter writer = new BufferedWriter(new FileWriter("src/main/java/output.csv"));
        int mnm = 123456;
        HashMap<String, Integer> effToMap = new HashMap<>();
        int xk = 1;
        for(String str:effects){
            effToMap.put(str, xk);
            xk++;
        }
        String stt = "a";
        //writer.write("geneId" + ",");
        for(int i=0; i<21; i++){
            writer.write(stt + ",");
            char c = stt.charAt(stt.length() - 1);
            c++;
            if(c > 'z'){
                c = 'a';
                stt += c;
            } else stt = stt.substring(0, stt.length() - 1) + c;
        }

        writer.write("protein\n");


        File file = new File("src/main/java/input12.txt");
        if (!(file.isFile() && file.canRead())) {
            System.out.println(file.getName() + " cannot be read from.");
            return;
        }
        try {
            FileInputStream fis = new FileInputStream(file);
            char current;
            int nbr = 0;
            String geneId = "";

            while (fis.available() > 0) {
                current = (char) fis.read();

                if(current != '>'){
                    String allGene = "";
                    while(current != '>'){
                        if(current == 'A' || current == 'C' || current == 'G' || current == 'T')
                            allGene += current;
                        current = (char) fis.read();
                        if(current == '>'){
                            break;
                        }
                    }
                    //System.out.println(geneId + " " + allGene.length());
                    //System.out.println(allGene);
                    nbr++;
                    List<String> amino = new ArrayList<>();
                    //Find amino
                        for(int i=0; i<allGene.length()-2 ;i+=3){
                            String codon = "";
                            codon += allGene.charAt(i);
                            codon += allGene.charAt(i+1);
                            codon += allGene.charAt(i+2);

                            if(codon.equals("TAA") || codon.equals("TAG") || codon.equals("TGA")) {
                                amino.add(codon);
                                break;
                            }
                            amino.add(codon);
                            //amino.add(indexOfAmino.get(codonsToAmino.get(codon)));
                        }
                    //writer.write(geneId + " ");
                    //
                    //mnm = Math.min(amino.size(), mnm);
                    /*
                    while(amino.size() < 100){
                        amino.add("0");

                    }
                    int x = 1;
                    for(String val: amino){
                        if(val.equals("0")){
                            writer.write("," + 0);
                        }else {

                            writer.write("," + indexOfAmino.get(codonsToAmino.get(val)));
                        }
                        if(x > 99){
                            break;
                        }

                        x++;
                    }*/
                    //
                    String[] hs = new String[]{"phe", "leu", "ile", "val", "met", "ser", "pro", "thr", "ala", "tyr", "his", "gln", "asn", "lys", "asp", "glu", "cys", "trp", "arg", "gly", "stop"};

                    HashMap<String, Integer> frq = new HashMap<>();
                    for(int i=0;i<hs.length;i++){
                        frq.put(hs[i], 0);
                    }
                    for(String val : amino){
                        frq.put(codonsToAmino.get(val), frq.get(codonsToAmino.get(val)) + 1);
                    }
                    for(int i=0;i<hs.length;i++){
                        if(hs.length == i + 1){
                            writer.write( "" + frq.get(hs[i]));
                        }
                        writer.write(frq.get(hs[i]) + ", ");
                    }
                    //System.out.println(geneId);
                    //writer.write(", \"" + mapOF.get(geneId) + "\"");
                    writer.write(effToMap.get(mapOF.get(geneId)) +"E" );
                    //
                    writer.write("\n");
                    geneId = "";
                }

                if(current == '>'){
                    boolean space = false;
                    while(current != '\n'){
                        current = (char) fis.read();
                        if(current == ' ') space = true;
                        if(!space)
                            geneId += current;
                    }

                    //System.out.println(geneId);
                }
                if(nbr == 150) break;
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        //System.out.println(mxSz);
        writer.close();
    }

}
