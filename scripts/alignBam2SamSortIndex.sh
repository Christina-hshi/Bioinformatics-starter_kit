#!/bin/sh

#	Created by Christina SHI <christina.hshi@gmail.com>

if [ "$#" -eq 0 ]; then
	echo "Usage: $0 <seqFile> <ref>" >&2
	echo "options:"
	echo "<seqFile>  fasta or fastq file to align"
	echo "<ref> reference file, default: MHC reference"
	echo "*'BWA mem' is used by default; Assume single-end read in file."
	exit 1
fi

QFile=$1
if [ "$#" -eq 2 ];then
	Ref=$2
else
	Ref=/public/hshi/reference/GRCh38/hg38.fa
fi
#Ref=consensus.fa

QNAME="${QFile/\.fa/}"
QNAME="${QFile/\.fasta/}"
QNAME="${QFile/\.fq/}"
QNAME="${QFile/\.fastq/}"
bwa mem -t 30 -P -o ${QNAME}.sam ${Ref} ${QFile}
#bwa mem -t 30 -L 500,500 -o ${QNAME}.sam ${Ref} ${QFile}
#mv ${QNAME}.sam ${QNAME}.sam.beforeFilter
#samtools view -h -q 10 -o ${QNAME}.sam ${QNAME}.sam.beforeFilter

samtools view -bS -o ${QNAME}.bam ${QNAME}.sam
#samtools sort -f ${QNAME}.bam ${QNAME}.sort.bam
samtools sort -o ${QNAME}.sort.bam ${QNAME}.bam
mv ${QNAME}.sort.bam ${QNAME}.bam
samtools index ${QNAME}.bam
