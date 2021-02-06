# Private cloud
Management tooling for luphord's private cloud.

## How to develop

For development you will have to generate certificates for localhost by running

`cd certs_localhost && ./generate_localhost_certificates.sh && cd ..`

Afterwards, you can start everything using

`docker-compose up`

## How to run in production

First you will have to adapt the configuration in `.env` according to your needs.
Alternatively, you can create a separate config file and tell docker to use that
by means of `docker-compose run --env-file=<your-config-file>`.

Second you will have to receive Let's Encrypt certificates using the dns-01 challenge.
This procedure is partly automated with

`docker-compose run --entrypoint generate_certificates.sh certs`

during which you will be prompted to place two tokens in your txt records.

In case of duckdns.org, you can only place a single txt record. Therefore, you first have to create the certificate for your subdomain *without* a wildcard star (e.g. `example.duckns.org`). Then you have to run certificate generation again for your subdomain *and* your subdomain *with* wildcard star (e.g. `example.duckns.org,*.example.duckns.org`) to perform an expansion.

After configuration and certificate generation, you can start everything using

`docker-compose up`

or possible

`docker-compose up --env-file=<your-config-file>`