# log2json

Convert log file to text or json format.

## Installation

This project can be installed via `pip`:

```bash
pip install log2json-fauzanelka
```

Or build it yourself by cloning this project:

```bash
git clone https://github.com/fauzanelka/log2json
```

Then install

```bash
cd log2json
python setup.py install
```

## Usage

### Convert to text format

Convert log file to text (default)

```bash
log2json /var/log/nginx/access.log -o $HOME/nginx-access.txt
```

Convert multiple log files to text with destination directory

```bash
log2json /var/log/nginx/access.log /var/log/nginx/error.log -d $HOME/log2json/
```

If destination directory is not provided, the scripts will use `current directory` + `log2json_output`

### Convert to json format

Convert log file to json

```bash
log2json /var/log/nginx/access.log -t json -o $HOME/nginx-access.json
```

Convert multiple log files to text with destination directory

```bash
log2json /var/log/nginx/access.log /var/log/nginx/error.log -t json -d $HOME/log2json/
```

Convert log file to json with regex (advanced)

```bash
log2json /var/log/nginx/access.log -t json -o $HOME/nginx-access.json -e '^(?P<remote_addr>.*?) - (?P<remote_user>.*?) \[(?P<time_local>.*)?\] \"(?P<request>.*?)\" (?P<status>\d+) (?P<body_bytes_sent>\d+) \"(?P<http_referer>.*?)\" \"(?P<http_user_agent>.*?)\" \"(?P<http_x_forwarder_for>.*?)\"$'
```

### For further documentation you can run

```bash
log2json -h
```
