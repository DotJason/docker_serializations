# docker_serializations

A simple service timing Python implementations of different serialization protocols distributed through multiple Docker containers

The structure being used for serialization is a static Python dict that is defined in `checker.py`. It includes integer, floating point, string, array and (nested) dict values, as well as an array of `1000` integers to properly test the protocols' performance

## Setup

1. Install [Docker](https://www.docker.com/)
2. Clone this repository to your local machine
3. Navigate to the repository's root directory (where `docker-compose.yml` is)
4. Run the app by executing the following commands:
```console
docker-compose build
docker-compose up
```

## Usage

The app provides a server with a simple HTTP interface listening on port `2000`. One can query it (from their local machine) by the following URL: 
```
http://localhost:2000/format
```
where `format` shall be substituted for one of the following strings, corresponding to available formats:
```
pickle
xml
json
yaml
msgpack
```

It returns a plain text response in the following format:
```
{protocol name} - {object serialization size in bytes} - {serialization time} - {deserialization time}
```

### Example

In the console:
```console
wget localhost:2000/xml -q -O -
```
Or in the web browser:
```
localhost:2000/xml
```
Output (one might have to wait ~5 seconds for the tests to complete with some formats):
```
XML - 14667 - 1.8473287720007647ms - 1.773440095999831ms
```

## Implementation details

The app runs a container for each supported serialization protocol. Inside, another HTTP server is listening to a port (from `2001` to `2007`). The `main` container server (running on port `2000`), upon recieving a query, queries the corresponding server for test data and passes the response to the user.

Tests are executed for every query, so results may vary between different responses for the same format.
