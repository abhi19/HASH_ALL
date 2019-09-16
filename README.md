# HASH_ALL: Store Hashesh of entire file directory
Takes hashes of the input file directory , check for the same file hashes periodically, and compares them with previously recorded hashes.  Alerts on change


root@kali:~# python hash.py
Found directory: .
.
	hash_list.txt
	RvB Fall 19 (9_7).pdf
	RDC-Red.ovpn
	rec.py
	hash.py
	1.txt
	list_of_hashes.txt
	RDC-Blue.ovpn
	hash_list2.txt
Now checking hashes in real time
.
Hashes matched !!! Okay
Sat Sep 14 02:22:07 2019
.
Alert !!! Hash values changed 
Sat Sep 14 02:22:12 2019
