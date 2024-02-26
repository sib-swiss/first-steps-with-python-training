### 7.5

# **1.** In **"SARS-CoV-2_S.gb"** file, you will find the GenBank sequence
# records of the 'S' gene for the first 50 accessions we used in previous
# exercises. 
# Can you create a **fasta** file that contains the spike protein sequences
# for these? Try to keep their `.id` and avoid translating stop codons!

with open("spike_proteins.fa", "w") as fasta:
    for rec in SeqIO.parse("data/SARS-CoV-2_S.gb", "genbank"):
        prot = rec.translate(to_stop=True)
        prot.id = rec.id
        SeqIO.write(prot, fasta, "fasta")


# **2**. Did you notice the *Warning* above, when we try to translate the
# first 50 accessions.
# It seems the length of one or more of our 'S' CDSs is not multiple of three.
# Can you find which one?

for rec in SeqIO.parse("data/SARS-CoV-2_S.gb", "genbank"):
    for feature in rec.features:
        if feature.type == 'gene' and 'S' in feature.qualifiers['gene']:
            s_length = feature.location.end - feature.location.start
            if s_length % 3 != 0:
                print("'S' gene from '{}' has a length of {}, which is not a multiple of 3".format(
                    rec.id, s_length))