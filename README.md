Python-service sets up a simple service with a daemon that runs in the background.\
It's used with pyservice.Service().run(), which:
1. Starts the daemon if necessary by running the daemon_setup function. Otherwise the client will connect to the existing daemon.
2. Runs the client_sender function.
3. Send the client_sender output to the daemon where it is the input for the daemon_main function
4. Send the daemon_main output to the client where it is the input for the client_receiver function
5. Run the client_receiver function

Service arguments:
- daemon_setup:
  - input: none
  - output: none
  - runs any necessary startup for the daemon
- client_sender:
  - input: none
  - output: json or string
- daemon_main:
  - input: json or string
  - output: json or string
- client_receiver:
  - input: json or string
  - output: none


Example test.py:

```
import pyservice
import argparse

def main(args):
    return int(args[1])+3

if __name__ == "__main__":
    pyservice.Service('test', daemon_main = main).run()
```

Run with:
```
>>> test.py 3
6
```


Troubleshooting:
"Traceback (most recent call last):
  File "/tmp/test.py", line 8, in <module>
    pyservice.Service('test', daemon_main = main).run()
  File "/usr/local/lib/python3.6/dist-packages/python_service-0.0.7-py3.6.egg/pyservice/service.py", line 84, in run
  File "/usr/local/lib/python3.6/dist-packages/python_service-0.0.7-py3.6.egg/pyservice/service.py", line 135, in run_client
ConnectionRefusedError: [Errno 111] Connection refused"

Try deleting ~/.service_*_test.pid and rerunning
