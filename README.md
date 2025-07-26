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

## clean cache

run as root

```
sync && echo 3 > /proc/sys/vm/drop_caches
```

run via sudo

```
sudo sync && sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"
```

## show process tree

```
pstree -p $(pgrep -f find-with-threading.py)

python(11549)─┬─{python}(11550)
              └─{python}(11551)


pgrep -f find-with-multiprocessing.py | xargs -I {} pstree -p {}

python(13457)─┬─python(13465)───{python}(13469)
              ├─python(13466)
              ├─python(13467)
              ├─{python}(13468)
              ├─{python}(13470)
              └─{python}(13471)
python(13465)───{python}(13469)
python(13466)
python(13467)

```

### top command screenshot

```
top - 18:52:13 up  1:21,  1 user,  load average: 2,82, 5,25, 4,39
Tasks: 293 total,   2 running, 291 sleeping,   0 stopped,   0 zombie
%Cpu0  : 24,0 us, 30,1 sy,  0,0 ni, 40,3 id,  5,6 wa,  0,0 hi,  0,0 si,  0,0 st
%Cpu1  : 22,4 us, 33,7 sy,  0,0 ni, 37,8 id,  5,6 wa,  0,0 hi,  0,5 si,  0,0 st
MiB Mem :   5794,1 total,   1814,8 free,   3065,9 used,    913,4 buff/cache
MiB Swap:   5072,0 total,   4344,2 free,    727,8 used.   2356,8 avail Mem

    PID USER     S  %CPU  %MEM     TIME+ COMMAND
  14382 dima     D  43,1   0,4   0:03.20 python find-with-multiprocessing.py
  14381 dima     R  42,6   0,4   0:03.21 python find-with-multiprocessing.py
```

## execution time

10000 files 2 threads, 2 processors

```
# clear cache
sudo sync && sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"

python find-with-threading.py
. . .
Execution time: 16.22 seconds

# clear cache
sudo sync && sudo sh -c "echo 3 > /proc/sys/vm/drop_caches"

python find-with-multiprocessing.py
. . .
Execution time: 15.98 seconds
```
