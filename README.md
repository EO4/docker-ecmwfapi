# docker-ecmwfapi
Docker container with alpine linux, python 3.6 and ECMWF API

# Set up ECMWF API access

Need to register, accept SLA, and get API key (.ecmwfapirc).

+ https://software.ecmwf.int/wiki/display/CKB/How+to+download+data+via+the+ECMWF+WebAPI

# Build container

```
cd docker-ecmwfapi
docker build --tag="eo4/ecmwfapi:latest" .
```

# Run container

+ Create a working directory
+ Add your .ecmwfapirc to the working directory
+ Add your API python script to the working directory
+ Run the container, mounting the working directory volume; .ecmwfapirc will be copied to 'root' in container
+ Data will appear in 'my_working_directory'

```
mkdir ~/my_working_directory
cp ~/.ecmwfapirc ~/my_working_directory
# Create API script 'test.py' in 'my_working_directory'
docker run -it --rm --name ecmwfapitest -v ~/my_working_directory:/usr/src/myapp eo4/ecmwfapi:latest python test.py
```
