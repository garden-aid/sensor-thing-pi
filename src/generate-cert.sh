#!/bin/bash

if [ ! -f !$AWS_IOT_CA_KEY_PATH ]; then
    $AWS_IOT_CA_KEY > $AWS_IOT_CA_KEY_PATH
fi

if [ ! -f !$AWS_IOT_CA_CERT_PATH ]; then
    $AWS_IOT_CA_CERT > $AWS_IOT_CA_CERT_PATH
fi

if [ ! -f !$AWS_IOT_KEY_PATH || ! -f !$AWS_IOT_CERT_PATH ]; then
    echo "Generating device certificates"

    openssl genrsa -out $AWS_IOT_KEY_PATH 2048
    openssl req -new -key $AWS_IOT_KEY_PATH -out $AWS_IOT_CSR_PATH

    openssl x509 -req \
        -in $AWS_IOT_CSR_PATH \
        -CA $AWS_IOT_CA_CERT_PATH \
        -CAkey $AWS_IOT_CA_KEY_PATH \
        -CAcreateserial \
        -out $AWS_IOT_CERT_PATH \
        -days 365 \
        -sha256

    cat $AWS_IOT_CERT_PATH $AWS_IOT_CA_CERT_PATH > $AWS_IOT_COMBINE_CERT_PATH
fi

