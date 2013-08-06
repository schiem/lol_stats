A simple python program which will generate a raw text file containing the stats of all the
summoners in the video game "League of Legends," which is done by pulling data from the 
official league of legends website.

The only official bug at the moment is that the list of summoners must be copied by hand from
the page source after it has been loaded, as the summoners list is dynamically generated
upon loading.  This has been placed in a file called lol_champs, and is parsed in python.

A generated list of champions stats has been uploaded, but if this becomes outdated then
rerun the program.  If a new champion comes out who is not in the champions list, then 
go to the champions list (url is in the python file) and inspect the champion grid. 
There will be a \<ul\> containing a list of "champion-grid-*champion name*".  Copy and paste
this list into the lol_champs file (in its entirety) and rerun the program.

