FROM certbot/certbot:v1.11.0

COPY generate_certificates.sh /bin

RUN chmod +x /bin/generate_certificates.sh

# only meant to be run via docker-compose run --entrypoint generate_certificates.sh certs
ENTRYPOINT [ "echo", "run 'docker-compose run --entrypoint generate_certificates.sh certs' to generate certificates" ]