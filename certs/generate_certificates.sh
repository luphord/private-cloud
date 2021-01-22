#!/bin/sh
certbot --manual --preferred-challenges dns --agree-tos -m $CERTIFICATE_MAIL -d $CERTIFICATE_DOMAINS certonly