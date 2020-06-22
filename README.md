

# Nanopore methylation post-process
Post processes of methylation data by nanopolish.
(1) convert bam for IGV.
(2) calculate the methylation frequency.
(3) add Haplotype tag.

Output from nanopolish [.methylation_calls.tsv] is a input in this processes.

## convert bam for IGV bisulfate mode

```
root=/home/path/to/nanopmethyl/
ref=/home/path/to/reference/hg38c.fa
input_tsv=$root/methylation_call/COLO829.methylation_calls.tsv.gz
cpg=$root/methylation_call/COLO829.methylation_calls.bed
bam=$root/bam/COLO829.bam
out=$root/convert_bam/COLO829_me.bam
t=10
#chr=chr21:1-46709983


echo start:mtsv2bedGraph.py  
date
python ./nanopore-methylation-utilities/mtsv2bedGraph.py -i $input_tsv -g $ref > $cpg

sort -k1,1 -k2,2n $cpg | bgzip > $cpg.gz
tabix -p bed $cpg.gz

echo end:mtsv2bedGraph.py
date
echo start:convert_bam_for_methylation.py
date

# option to specify the region, -r $bed OR -w chr:start-end
python ./nanopore-methylation-utilities/convert_bam_for_methylation_refbase_ni.py -t $t \
  -f $ref -b $bam -c $cpg.gz |\
  samtools sort -o $out
```

## calculate methylation frequency
step1
-c: threshold default=2.0
```
python ./nanopolish/calculate_methylation_frequency.py ./methylation_call/COLO829.methylation_calls.tsv > COLO829.methylation_frequency.tsv

```
step2
Change the unit of position from a motif to a base.
Filtering by read depth (default >=10).
```
nanop_methylfreq1base.py -input_file {} -output_file {} -r {10}
```

## add Haplotype tag to a converted bam.

add_bam_haptag.py --hap {bam of haplotype} --me {bam of methylation} --out {output bam name}

## Comparing the methylation frequency with infinium. 
```
bedtools intersect -wo -a ./inf/inf_nrm_COLO829.bedGraph -b COLO829.methylation_frequency.bedGraph > ./intersect/COLO829_inf_nanop.bed

```
