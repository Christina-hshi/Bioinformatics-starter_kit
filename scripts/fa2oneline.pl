#!/usr/bin/perl -w
use strict;

my $usage="$0 <FASTA>\n";
my $input_fasta=$ARGV[0] || die $usage;
open(IN,"<$input_fasta") || die ("Error opening $input_fasta $!");

my $line = <IN>; 
print $line;

while ($line = <IN>)
{
	chomp $line;
	if ($line=~m/^>/gi) { print "\n",$line,"\n"; }
	else { print $line; }
}

print "\n";
