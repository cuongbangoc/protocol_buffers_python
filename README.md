# protocol_buffers_python
This is example about Protocol Buffer and RabbitMQ. Use Protocol Buffer to encode and decode data, and using Python 
to send and receive it from RabbitMQ server

### PREREQUISITE:
- python2.7
- virtualenv
- pip
- pika


### INSTALLATION:
```
virtualenv -p /usr/bin/python2.7 env
source env/bin/activate

# install library
pip install -r requirements.txt 
cd python
python setup.py install
```


### RUN PRODUCER AND CONSUMER
```
python producer.py
python consumer.py

```

