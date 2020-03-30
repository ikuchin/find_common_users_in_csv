# find_common_users_in_csv
Task is to write a function **find_users** in file **solution.py** that should receive file names, at least 2.
And should return list of user_id's that are present in both files. List should have unique values.

Goal is to use as less memory as possible. And have a decent runtime.

It's acceptable to use non common data structures.

When you you can run test by running next command
```
python -m unittest discover
```

Best results using build in python data structures:
- 1KiB file - runtime:0.1 sec, memory:0.0MB
- 1MiB file - runtime:0.2 sec, memory:0.2MB
- 1GiB file - runtime:1,0 min, memory:1.4GB !!!