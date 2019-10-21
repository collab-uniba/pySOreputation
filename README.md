# pySOreputation
A sequential script to compute an approximation of the reputation gained by a [Stack Overflow](https://stackoverflow.com/) user up to a given date in python.

### NOTE:
You will need to install [Git LFS](https://git-lfs.github.com/) extension to check out this project. Once installed and initialized, simply run:

```$ git lfs clone https://github.com/collab-uniba/pySOreputation.git```

## DISCLAIMER

The extracted reputation is only an estimate (with a ~10% error). The following rules are not considered:
- Suggested edit is accepted: +2 (up to +1000 total per user)
- Bounty awarded to your answer: + full bounty amount
- One of your answers is awarded a bounty automatically: + half of the bounty amount (see more details about how bounties work)
- Example you contributed to is voted up: +5
- Proposed change is approved: +2
- First time an answer that cites documentation you contributed to is upvoted: +5
- You place a bounty on a question: - full bounty amount
- One of your posts receives 6 spam or offensive flags: -100

## Fair Use Policy
Please, cite the following works if you intend to use our tool for your own research:

>F. Calefato, F. Lanubile, N. Novielli. “[Moving to Stack Overflow: Best-Answer Prediction in Legacy Developer Forums.](http://collab.di.uniba.it/fabio/wp-content/uploads/sites/5/2014/05/a13-calefato.pdf)” In *Proc. 10th Int’l Symposium on Empirical Softw. Eng. and Measurement (ESEM’16)*, Ciudad Real, Spain, Sept. 8-9, 2016, DOI:10.1145/2961111.2962585.

```
@inproceedings{Calefato_esem2016,
 author = {Calefato, Fabio and Lanubile, Filippo and Novielli, Nicole},
 title = {Moving to Stack Overflow: Best-Answer Prediction in Legacy Developer Forums},
 booktitle = {Proc. 10th ACM/IEEE Int'l Symposium on Empirical Software Engineering and Measurement}, 
 series = {ESEM '16},
 year = {2016},
 isbn = {978-1-4503-4427-2},
 location = {Ciudad Real, Spain},
 pages = {13:1--13:10},
 articleno = {13},
 numpages = {10},
 url = {http://doi.acm.org/10.1145/2961111.2962585},
 doi = {10.1145/2961111.2962585},
 publisher = {ACM},
} 
```
>F. Calefato, F. Lanubile, M.C. Marasciulo, N. Novielli. MSR Challenge: “[Mining Successful Answers in Stack Overflow.](http://collab.di.uniba.it/fabio/wp-content/uploads/sites/5/2014/05/MSR_2015_calefato_et_al.pdf)” In *Proc. 12th IEEE Working Conf. on Mining Software Repositories (MSR 2015)*, Florence, Italy, May 16-17, 2015.

```
@inproceedings{Calefato_msr2015,
 author = {Calefato, Fabio and Lanubile, Filippo and Marasciulo, Maria Concetta and Novielli, Nicole},
 title = {Mining Successful Answers in Stack Overflow},
 booktitle = {Proc. 12th Working Conf. on Mining Software Repositories},
 series = {MSR '15},
 year = {2015},
 isbn = {978-0-7695-5594-2},
 location = {Florence, Italy},
 pages = {430--433},
 numpages = {4},
 url = {http://dl.acm.org/citation.cfm?id=2820518.2820579},
 publisher = {IEEE Press},
}
```

## Database Setup
If you want to run your script locally or deploy the web service on your own server, you need to setup a MySQL database. From this point forward, we assume that you have already imported the [SO dump](https://archive.org/download/stackexchange) to a local MySQL database (there are several scripts that you can easily adapt to your purpose; see [here](https://gist.github.com/megansquire/877e028504c92e94192d) for example).

### Requirements
- Python 3
 - PyMysql version 0.7.9 (or superior)

Go to the `scripts/db-setup/` folder and run in batch mode the sql script `setup_sequential.sh`:

```$ bash setup_sequential.sh```
## NOTE:
Before running, edit the first lines of the file to change the following information:
```
#!/bin/bash
MYSQL_USER=root
MYSQL_PASS=secret
MYSQL_SO_DB=stackoverflow
...
```
This script will create several table/views and indexes to speed up the querying process.

## How to Run
The scripts referenced in this section must be edited prior to execution, in order to customize the following variables:
- MySQL username
- MySQL password
- SO database name
### Script: Sequential version
#### Requirements
- Python 3
- PyMySQL version 0.7.9

#### Usage
From comand line run:

```$ python reputation.py```
