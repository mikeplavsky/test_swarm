docker build -t mikeplavsky/swarm:0.1 .

docker rm -f sw 
docker run -d \
    --name=sw \
    -v $(pwd):/sw  \
    -p 80:5000 \
    mikeplavsky/swarm:0.1 \
    python /sw/run.py
