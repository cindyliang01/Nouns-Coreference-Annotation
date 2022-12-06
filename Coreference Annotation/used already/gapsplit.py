import pandas as pd
import re
# Passing the TSV file to
# read_csv() function
# with tab separator
# This function will
# read data from file
interviews_df = pd.read_csv('Project/gap-development.tsv', sep='\t')

import csv
tsvfile= open('Project/gapdev_edit.tsv', 'w', newline='')
writer = csv.writer(tsvfile, delimiter='\t', lineterminator='\n')
writer.writerow(["Original Text","User annotations", "Annotated Text"])


j=0
for curr_text in interviews_df["Text"]:
    if(re.search("\[|\]|[0-9]+|_",curr_text)==None and len(curr_text)<350):
        writer.writerow([curr_text])
        #print(curr_text)
        j=j+1
print(j)

