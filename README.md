
This Program aims to read and gather information from a data file and place information onto a useful text file.
Data filtering and queries are placed on sorting text file.

As output we need to see matches and mismatches from the sorting file.

Datafile.txt
==============
	COMPANY, NAME, POSITION
	Microsoft, Steve, CEO
	Apple, Tim, CEO
	Apple, Jony, Designer
	Incuventure, John, DBA 
	Microsoft, Mike, Developer 
	Microsoft, Don, Division 
	Head Incuventure, Marvin, Developer 
	Incuventure, Brian Developer

Sorting.txt
=============
group by POSITION 
filter by POSITION=CEO 
filter by POSITION=Developer


OUTPUT
===========
20130516093528_POSITION_Developer_mismatch.txt
----------------------------
Microsoft ,Steve ,CEO
Apple ,Tim ,CEO
Incuventure ,John ,DBA
Apple ,Jony ,Designer
Microsoft ,Don ,Division

20130516093528_POSITION_Developer_match.txt
----------------------------
Microsoft ,Mike ,Developer
Head Incuventure ,Marvin ,Developer

20130516093528_POSITION_CEO_mismatch.txt
---------------------------
Incuventure ,John ,DBA
Apple ,Jony ,Designer
Microsoft ,Mike ,Developer
Head Incuventure ,Marvin ,Developer
Microsoft ,Don ,Division

20130516093528_POSITION_CEO_match.txt
--------------------------
Microsoft ,Steve ,CEO
Apple ,Tim ,CEO

