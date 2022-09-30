# dockerwebhook

A simple python flask server that listens for dockerhub webhooks

## Install

`pip install git+https://github.com/Blotz/dockerwebhook.git`

## Run

`waitress-serve --host 127.0.0.1 dockerwebhook:app`

## Deets

The webserver is listening to post requests on http://localhost/webhook

configure and port forward your server so that this is public to the internet

containers are updated based on whether they have the `com.centurylinklabs.watchtower.enable` label


