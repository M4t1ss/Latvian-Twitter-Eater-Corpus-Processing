#/bin/bash

echo "Extracting plain text tweets"
python ../text.py
mv ../ltec-full-december-2020-nominative.txt .

echo "Replacing URLs and user mentions"
cat ltec-full-december-2020-nominative-date.txt | \
	sed -e 's!http\(s\)\{0,1\}://[^[:space:]]*!!g' | \
	sed 's/@[^[:space:]]\+/@USR/g' | \
	sed 's/@USR @USR/@USR/g' | \
	sed 's/@USR @USR/@USR/g' | \
	sed ':a;N;$!ba;s/\n@USR /\n/g' | \
	sed ':a;N;$!ba;s/\nRT @USR /\n/g' | \
	sed ':a;N;$!ba;s/ @USR\n/\n/g' | \
	sed ':a;N;$!ba;s/@USR\n/\n/g' \
	> ltec-full-december-2020-nominative-date.UR.US.txt

echo "Running Tokenizer"
cat ltec-full-december-2020-nominative-date.UR.US.txt | /home/matiss/tools/mosesdecoder/scripts/tokenizer/tokenizer.perl -no-escape -l lv | sed 's/@ USR/@USR/g' > ltec-full-december-2020-nominative-date.UR.US.tok.txt

echo "Sorting - filtering unique lines"
sort -uf ltec-full-december-2020-nominative-date.UR.US.tok.txt > ltec-full-december-2020-nominative-date.UR.US.tok.u.txt

echo "Removing repetative substrings"
python substrings.py

echo "Finding words of interest"
python filter-txt.py

echo "Done!"