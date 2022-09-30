from flask import Flask, request, Response
import docker
import requests

# Flask
app = Flask( __name__ )

# Docker
client = docker.from_env()
bindVolume = {'/var/run/docker.sock': {'bind': '/var/run/docker.sock', 'mode': 'rw'}}

@app.route('/webhook', methods=['POST'])
def respond():
    # Check state of image
    data = request.json
    r = requests.get(data["callback_url"])
    if r.status_code != 200:
        return Response(status=500)  # Part

    data = r.json()
    if data["state"] != "success":
        return Response(status=200)

    # pull latest image for everything that was pulled
    client.containers.run('containrrr/watchtower',command=["--run-once", "--label-enable", "--include-restarting", "--cleanup"], name="watchtower", volumes = bindVolume, auto_remove=True)
    return Response(status=200)

if __name__=="__main__":
    app.run()
