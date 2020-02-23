# pySOreputation
A sequential script to compute an approximation of the reputation gained by a [Stack Overflow](https://stackoverflow.com/) user up to a given date in python.

#### NOTE:
You will need to install [Git LFS](https://git-lfs.github.com/) extension to check out this project. Once installed and initialized, simply run:

```$ git lfs clone https://github.com/collab-uniba/pySOreputation.git```

## DISCLAIMER

The extracted reputation is only an estimate (with an avg error <10%). Also, note that the scripts are already compliant with the [change][https://stackoverflow.blog/2019/11/13/were-rewarding-the-question-askers) in the reputation system that doubles the reputation points earned from getting an upvote to a question.

Still, the following rules are not considered:
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

Cd to `./db-setup/` folder and run the sql script `setup_sequential.sh`:

```$ bash setup_sequential.sh```

#### NOTE:
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
- Python 3+
- PyMySQL version 0.7.9

#### Usage
From command line run:

```$ python reputation.py```

### Script: Parallel version
Unlike the sequential version, the parallel one does not use a MySQL database. Instead, it relies on several CSV files that are created *ad hoc* by running the script `setup_parallel.sh`, which will retrieve the content from the database and pre-process it for increasing the speed.

#### Requirements
- Python 3.4+
- Pandas 
- concurrent.futures

#### Usage
From the command line run:
```$ python main.py```

## Web Service 
The web service is built upon the parallel version, so make sure that you have generated the CSV files by running the script `setup_parallel.sh` before starting it.

#### Requirements
- Python 3.4+
- Flask 
- uWSGI 
- Pillow

#### How to run
Before first run, execute once the setup file:
```bash
sh setup_ws.sh
```

#### Server
From the command line, run:
```uwsgi --ini app.ini```

Then, wait for the setup of application service.

#### Client
You can test a demo version of the service at this address: [http://172.8.30.16:18000](http://172.8.30.16:18000). 
*Note that the demo uses the official dump of 2019-08-31*.

To invoke the service from the command line, execute the following:

```bash
curl \
  --header "Content-type: application/json" \
  --request POST \
  --data '{"user_id": "1315221", "date": "2019-08-31"}' \
  http://hostaddress:19000/estimate
```

The returned json is formatted as follows:

```json
{
   "1315221": {
      "estimated": 35,
      "name": "bateman",
      "registered": 38
   }
}
```
