python extract.py

languages=$(ls '1.1/data')

for language in $languages; do
    python main.py $language
done