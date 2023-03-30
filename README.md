# gku-proxy

This project aims to develop collaborative development skills. The planned functionality of the application: receiving a request from the user, duplicating this request to several APIs and issuing a consolidated response to the user.

## Installation

```console
git clone && cd gku-proxy
```

### Requires

- [python3.11](https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux/)
- [pdm](https://pdm.fming.dev/latest/)

## Development

To install all dependencies

```console
pdm install
```

To run autoformatting, linting

```console

pdm run test
```

To run unittest localy

```console

pdm run lint-all
```

To run app localy

```console
pdm run start
```
