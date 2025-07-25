# goit-cs-hw-04

## generate text files

```
pip install faker
```

run file generator

```
python file-generator.py
```

the files are in the directory files

## find files with threading

### example of program operation

```
python find-with-threading.py
Результати пошуку: {'Group': ['files/file_7.txt'], 'environment': ['files/file_22.txt', 'files/file_9.txt'], 'stuff': ['files/file_16.txt']}
```

### checking the program's operation using find command

```
find files -name "*.txt" -exec grep -H "mission" {} \; | wc -l
```
