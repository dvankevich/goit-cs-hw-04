#!/bin/bash

# Run:
# ./word_counter.sh | sort -k2,2nr | less

if [ ! -d "files" ]; then
  echo "directory 'files' not found."
  exit 1
fi

declare -A word_count

for file in files/*.txt; do
  while read -r line; do
    for word in $line; do
      word=$(echo "$word" | tr '[:upper:]' '[:lower:]')
      ((word_count["$word"]++))
    done
  done < "$file"
done

echo "Кількість слів у файлах:"
for word in "${!word_count[@]}"; do
  echo "$word: ${word_count[$word]}"
done