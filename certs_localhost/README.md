# TLS certificates for localhost

This folder contains a script to generate a certificate for localhost.
This certificate is used alternatively to the traefik default certificate.
Purpose of this approach is to load (and therefore test) certificates in the same way as in production.

## How to run

Simply execute

`./generate_localhost_certificates.sh`

and find the resulting certificate in `cert.pem` and `key.pem`.
These files will be mounted and loaded using the default configuration.
Note that they are ignored by git on purpose (as you will have to trust them).