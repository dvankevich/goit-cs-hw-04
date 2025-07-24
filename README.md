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
find files -name "\_.txt" -exec grep -H "Group" {} \;

files/file_7.txt:Mind inside western interesting happen job wide character. Group these four work task employee.

find files -name "\_.txt" -exec grep -H "environment" {} \;

files/file_22.txt:Executive door wait represent lawyer. Book herself environment.
files/file_9.txt:Rock simple actually purpose defense final like cold. Visit majority despite source environment. Argue special middle.

find files -name "\*.txt" -exec grep -H "stuff" {} \;

files/file_16.txt:Cultural cause fill energy history then area. Arm at police use. Citizen stuff trade group.

```
