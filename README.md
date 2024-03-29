# pySOreputation [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3687265.svg)](https://doi.org/10.5281/zenodo.3687265)
A service to compute an approximation of the reputation gained by a [Stack Overflow](https://stackoverflow.com/) user up to a given date.

## License
This software is released under the MIT License.

## DISCLAIMER

The extracted reputation is only an estimate (with an avg error <10%). Also, note that the scripts are already compliant with the [change](https://stackoverflow.blog/2019/11/13/were-rewarding-the-question-askers) in the reputation system that doubles the reputation points earned from getting an upvote to a question.

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

## Installation
You will need to install [Git LFS](https://git-lfs.github.com/) extension to check out this project. Once installed and initialized, simply run:

```bash
$ git lfs clone https://github.com/collab-uniba/pySOreputation.git
$ cd pySOreputation
$ conda create --name .venv37 python=3.7 
$ conda activate .venv37
$ pip install -r requirements.txt
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
- Python 3.7+
- PyMySQL version 0.7.9

#### Usage
From command line run:

```bash
$ python reputation.py (--uid ID | --file /path/to/file.txt) --date `YYYY-MM-DD`
```
where:
* `-u | --uid` (*mutually exclusive*) is the numeric id associate with a Stack Overflow user account (e.g., `1315221`)
* `-f | --file` (*mutually exclusive*) is the full path to a text file containing a list (one per line) of user ids
* `-d | --date` (*mandatory*) is the date at which estimate the reputation, formatted as `YYYY-MM-DD`

Please, note that `--uid` and `--file` options are mutually exclusive, if provided together the `--uid` supersede the other.

### Script: Parallel version
Unlike the sequential version, the parallel one does not use a MySQL database. Instead, it relies on several CSV files that are created *ad hoc* by running the script `setup_parallel.sh`, which will retrieve the content from the database and pre-process it for increasing the speed.

#### Requirements
- Python 3.7+
- Pandas 
- concurrent.futures

#### Usage
From the command line run:
```bash
$ python main.py (--uid ID | --file /path/to/file.txt) --date `YYYY-MM-DD`
```
where:
* `-u | --uid` (*mutually exclusive*) is the numeric id associate with a Stack Overflow user account (e.g., `1315221`)
* `-f | --file` (*mutually exclusive*) is the full path to a text file containing a list (one per line) of user ids
* `-d | --date` (*mandatory*) is the date at which estimate the reputation, formatted as `YYYY-MM-DD`

Please, note that `--uid` and `--file` options are mutually exclusive, if provided together the `--uid` supersede the other.

## Web Service 
The web service is built upon the parallel version, so make sure that you have generated the CSV files by running the script `setup_parallel.sh` before starting it.

#### Requirements
- Python 3.4+
- Flask 
- uWSGI 

#### How to run
Before first run, execute once the setup file:
```bash
sh setup_ws.sh
```

#### Server
From the command line, run the script `start_ws.sh`. Then, wait for the application to start up (depending on your system specs, it will take about 10 min).

##### Installation as a service
In order for the web service to start up with the system, follow these steps.

1. Copy `pyso-ws.conf` to `/etc/init`
2. Edit line 13 of copied file to point to the actual path of installation
`cd /path/to/pySOreputation/SOWebService/StackOverflowServer`
3. The configuration assumes you are running a conda environment called `.venv37`. Hence, edit `start_ws.sh` and uncomment line 4 `#source /anaconda3/etc/profile.d/conda.sh` if you find the service not to boot and the script to raise the error 
`CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.`
4. Check if the syntax is correct
```bash
$ init-checkconf /etc/init/pyso-ws.conf
```
5. Start the service manually:
```bash
$ sudo service pyso-ws start 
```
6. The service will start in about 10 minutes. To check the status:
```bash
$ sudo service pyso-ws status
```
7. To check the execution log:
```bash
$ sudo tail -f /var/log/pyso-ws.log
```

#### Client
To launch the client, execute the `start_client.sh` script. The client will be locally accessible at this address [http://127.0.0.1:18000](http://127.0.0.1:18000).

You can test a demo version of the service at this address: [http://172.30.8.16:18000](http://172.30.8.16:18000). 
*Note that the demo uses the official dump of 2019-08-31, so do not query anything after that date*.

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

where `name` is the name chosen by the user, `estimated` is the estimated reputation whereas `registered` 
is the reputation stored in the database as of the dump creation. 

##### Installation as a service
In order for the web client to start up with the system, follow the steps below.
Also, note that the client assumes that the server is executed on the same host on port 19000. If not, edit file `config.py` and change the following variables as needed:
 ```python
WS_HOST = "localhost"
WS_PORT = 19000
``` 

1. Copy `pyso-client.conf` to `/etc/init`
2. Edit line 13 of copied file to point to the actual path of installation
`cd /path/to/pySOreputation/SOWebService/StackOverflowServer`
3. The configuration assumes you are running a conda environment called `.venv37`. Hence, edit `start_client.sh` and uncomment line 4 `#source /anaconda3/etc/profile.d/conda.sh` if you find the service not to boot and the script to raise the error `CommandNotFoundError: Your shell has not been properly configured to use 'conda activate'.`
4. Check if the syntax is correct
```bash
$ init-checkconf /etc/init/pyso-client.conf
```
5. Start the service manually:
```bash
$ sudo service pyso-client start 
```
6. The service will start immediately. To check the status:
```bash
$ sudo service pyso-client status
```
7. To check the execution log:
```bash
$ sudo tail -f /var/log/pyso-client.log
```

#### Screenshots

![An example of input](images/input.png)

*Fig. 1: An example of input*

![The result](images/result.png)

*Fig. 2: And the returned result*

