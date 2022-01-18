# Github repository: https://github.com/Christina-hshi/Bioinformatics-starter_kit.git
# By Christina HUAN SHI

import sys
from utility import logging

def DNA_RC(seq):
  base2RCbase={'A':'T', 'a':'t', 'T':'A', 't':'a', 'G':'C', 'g':'c', 'C':'G', 'c':'g','N':'N', 'n':'n'}
  res=""
  for x in range(0, len(seq)):
    res = base2RCbase[seq[x]] + res
  return res

def DNA_HammingDis(seq1, seq2):
  if len(seq1) != len(seq2):
    logging.error("Length of two sequences are not the same!\n\tlen. of seq1: "+str(len(seq1))+"\n\tlen. of seq2: "+str(len(seq2)))
  mismatches=0
  for x in range(0, len(seq1)):
    if seq1[x] != seq2[x]:
      mismatches = mismatches + 1
      if mismatches > maxallowed:
        return mismatches
  return mismatches

#Scoring scheme:
#   mismatch: -1
#   gap openning: -1
#   gap extension: -1
#   match: 1
#Return: [max_score, max_score_pos(aligned pos of last G in PAM, count from zero)]
def AligngRNA(seq, gRNA): #The last base of match should be "G" ("NGG"). "N" is allowed but will counted as mismatch, except "N" in "NGG"
  assert(seq)
  assert(gRNA)
  # if seq.find("N") != -1:
  #   logging.error("[Warning] N in sequence!")
  #   sys.exit(1)
  seq_len = len(seq)
  assert(len(gRNA) == 20)
  gRNA = gRNA + "NGG"
  seq = seq.upper()
  score_mat = [[0 for y in range(0, len(gRNA))] for x in range(0, len(seq))]
  for row in range(0, len(seq)):
    if seq[row] == gRNA[0]:
      score_mat[row][0] = 1
    else:
      score_mat[row][0] = -1
  for col in range(0, len(gRNA)):
    if seq[0] == gRNA[col]:
      score_mat[0][col] = 1-col
    else:
      score_mat[0][col] = -1-col
  for row in range(1, len(seq)):
    for col in range(1, len(gRNA)):
      diag = score_mat[row-1][col-1]
      if seq[row] == gRNA[col] or (gRNA[col]=="N"):
        diag = diag + 1
      else:
        diag = diag - 1
      score_mat[row][col] = max(max(diag, score_mat[row-1][col]-1), score_mat[row][col-1]-1)
  #maximum score by subsequence ending with G
  max_score = [0, 0]
  for row in range(0, len(seq)):
    if seq[row] == "G":
      if score_mat[row][len(gRNA)-1] > max_score[0]:
        max_score = [score_mat[row][len(gRNA)-1], row]
      # max_score = max(max_score, score_mat[row][len(gRNA)-1])
  return max_score
